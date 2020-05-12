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
# urlx = 'mengkome.pythonanywhere.com'
urlx = '.google.com'
cookies = browser_cookie3.chrome(domain_name=urlx, cookie_file='C:/Users/cromox/Desktop/newselenium/Selenium/MengKome/chrome-data/Default/Cookies')
# response = requests.get('http://www.google.com', verify=False, headers=headers, cookies=cookies, timeout=3)

cookie = {}
for c in cookies:
    cookie = {'domain': c.domain, 'name': c.name, 'value': c.value, 'secure': c.secure and True or False}

print('COOKIE1 = ' + str(cookie))
#     driver.add_cookie(cookie)
# driver.get('http://www.google.com')

# urlx = 'mengkome.pythonanywhere.com'
# urlx = '.google.com'
cookies = browser_cookie3.chrome(cookie_file='C:/Users/cromox/Desktop/newselenium/Selenium/MengKome/chrome-data/Default/Cookies')
# response = requests.get('http://www.google.com', verify=False, headers=headers, cookies=cookies, timeout=3)

cookie = {}
for c in cookies:
    cookie = {'domain': c.domain, 'name': c.name, 'value': c.value, 'secure': c.secure and True or False}

print('COOKIE2 = ' + str(cookie))