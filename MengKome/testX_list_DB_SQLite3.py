import glob
import os
import sqlite3
from time import sleep
from shutil import copy2

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
    if len(rows) >= 1:
        i = 1
        for row in rows:
            print(str(i) + ') ' + str(row))
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

# DB file & DB table
####################
# 1) DB of Cookies
# file = 'Cookies'; dbtable = 'cookies'
#2) DB of Login Data - have username & password
file = 'Login Data'; dbtable = 'logins'
#3) DB of History
# file = 'History'; dbtable = 'visits'
# file = 'History'; dbtable = 'urls'
#4) DB of Web Data
# file = 'Web Data'; dbtable = 'autofill'
# file = 'Web Data'; dbtable = 'token_service'
# file = 'Web Data'; dbtable = 'unmasked_credit_cards'
# file = 'Web Data'; dbtable = 'masked_credit_cards'
# file = 'Web Data'; dbtable = 'autofill_profiles'
# file = 'Web Data'; dbtable = 'credit_cards'

# EXECUTE command to check the DB
listing_SQLite3_DB(filepath, file, dbtable)



