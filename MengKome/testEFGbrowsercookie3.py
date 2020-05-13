import browser_cookie3

base_url = "https://mengkome.pythonanywhere.com/admin/login/"
print('URLX = ' + str(base_url.split('://')[1].split('/')[0]))
# urlx = '.pythonanywhere.com'
urlx = 'mengkome.pythonanywhere.com'
# urlx = '.google.com'
cookies = browser_cookie3.chrome(domain_name=urlx)

cookie = {}
for c in cookies:
    cookie = {'domain': c.domain, 'name': c.name, 'value': c.value, 'secure': c.secure and True or False}
print('COOKIE1 [ ' + urlx + ' ] = ' + str(cookie))

# urlx = 'mengkome.pythonanywhere.com'
urlx = '.google.com'
# cookies = browser_cookie3.chrome(domain_name=urlx, cookie_file='C:/Users/cromox/Desktop/newselenium/Selenium/MengKome/chrome-data/Default/Cookies')
cookies = browser_cookie3.chrome(domain_name=urlx)

cookie = {}
for c in cookies:
    cookie = {'domain': c.domain, 'name': c.name, 'value': c.value, 'secure': c.secure and True or False}
print('COOKIE2 [ ' + urlx + ' ] = ' + str(cookie))