import glob
import os
import sqlite3

def listing_SQLite3_DB(file, DBtable):
    con = sqlite3.connect(file)
    cur = con.cursor()
    cur.execute("SELECT * FROM " + DBtable)
    rows = cur.fetchall()
    for row in rows:
        print(row)

cookie_exefileD = glob.glob(os.path.join(os.getenv('APPDATA', ''), '..\Local\\Google\\Chrome\\User Data\\Default\\Cookies'))
#cookie_exefileD = glob.glob(os.path.join(os.getenv('APPDATA', ''), '..\Local\\Google\\Chrome\\User Data\\Default\\Login_Data'))
cookie_exefile = cookie_exefileD[0]
# cookie_exefile = 'C:\\Users\\penggunabiasa\\python3_projects\\Selenium\\MengKome\\chromedata\\Default\\Cookies'
# cookie_exefile = 'chromedata\\Default\\Cookies'
# cookie_exefile = 'chromedata\\Default\\History2'
# cookie_exefile = 'chromedata\\Default\\Login_Data'
# cookie_exefile = 'chromedata\\Default\\Web Data'
# cookie_exefile = glob.glob(os.path.join(os.getenv('APPDATA', ''), '..\Local\\Google\\Chrome\\User Data\\Default\\Cookies'))

print('DB FILE = ' + cookie_exefile)
listing_SQLite3_DB(cookie_exefile, 'cookies')