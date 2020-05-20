import base64
import binascii
import glob
import hashlib
import json
import os
import sqlite3
import subprocess
import sys
from time import sleep, strftime, localtime
from shutil import copy2
from Crypto.Cipher import AES
import pyaes
# from browser_cookie3 import crypt_unprotect_data

# from pyaes import AES
# from pbkdf2 import PBKDF2
from Crypto.Cipher._mode_gcm import GcmMode

def tukar(ciphertext, output=None):
    # __import__(ciphertext)
    print('TYPE 1 = ' + str(type(ciphertext)))
    tukaran = GcmMode.decrypt(ciphertext)
    print('TYPE 2 = ' + str(type(tukaran)))
    return tukaran

def decrypt2(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def decrypt3(ciphertext, key):
    unpad = lambda s: s[:-s[-1]]
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext))[AES.block_size:]
    return plaintext

def decrypt4(encryptedB64):
    encrypted = base64.b64decode(encryptedB64 + '===')
    iv = encrypted[:AES.block_size]
    key = hashlib.sha256(base64.encode('utf-8')).digest()
    cipher = AES.new(key, AES.MODE_CBC, iv )
    decrypted = cipher.decrypt(encrypted[AES.block_size:]) #<-- error on this line
    return decrypted

def decrypt5(encrypted, key):
    '''
    The reason that the passwords showed up like they did is because they are encrypted with a pbkdf2
    key that is stored in a specific keychain location (usually having the name 'Chrome' in it). To find
    this key you can execute the command
        security find-generic-password -wa 'Chrome'
        (as an administrator)
    and it should pull the key for you.

    ref = https://security.stackexchange.com/questions/186513/retreiving-google-chrome-passwords
    '''
    iv = ''.join(('20', ) * 16)
    key = hashlib.pbkdf2_hmac('sha1', key, b'saltysalt', 1003)[:16]

    hex_key = binascii.hexlify(key)
    hex_enc_password = base64.b64encode(encrypted[3:])
    try:
        decrypted = subprocess.check_output(
            "openssl enc -base64 -d "
            "-aes-128-cbc -iv '{}' -K {} <<< "
            "{} 2>/dev/null".format(iv, hex_key, hex_enc_password),
            shell=True)
    except subprocess.CalledProcessError:
        decrypted = "n/a"

    return decrypted

def _decrypt_v80(buff):
    masterkey_list = ['08036b55-a738-4671-a95e-e082849fc957', '4b384997-1fdf-469a-bb6c-6826890b8555', '5812b20c-c9b7-4790-99dd-7a74113d54c1',
                      '6f2dbbee-4f30-4f30-9354-019bcbe88777', '9461c677-c2e6-47ab-b42c-0d91116f9892', '9691f273-64fe-4d61-8bf2-571f51ed342e',
                      '9965cc23-4c21-46fe-8e3a-662ff3df1f65', 'd5c3487b-1f76-4f3b-b29f-1aa0f1030e35', 'd6883d3f-a1e2-407c-99b2-4c1553f8bab4']
    for master_key in masterkey_list:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        print('IV = ' + str(iv) + ' // PAYLOAD = ' + str(payload) + ' // CIPHER = ' + str(cipher))
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
    if decrypted_pass:
        return decrypted_pass
    else:
        return None

def listing_SQLite3_DB(filepath, file, DBtable):
    # from Crypto.Cipher import _mode_gcm as tukar
    print('\nDB FILE = ' + filepath + file)
    copy2(src=filepath+file, dst=filepath+'mytmp123')
    sleep(1)
    con = sqlite3.connect(filepath + 'mytmp123')
    cur = con.cursor()
    sqlcommand = "SELECT * FROM " + str(DBtable) + " ORDER BY date_created ASC"
    print('SQL req = ' + sqlcommand + '\n')
    cur.execute(sqlcommand)
    names = [description[0] for description in cur.description]
    print(str(names) + '\n')
    rows = cur.fetchall()
    # print(rows)
    user1 = 2; user2 = 3
    pswd1 = 4; pswd2 = 5
    date1 = 9
    print(str(names[date1]) + ' // ' + str(names[user1]) + ' // ' + str(names[user2]) + ' // ' + str(names[pswd1]) + ' // ' + str(names[pswd2]))
    if len(rows) >= 1:
        i = 0
        for row in rows:
            if row[user1] or row[user2]:
                i = i+1
                value1 = row[date1]
                value2 = (value1 / 1000000) - 11644473600
                masa = strftime('%Y-%m-%d %H:%M:%S', localtime(int(value2)))
                dcydata = row[pswd2]
                # print(str(_decrypt(row[user1], row[user2])) + '  /=/=/  ' + str(_decrypt(row[pswd1], row[pswd2])))
                # print('USER = ' + str(str(row[user2])) + ' / PSWD = ' + str(str(row[pswd2])))
                # print(' PSWD = ' + str(tukar(str(row[pswd2]))))
                # print(' PSWD = ' + str(GcmMode.decrypt(row[pswd2])))
                # print(str(i) + ') ' + str(masa) + ' // ' + str(row[user1]) + ' // ' + str(row[user2]) + ' // ' + str(row[pswd1]) + ' // ' + str(row[pswd2]))
                # print(str(i) + ') ' + str(masa) + ' // ' + str(crypt_unprotect_data(dcydata)))
                # print(str(i) + ') ' + str(masa) + ' // ' + str(GcmMode.decrypt(str(dcydata))))
                # key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
                # key = hashlib.sha256(base64.encode('utf-8')).digest()
                print(str(i) + ') ' + str(masa) + ' // ' + str(_decrypt_v80(dcydata)))
                # print(str(i) + ') ' + str(masa) + ' // ' + str(row[user2]) + ' // ' + str(dcydata))

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