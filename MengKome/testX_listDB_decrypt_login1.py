import glob
import os
import sqlite3
import sys
# from datetime import datetime
from time import sleep, strftime, localtime
from shutil import copy2
from Crypto.Cipher import AES
import pyaes
# from browser_cookie3 import crypt_unprotect_data
# from pyaes import AES
from pbkdf2 import PBKDF2

def listing_SQLite3_DB(filepath, file, DBtable):
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
    date1 = 9
    print(str(names[date1]) + '  //  ' + str(names[user1]) + '  //  ' + str(names[user2]) + '  //  ' + str(names[pswd1]) + '  //  ' + str(names[pswd2] + '\n'))
    if len(rows) >= 1:
        i = 1
        for row in rows:
            if row[user2]:
                # masa = strftime('%Y-%m-%d %H:%M:%S', localtime(row[date1]))
                # (130305048577611542 / 10000000) - 11644473600
                value1 = row[date1]
                value2 = (value1/1000000) - 11644473600
                # print('value1 = ' + str(value1) + ' / value2 = ' + str(value2))
                masa = strftime('%Y-%m-%d %H:%M:%S', localtime(int(value2)))
                print(str(i) + ') ' + str(masa) + '  //  ' + str(row[user1]) + '  //  ' + str(row[user2]) + '  //  ' + str(row[pswd1]) + '  //  ' + str(row[pswd2]) + '\n')
                i = i+1
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