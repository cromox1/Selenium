import glob
import os
import sqlite3

def listing_SQLite3_DB(filepath, file, DBtable):
    print('\nDB FILE = ' + filepath + file + '\n')
    con = sqlite3.connect(filepath + file)
    cur = con.cursor()
    cur.execute("SELECT * FROM " + DBtable)
    rows = cur.fetchall()
    for row in rows:
        print(row)

# filepath
##########
# 1) Chrome Default
# -- > /cygdrive/c/Users/taverner/AppData/Local/Google/Chrome/User Data/Default
filepath = glob.glob(os.path.join(os.getenv('APPDATA', ''), '..\Local\\Google\\Chrome\\User Data\\Default\\'))[0]
# 2) chrome specific directory - chromedata
# 'C:\\Users\\penggunabiasa\\python3_projects\\Selenium\\MengKome\\chromedata\\Default\\Cookies'
# filepath = 'chromedata\\Default\\'

# DB file & DB table
####################
# 1) DB of Cookies
# file = 'Cookies'
# dbtable = 'cookies'
#2) DB of Login Data - have username & password
file = 'Login_Data'  # need to copy first - as it still open
dbtable = 'logins'
#3) DB of History
# file = 'History2'
# dbtable = 'visits'
# dbtable = 'urls'
#4 DB of Web Data
# file = 'Web_Data'
# dbtable = 'autofill'
# dbtable = 'token_service'
# dbtable = 'unmasked_credit_cards'
# dbtable = 'masked_credit_cards'
# dbtable = 'autofill_profiles'
# dbtable = 'credit_cards'

# EXECUTE command to check the DB
listing_SQLite3_DB(filepath, file, dbtable)



