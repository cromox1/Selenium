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
from Crypto.Cipher._mode_gcm import GcmMode

def tukar(ciphertext, output=None):
    # __import__(ciphertext)
    print('TYPE 1 = ' + str(type(ciphertext)))
    tukaran = GcmMode.decrypt(ciphertext)
    print('TYPE 2 = ' + str(type(tukaran)))
    return tukaran

def listing_SQLite3_DB(filepath, file, DBtable):
    # from Crypto.Cipher import _mode_gcm as tukar
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
            # print(str(_decrypt(row[user1], row[user2])) + '  /=/=/  ' + str(_decrypt(row[pswd1], row[pswd2])))
            print('USER = ' + str(str(row[user2])) + ' / PSWD = ' + str(str(row[pswd2])))
            # print(' PSWD = ' + str(tukar(str(row[pswd2]))))
            print(' PSWD = ' + str(GcmMode.decrypt(row[pswd2])))
            # print(str(row[user1]) + '  /=/  ' + str(row[user2]) + '  /=/  ' + str(row[pswd1]) + '  /=/  ' + str(row[pswd2]))
            # print(str())
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