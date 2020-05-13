import browser_cookie3
import time

cookies = browser_cookie3.chrome()
# print('COOKIE_ALL = ' + str(cookies))
i=1
for c in cookies:
    timeexpire = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(c.expires))
    print(str(i) + ') ' + str(c.domain) + ' / ' + str(c.name) + ' / ' + str(c.value) + ' / ' + str(timeexpire))
    i=i+1

base_url = "https://mengkome.pythonanywhere.com/admin/login/"
urlx = str(base_url.split('://')[1].split('/')[0])
print('URLX = ' + urlx)
# urlx = '.pythonanywhere.com'
# urlx = 'mengkome.pythonanywhere.com'
# urlx = '.google.com'
cookies = browser_cookie3.chrome(domain_name=urlx)
if len(cookies) >= 1:
    cookie = {}
    for c in cookies:
        # cookie = {'domain': c.domain, 'name': c.name, 'value': c.value, 'secure': c.secure and True or False}
        cookie = {'domain': c.domain, 'name': c.name, 'value': c.value, 'expiry': c.expires, 'path': c.path, 'secure': c.secure and True or False}
    print('COOKIE1 [ ' + urlx + ' / ' + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(c.expires))) + ' ] = ' + str(cookie))
else:
    print('COOKIE1 [ ' + urlx + ' ] = NONE')

# urlx = 'mengkome.pythonanywhere.com'
urlx = '.google.com'
# cookies = browser_cookie3.chrome(domain_name=urlx, cookie_file='C:/Users/cromox/Desktop/newselenium/Selenium/MengKome/chrome-data/Default/Cookies')
cookies = browser_cookie3.chrome(domain_name=urlx)

if len(cookies) >= 1:
    cookie = {}
    for c in cookies:
        cookie = {'domain': c.domain, 'name': c.name, 'value': c.value, 'expiry': c.expires, 'path': c.path, 'secure': c.secure and True or False}
    print('COOKIE2 [ ' + urlx + ' / ' + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(c.expires))) + ' ] = ' + str(cookie))
else:
    print('COOKIE2 [ ' + urlx + ' ] = NONE')