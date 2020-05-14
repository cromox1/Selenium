import glob
import os

import browser_cookie3
import requests

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
    "Accept-Encoding":"gzip, deflate",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT":"1",
    "Connection":"close",
    "Upgrade-Insecure-Requests":"1"
}

# urlx = '.pythonanywhere.com'
urlx = 'mengkome.pythonanywhere.com'
# urlx = '.google.com'
# cookie_exefile = glob.glob(os.path.join(os.getenv('APPDATA', ''), '..\Local\\Google\\Chrome\\User Data\\Default\\Cookies'))
# cookie_exefile = 'C:\\Users\\penggunabiasa\\python3_projects\\Selenium\\MengKome\\chromedata\\Default\\Cookies'
cookie_exefile = 'chromedata\\Default\\Cookies'
# cookie_exefile = 'chromedata\\Default\\History2'
# cookie_exefile = 'chromedata\\Default\\Login Data'
# cookie_exefile = 'chromedata\\Default\\Web Data'
# cookie_exefile = glob.glob(os.path.join(os.getenv('APPDATA', ''), '..\Local\\Google\\Chrome\\User Data\\Default\\Cookies'))
print('COOKIE_EXE_FILE = ' + str(cookie_exefile))
cookies = browser_cookie3.chrome(domain_name=urlx, cookie_file=cookie_exefile)
# response = requests.get('http://www.google.com', verify=False, headers=headers, cookies=cookies, timeout=3)

cookie = {}
if len(cookies) >= 1:
    # cookie = {}
    for c in cookies:
        cookie = {'domain': c.domain,
                                 'name': c.name,
                                 'value': c.value,
                                 'expiry': c.expires,
                                 'path': c.path,
                                 'httpOnly': False,
                                 'HostOnly': False,
                                 'secure': c.secure and True or False}
else:
    cookie = {'domain': urlx}

print('COOKIE1 = ' + str(cookie))
#     driver.add_cookie(cookie)
# driver.get('http://www.google.com')

# urlx = 'mengkome.pythonanywhere.com'
# urlx = '.google.com'
cookies = browser_cookie3.chrome(cookie_file=cookie_exefile)
# response = requests.get('http://www.google.com', verify=False, headers=headers, cookies=cookies, timeout=3)

cookie = {}
if len(cookies) >= 1:
    # cookie = {}
    for c in cookies:
        cookie = {'domain': c.domain,
                                 'name': c.name,
                                 'value': c.value,
                                 'expiry': c.expires,
                                 'path': c.path,
                                 'httpOnly': False,
                                 'HostOnly': False,
                                 'secure': c.secure and True or False}
else:
    cookie = {}

print('COOKIE2 = ' + str(cookie))