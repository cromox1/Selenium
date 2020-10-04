__author__ = 'cromox'
'''
to get link_text for specific words on specific page or site.
Example how to run :

$ python LINKTEXT_TEXTByType_Selenium_WebDriver_OnPage.py

Put URL = www.facebook.com
URL = https://www.facebook.com
Partial_Link_Text / Link_Text / All? = pa

Python Version = 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)]
Browser version ( chrome ) = 71.0.3578.98

Text for partial_link_text = Facebook

List of ElementID for -- > partial_link_text = Facebook :
1) 0.7194563140349746-1 / text = Facebook
2) 0.7194563140349746-2 / text = Facebook Lite

$
'''

from selenium import webdriver
import sys

class FindLinkText():
    def __init__(self, browser, partorfull, base_url):
        self.browser = browser
        self.partorfull = partorfull
        self.base_url = base_url

    def setUp_webdriver(self, browser='chrome'):
        ## Chrome - add_argument='headless' or headless=True, Firefox - add_argument="--headless"
        chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
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

    def partial_or_full_linktext(self, partorfull):
        if partorfull is not None and partorfull != '':
            if partorfull[0].lower() == 'p':
                self.attribute = 'partial_link_text'
            elif partorfull[0].lower() == 'l':
                self.attribute = 'link_text'
            else:
                self.attribute = 'link_text'
        else:
            self.attribute = 'link_text'
        return self.attribute

    def get_driver_ids_attb(self):
        self.valuetofind = ''
        self.valuetofind1 = 'ANY'
        self.attribute = self.partial_or_full_linktext(self.partorfull)
        if self.partorfull is not None and len(self.partorfull) >= 1:
            if self.partorfull[0].lower() == 'p' or self.partorfull[0].lower() == 'l':
                self.valuetofind = input('Text for ' + self.attribute + ' = ')
                if self.partorfull[0].lower() == 'p':
                    self.valuetofind1 = self.valuetofind
                    self.driver.get(self.base_url)
                    self.ids = self.driver.find_elements_by_partial_link_text(self.valuetofind)
                elif self.partorfull[0].lower() == 'l':
                    self.valuetofind1 = self.valuetofind
                    self.driver.get(self.base_url)
                    self.ids = self.driver.find_elements_by_link_text(self.valuetofind)
                else:
                    self.driver.get(self.base_url)
                    self.ids = self.driver.find_elements_by_partial_link_text(self.valuetofind)
            else:
                self.driver.get(self.base_url)
                self.ids = self.driver.find_elements_by_partial_link_text(self.valuetofind)
        else:
            self.driver.get(self.base_url)
            self.ids = self.driver.find_elements_by_partial_link_text(self.valuetofind)
        return self.ids

    def find_linktext(self, ids):
        print()
        if len(ids) >= 1:
            print('List of ElementID for -- > ' + self.attribute + ' = ' + self.valuetofind1 + ' :')
            i = 1
            self.attrb1 = 'text'
            self.idserror = []
            for ii in ids:
                if ii.get_attribute(self.attrb1) is not None and ii.get_attribute(self.attrb1) != '':
                    text1 = str(ii.get_attribute(self.attrb1)).replace('\n', "\ENTER\ ").replace('  ', ' ').replace('   ', ' ')[:200]
                    try:
                        if self.driver.find_element_by_link_text(text1) is not None and self.driver.find_element_by_link_text(text1) != '':
                            print(str(i) + ') ' + str(ii._id) + ' / ' + self.attrb1 + ' = ' + text1)
                            i+=1
                    except:
                        self.idserror.append(ii._id)
            if len(self.idserror) >= 1:
                print()
                print('List of ElementID with ERROR (element is not attached to the page document) :')
                for i in range(len(self.idserror)):
                    try:
                        if self.idserror[i].get_attribute('name') is not None and self.idserror[i].get_attribute('name') != '':
                            print(str(i+1) + ') ' + str(self.idserror[i]) + ' / name = ' + str(self.idserror[i].get_attribute('name')))
                        elif self.idserror[i].get_attribute('id') is not None and self.idserror[i].get_attribute('id') != '':
                            print(str(i+1) + ') ' + str(self.idserror[i]) + ' / id = ' + str(self.idserror[i].get_attribute('id')))
                        else:
                            print(str(i+1) + ') ' + str(self.idserror[i]) + ' / id_or_name NOT_EXIST')
                    except:
                        print(str(i+1) + ') ' + str(self.idserror[i]))
        else:
            print('NO ElementID EXIST for -- > ' + self.attribute + ' = ' + self.valuetofind1)

    def output_find_linktext(self):
        self.setUp_webdriver(self.browser)
        ids = self.get_driver_ids_attb()
        self.find_linktext(ids)
        self.driver.quit()

####### SCRIPT TO GET INPUT & PUT TO SCRIPT  ######
print()
base_url = input('Put URL = ')
# base_url = 'mengkome.pythonanywhere.com'
if base_url.split('://')[0] == base_url and base_url is not None:
    base_url = 'https://' + base_url
print('URL = ' + base_url)
partorfull = input('Partial_Link_Text / Link_Text / All? = ')

test1 = FindLinkText('chrome', partorfull, base_url)
test1.output_find_linktext()