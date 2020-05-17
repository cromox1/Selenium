import glob
import os
import sqlite3
import sys
from time import sleep
from shutil import copy2
from Crypto.Cipher import AES
import pyaes
# from browser_cookie3 import crypt_unprotect_data
# from pyaes import AES
from pbkdf2 import PBKDF2

def crypt_unprotect_data(cipher_text=b'', entropy=b'', reserved=None, prompt_struct=None, is_key=False
):
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

def _decrypt_windows_chrome(value, encrypted_value):
    # if len(value) != 0:
    #     return value

    if encrypted_value == "":
        return ""

    _, data = crypt_unprotect_data(encrypted_value)
    assert isinstance(data, bytes)
    return data.decode()

def _decrypt(value, encrypted_value):
    """Decrypt encoded cookies
    """
    from browser_cookie3 import get_linux_pass
    salt = b'saltysalt'
    iv = b' ' * 16
    length = 16
    my_pass = get_linux_pass(browser="Chrome").encode('utf8')
    iterations = 1  # number of pbkdf2 iterations on linux
    key = PBKDF2(my_pass, salt, iterations=iterations).read(length)
    if sys.platform == 'win32':
        try:
            return _decrypt_windows_chrome(value, encrypted_value)

        # Fix for change in Chrome 80
        except RuntimeError:  # Failed to decrypt the cipher text with DPAPI
            if not key:
                raise RuntimeError(
                    'Failed to decrypt the cipher text with DPAPI and no AES key.')
            # Encrypted cookies should be prefixed with 'v10' according to the
            # Chromium code. Strip it off.
            encrypted_value = encrypted_value[3:]
            nonce, tag = encrypted_value[:12], encrypted_value[-16:]
            print('TAG = ' + str(tag) + ' / NONCE = ' + str(nonce))
            aes = AES.new(key, AES.MODE_GCM, nonce=nonce)
            print('AES = ' + str(aes))
            data = aes.decrypt_and_verify(encrypted_value[12:-16], tag)
            print('DATA = ' + str(data))
            return data.decode()

    if value or (encrypted_value[:3] not in [b'v11', b'v10']):
        return value

    # Encrypted cookies should be prefixed with 'v10' according to the
    # Chromium code. Strip it off.
    encrypted_value = encrypted_value[3:]
    encrypted_value_half_len = int(len(encrypted_value) / 2)

    cipher = pyaes.Decrypter(
        pyaes.AESModeOfOperationCBC(key, iv))
    decrypted = cipher.feed(encrypted_value[:encrypted_value_half_len])
    decrypted += cipher.feed(encrypted_value[encrypted_value_half_len:])
    decrypted += cipher.feed()
    return decrypted.decode("utf-8")

def _update(self, data):
    assert(len(self._cache) < 16)

    if len(self._cache) > 0:
        filler = min(16 - len(self._cache), len(data))
        self._cache += _copy_bytes(None, filler, data)
        data = data[filler:]

        if len(self._cache) < 16:
            return

        # The cache is exactly one block
        self._signer.update(self._cache)
        self._cache = b""

    update_len = len(data) // 16 * 16
    self._cache = _copy_bytes(update_len, None, data)
    if update_len > 0:
        self._signer.update(data[:update_len])

def tukar(ciphertext, output=None):
    # Allowed transitions after initialization
    # _next = [update, encrypt, decrypt, digest, verify]
    #
    # if decrypt not in _next:
    #     raise TypeError("decrypt() can only be called"
    #                     " after initialization or an update()")
    _next = [decrypt, verify]

    _update(ciphertext)
    _msg_len += len(ciphertext)

    return _cipher.decrypt(ciphertext, output=output)

def listing_SQLite3_DB(filepath, file, DBtable):
    from Crypto.Cipher import _mode_gcm as tukar
    print('\nDB FILE = ' + filepath + file)
    copy2(src=filepath+file, dst=filepath+'mytmp123')
    sleep(1)
    con = sqlite3.connect(filepath + 'mytmp123')
    cur = con.cursor()
    sqlcommand = "SELECT * FROM " + str(DBtable)
    print('SQL req = ' + sqlcommand + '\n')
    cur.execute(sqlcommand)
    names = [description[0] for description in cur.description]
    print(str(names) + '\n')
    rows = cur.fetchall()
    # print(rows)
    user1 = 2
    user2 = 3
    pswd1 = 4
    pswd2 = 5
    print(str(names[user1]) + '  /=/  ' + str(names[user2]) + '  /=/  ' + str(names[pswd1]) + '  /=/  ' + str(names[pswd2]))
    if len(rows) >= 1:
        for row in rows:
            print(str(_decrypt(row[user1], row[user2])) + '  /=/=/  ' + str(_decrypt(row[pswd1], row[pswd2])))
            # print('USER = ' + str(tukar()))
            # print(str(row[user1]) + '  /=/  ' + str(row[user2]) + '  /=/  ' + str(row[pswd1]) + '  /=/  ' + str(row[pswd2]))
            print(str())
    else:
        print('SQLTABLE ' + DBtable + ' EMPTY - NO DATA')
    sleep(1); con.close(); sleep(1)
    os.remove(filepath+'mytmp123')

# filepath
##########
# 1) Chrome Default
# -- > /cygdrive/c/Users/taverner/AppData/Local/Google/Chrome/User Data/Default
filepath = glob.glob(os.path.join(os.getenv('APPDATA', ''), '..\Local\\Google\\Chrome\\User Data\\Default\\'))[0]
# 2) chrome specific directory - chromedata
# -- > 'C:\\Users\\penggunabiasa\\python3_projects\\Selenium\\MengKome\\chromedata\\Default\\Cookies'
# filepath = 'chromedata\\Default\\'

file = 'Login Data'; dbtable = 'logins'

# EXECUTE command to check the DB
listing_SQLite3_DB(filepath, file, dbtable)