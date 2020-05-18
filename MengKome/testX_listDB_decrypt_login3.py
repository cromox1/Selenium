import os
import os.path
import sys
# import time
import glob
import http.cookiejar
# import tempfile
# import lz4.block
import datetime
# import configparser
import base64
from Crypto.Cipher import AES

try:
    import json
except ImportError:
    import simplejson as json

try:
    # should use pysqlite2 to read the cookies.sqlite on Windows
    # otherwise will raise the "sqlite3.DatabaseError: file is encrypted or is not a database" exception
    from pysqlite2 import dbapi2 as sqlite3
except ImportError:
    import sqlite3

# external dependencies
import keyring
import pyaes
from pbkdf2 import PBKDF2

__doc__ = 'Load browser cookies into a cookiejar'

# Code adapted slightly from https://github.com/Arnie97/chrome-cookies

def crypt_unprotect_data(cipher_text=b'', entropy=b'', reserved=None, prompt_struct=None, is_key=False):
    # we know that we're running under windows at this point so it's safe to try these imports
    import ctypes
    import ctypes.wintypes

    class DataBlob(ctypes.Structure):
        _fields_ = [
            ('cbData', ctypes.wintypes.DWORD),
            ('pbData', ctypes.POINTER(ctypes.c_char))
        ]

    blob_in, blob_entropy, blob_out = map(
        lambda x: DataBlob(len(x), ctypes.create_string_buffer(x)),
        [cipher_text, entropy, b'']
    )
    desc = ctypes.c_wchar_p()

    CRYPTPROTECT_UI_FORBIDDEN = 0x01

    if not ctypes.windll.crypt32.CryptUnprotectData(
            ctypes.byref(blob_in), ctypes.byref(
                desc), ctypes.byref(blob_entropy),
            reserved, prompt_struct, CRYPTPROTECT_UI_FORBIDDEN, ctypes.byref(
                blob_out)
    ):
        raise RuntimeError('Failed to decrypt the cipher text with DPAPI')

    description = desc.value
    buffer_out = ctypes.create_string_buffer(int(blob_out.cbData))
    ctypes.memmove(buffer_out, blob_out.pbData, blob_out.cbData)
    map(ctypes.windll.kernel32.LocalFree, [desc, blob_out.pbData])
    if is_key:
        return description, buffer_out.raw
    else:
        return description, buffer_out.value

def get_linux_pass(browser="Chrome"):
    # Try to get pass from Gnome / libsecret if it seems available
    # https://github.com/n8henrie/pycookiecheat/issues/12
    my_pass = None
    try:
        import gi

        gi.require_version("Secret", "1")
        from gi.repository import Secret
    except (ImportError, AttributeError):
        pass
    else:
        flags = Secret.ServiceFlags.LOAD_COLLECTIONS
        service = Secret.Service.get_sync(flags)

        gnome_keyring = service.get_collections()
        unlocked_keyrings = service.unlock_sync(gnome_keyring).unlocked

        keyring_name = "{} Safe Storage".format(browser.capitalize())

        for unlocked_keyring in unlocked_keyrings:
            for item in unlocked_keyring.get_items():
                if item.get_label() == keyring_name:
                    item.load_secret_sync()
                    my_pass = item.get_secret().get_text()
                    break
            else:
                # Inner loop didn't `break`, keep looking
                continue

            # Inner loop did `break`, so `break` outer loop
            break

    # Try to get pass from keyring, which should support KDE / KWallet
    # if dbus-python is installed.
    if not my_pass:
        try:
            my_pass = keyring.get_password(
                "{} Keys".format(browser), "{} Safe Storage".format(browser)
            )
        except RuntimeError:
            pass

    if my_pass:
        return my_pass
    else:
        return "peanuts"


class Chrome:
    def __init__(self, cookie_file=None, domain_name=""):
        self.salt = b'saltysalt'
        self.iv = b' ' * 16
        self.length = 16
        # domain name to filter cookies by
        self.domain_name = domain_name

        if sys.platform.startswith('linux'):
            # running Chrome on Linux
            # chrome linux is encrypted with the key peanuts
            my_pass = get_linux_pass().encode('utf8')
            iterations = 1
            self.key = PBKDF2(my_pass, self.salt,
                              iterations=iterations).read(self.length)
            paths = map(os.path.expanduser, [
                '~/.config/google-chrome/Default/Cookies',
                '~/.config/chromium/Default/Cookies',
                '~/.config/google-chrome-beta/Default/Cookies'
            ])
            cookie_file = cookie_file or next(
                filter(os.path.exists, paths), None)
        elif sys.platform == "win32":

            # Read key from file
            key_file = glob.glob(os.path.join(os.getenv('APPDATA', ''), '..\Local\\Google\\Chrome\\User Data\\Local State')) \
                or glob.glob(os.path.join(os.getenv('LOCALAPPDATA', ''), 'Google\\Chrome\\User Data\\Local State')) \
                or glob.glob(os.path.join(os.getenv('APPDATA', ''), 'Google\\Chrome\\User Data\\Local State'))

            if isinstance(key_file, list):
                if key_file:
                    key_file = key_file[0]

            if key_file:
                f = open(key_file, 'rb')
                key_file_json = json.load(f)
                key64 = key_file_json['os_crypt']['encrypted_key'].encode(
                    'utf-8')

                # Decode Key, get rid of DPAPI prefix, unprotect data
                keydpapi = base64.standard_b64decode(key64)[5:]
                _, self.key = crypt_unprotect_data(keydpapi, is_key=True)

    def __str__(self):
        return 'chrome'

    def load(self, cookie_file):
        """Load sqlite cookies into a cookiejar
        """
        con = sqlite3.connect(cookie_file)
        cur = con.cursor()
        try:
            # chrome <=55
            cur.execute('SELECT host_key, path, secure, expires_utc, name, value, encrypted_value '
                        'FROM cookies WHERE host_key like "%{}%";'.format(self.domain_name))
        except sqlite3.OperationalError:
            # chrome >=56
            cur.execute('SELECT host_key, path, is_secure, expires_utc, name, value, encrypted_value '
                        'FROM cookies WHERE host_key like "%{}%";'.format(self.domain_name))

        cj = http.cookiejar.CookieJar()
        epoch_start = datetime.datetime(1601, 1, 1)
        for item in cur.fetchall():
            host, path, secure, expires, name = item[:5]
            if item[3] != 0:
                # ensure dates don't exceed the datetime limit of year 10000
                try:
                    offset = min(int(item[3]), 265000000000000000)
                    delta = datetime.timedelta(microseconds=offset)
                    expires = epoch_start + delta
                    expires = expires.timestamp()
                # Windows 7 has a further constraint
                except OSError:
                    offset = min(int(item[3]), 32536799999000000)
                    delta = datetime.timedelta(microseconds=offset)
                    expires = epoch_start + delta
                    expires = expires.timestamp()

            value = self._decrypt(item[5], item[6])
            c = create_cookie(host, path, secure, expires, name, value)
            cj.set_cookie(c)
        con.close()
        return cj

    @staticmethod
    def _decrypt_windows_chrome(value, encrypted_value):

        if len(value) != 0:
            return value

        if encrypted_value == "":
            return ""

        _, data = crypt_unprotect_data(encrypted_value)
        assert isinstance(data, bytes)
        return data.decode()

    def _decrypt(self, value, encrypted_value):
        """Decrypt encoded cookies
        """

        if sys.platform == 'win32':
            try:
                return self._decrypt_windows_chrome(value, encrypted_value)

            # Fix for change in Chrome 80
            except RuntimeError:  # Failed to decrypt the cipher text with DPAPI
                if not self.key:
                    raise RuntimeError(
                        'Failed to decrypt the cipher text with DPAPI and no AES key.')
                # Encrypted cookies should be prefixed with 'v10' according to the
                # Chromium code. Strip it off.
                encrypted_value = encrypted_value[3:]
                nonce, tag = encrypted_value[:12], encrypted_value[-16:]
                aes = AES.new(self.key, AES.MODE_GCM, nonce=nonce)

                data = aes.decrypt_and_verify(encrypted_value[12:-16], tag)
                return data.decode()

        if value or (encrypted_value[:3] not in [b'v11', b'v10']):
            return value

        # Encrypted cookies should be prefixed with 'v10' according to the
        # Chromium code. Strip it off.
        encrypted_value = encrypted_value[3:]
        encrypted_value_half_len = int(len(encrypted_value) / 2)

        cipher = pyaes.Decrypter(
            pyaes.AESModeOfOperationCBC(self.key, self.iv))
        decrypted = cipher.feed(encrypted_value[:encrypted_value_half_len])
        decrypted += cipher.feed(encrypted_value[encrypted_value_half_len:])
        decrypted += cipher.feed()
        return decrypted.decode("utf-8")

def create_cookie(host, path, secure, expires, name, value):
    """Shortcut function to create a cookie
    """
    return http.cookiejar.Cookie(0, name, value, None, False, host, host.startswith('.'), host.startswith('.'), path,
                                 True, secure, expires, False, None, None, {})

def chrome(cookie_file=None, domain_name=""):
    """Returns a cookiejar of the cookies used by Chrome. Optionally pass in a
    domain name to only load cookies from the specified domain
    """
    return Chrome(cookie_file, domain_name).load()

def load(domain_name=""):
    """Try to load cookies from all supported browsers and return combined cookiejar
    Optionally pass in a domain name to only load cookies from the specified domain
    """
    cj = http.cookiejar.CookieJar()
    for cookie_fn in [chrome]:
        try:
            for cookie in cookie_fn(domain_name=domain_name):
                cj.set_cookie(cookie)
        except:
            pass
    return cj


if __name__ == '__main__':
    print(load())