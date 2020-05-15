import browser_cookie3
import time


def extract_cookie(domainname=""):
    ## Location of Cookie file (specific location + file)
    cookie_exefile = 'chromedata\\Default\\Cookies'
    print('\nCOOKIE_EXE_FILE = ' + str(cookie_exefile))
    cookies = browser_cookie3.chrome(domain_name=domainname, cookie_file=cookie_exefile)
    if domainname == "":
        print()
        i = 1
        for c in cookies:
            timeexpire = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(c.expires))
            print(str(i) + ') ' + str(c.domain) + ' / ' + str(c.name) + ' / ' + str(c.value) + ' / ' + str(timeexpire))
            i = i + 1
        cookie = {}
    else:
        if len(cookies) >= 1:
            cookie = {}
            for c in cookies:
                # cookie = {'domain': c.domain, 'name': c.name, 'value': c.value, 'secure': c.secure and True or False}
                cookie = {'domain': c.domain,
                          'name': c.name,
                          'value': c.value,
                          'expiry': c.expires,
                          'path': c.path,
                          'httpOnly': False,
                          'HostOnly': False,
                          'sameSite': 'None',
                          'secure': c.secure and True or False}
            print('COOKIE [ ' + domainname + ' / ' + str(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(cookie['expiry']))) + ' ] = ' + str(cookie))
        else:
            print('COOKIE [ ' + domainname + ' ] = NONE')
            cookie = {}
    return cookie


# ## Location of Cookie file (specific location + file)
# cookie_exefile = 'chromedata\\Default\\Cookies'
# print('\nCOOKIE_EXE_FILE = ' + str(cookie_exefile))

# 1) ALL COOKIES
extract_cookie()

# 2) mengkome COOKIES
base_url = "https://mengkome.pythonanywhere.com/admin/login/"
print('\n-- > > URL ' + base_url + ' ---- ')
urlx = str(base_url.split('://')[1].split('/')[0])
print('URLX = ' + urlx)
# urlx = '.pythonanywhere.com'
# urlx = 'mengkome.pythonanywhere.com'
extract_cookie(urlx)

# 3) google COOKIES
print('\n-- > > URL .google.com ---- ')
extract_cookie('.google.com')
