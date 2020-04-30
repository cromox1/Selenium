__author__ = 'cromox'
'''
Find ALL existing/avaiable ID/Name/Class/(specificname) using xpath (Selenium element search).
Example:

$ python3 FINDALL_ID_NAME_CLASS_XPATHByType_Selenium_WebDriver_OnPage.py

Put URL = mengkome.pythonanywhere.com
URL = https://mengkome.pythonanywhere.com
What to find [ ID / NAME / CLASS NAME / (specific) ] : name

Python Version = 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)]
Browser version ( chrome ) = 71.0.3578.98

List of ElementID for -- > xpath = //*[@name] :
1) 0.5614896517871395-1 / name = viewport
2) 0.5614896517871395-2 / name = robots
3) 0.5614896517871395-3 / name = csrfmiddlewaretoken
4) 0.5614896517871395-4 / name = username
5) 0.5614896517871395-5 / name = password
6) 0.5614896517871395-6 / name = next

$
(This is using Basic OOP (Object-Oriented Programming))
'''

from selenium import webdriver
import sys

class FindAllIDNameClassUsingXpath():
    def __init__(self, browser, base_url, findwhat):
        self.browser = browser
        self.base_url = base_url
        self.findwhat = findwhat

    def setUp_webdriver(self, browser='chrome'):
        ## Chrome - add_argument='headless' or headless=True, Firefox - add_argument="--headless"
        chromedriverpath = r'C:\tools\python3\Scripts\chromedriver.exe'
        if browser == 'chrome' or browser == 'ch' or browser == 'google':
            from selenium.webdriver.chrome.options import Options
            myoption = Options()
            # myoption.add_argument('headless')
            # myoption.set_headless(headless=True) -- Deprecated
            myoption.add_argument("--proxy-server='direct://'")
            myoption.add_argument("--proxy-bypass-list=*")
            # chromedriver = "/usr/lib/chromium-browser/chromedriver"
            # driver = webdriver.Chrome(chromedriver, options=myoption)
            # (if webdriver need chromedriver - esp in Linux system)
            self.driver = webdriver.Chrome(chromedriverpath, options=myoption)
        elif browser == 'firefox' or browser == "ff":
            from selenium.webdriver.firefox.options import Options
            myoption = Options()
            myoption.add_argument('--headless')
            myoption.add_argument("--proxy-server='direct://'")
            myoption.add_argument("--proxy-bypass-list=*")
            self.driver = webdriver.Firefox(options=myoption)
        else:
            self.driver = webdriver.Chrome(chromedriverpath)
            self.driver.quit()
        self.driver.implicitly_wait(2)
        ### GET python version & Browser version
        print()
        print('Python Version = ' + sys.version)
        print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['browserVersion'])
        print()
        return self.driver

    def xpath_to_use(self, findwhat):
        if findwhat is not None and findwhat != '':
            truefindwhat = findwhat.lower()
            if truefindwhat == 'id' or truefindwhat == 'i':
                valuetofind = '//*[@id]'
                attribute = 'id'
            elif findwhat.lower()[0:2] == 'na':
                valuetofind = '//*[@name]'
                attribute = 'name'
            elif findwhat.lower()[0:2] == 'cl':
                valuetofind = '//*[@class]'
                attribute = 'class'
            elif len(truefindwhat) >= 4:
                valuetofind = '//*[@' + truefindwhat + ']'
                attribute = truefindwhat
            else:
                valuetofind = '//*[@type]'
                attribute = 'type'
        else:
            valuetofind = '//*[@type]'
            attribute = 'type'
        return attribute, valuetofind

    def find_element_xpath(self, driver, valuetofind):
        return driver.find_elements_by_xpath(valuetofind)

    def list_of_ids(self, ids):
        if len(ids) >= 1:            
            print('List of ElementID for -- > xpath = ' + self.valuetofind + ' :')
            i = 1
            for ii in ids:
                try:
                    if ii.get_attribute(self.attribute) is not None and ii.get_attribute(self.attribute) != '':
                        print(str(i) + ') ' + str(ii._id) + ' / ' + self.attribute + ' = ' + str(ii.get_attribute(self.attribute)))
                    elif self.attribute != 'name' and ii.get_attribute('name') is not None and ii.get_attribute('name') != '':
                        print(str(i) + ') ' + str(ii._id) + ' / name = ' + str(ii.get_attribute('name')))
                    elif self.attribute != 'id' and ii.get_attribute('id') is not None and ii.get_attribute('id') != '':
                        print(str(i) + ') ' + str(ii._id) + ' / id = ' + str(ii.get_attribute('id')))
                    elif ii.get_attribute('text') is not None and ii.get_attribute('text') != '':
                        print(str(i) + ') ' + str(ii._id) + ' / text = ' + str(ii.get_attribute('text').replace('\n', "\ENTER\ ").replace('  ', ' ').replace('   ', ' ')[:200]))
                    else:
                        print(str(i) + ') ' + str(ii._id) + ' / id_or_name NOT_EXIST')
                    i+=1
                except:
                    print(str(i) + ') ' + str(ii._id) + ' / ERROR (element is not attached to the page document)')
                    i+=1
        else:
            print('NO ElementID EXIST for -- > xpath = ' + self.valuetofind)

    def final_output(self):
        self.attribute = self.xpath_to_use(self.findwhat)[0]
        self.valuetofind = self.xpath_to_use(self.findwhat)[1]
        self.setUp_webdriver(self.browser)
        self.driver.get(self.base_url)
        ids = self.find_element_xpath(self.driver, self.valuetofind)
        self.list_of_ids(ids)
        self.driver.quit()

####### SCRIPT TO GET INPUT & PUT TO SCRIPT  ######
print()
base_url = input('Put URL = ')
# base_url = 'mengkome.pythonanywhere.com'
if base_url.split('://')[0] == base_url and base_url is not None:
    base_url = 'https://' + base_url
print('URL = ' + base_url)

findwhat = input('What to find [ ID / NAME / CLASS NAME / (specific) ] : ')

#### RUN THE FindAllIDNameClassUsingXpath CLASS
findall = FindAllIDNameClassUsingXpath('chrome', base_url, findwhat)
findall.final_output()
