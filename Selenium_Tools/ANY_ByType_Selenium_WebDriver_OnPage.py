__author__ = 'cromox'
'''
Find existing ID/Name/Tag_Name/Class/LinkText/etc using specific Selenium element search.
Example:

$ python3 ANY_ByType_Selenium_WebDriver_OnPage.py

Put URL = www.facebook.com
URL = https://www.facebook.com
id / xpath / name / tagname / classname / linktext / css_selector = tagname

Python Version = 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)]
Browser version ( chrome ) = 71.0.3578.98

Value for 'tag_name' to execute = label

List of ElementID for -- > tag_name = label :
1) 0.8333807069740009-1
2) 0.8333807069740009-2
3) 0.8333807069740009-3 / id = loginbutton
4) 0.8333807069740009-4
5) 0.8333807069740009-5

$
(This is using Basic OOP (Object-Oriented Programming))
'''
from selenium import webdriver
import sys

class CheckAnyByType():
    def __init__(self, browser, base_url, attribute):
        self.browser = browser
        self.base_url = base_url
        self.attribute = attribute

    def setUp_webdriver(self, browser='chrome'):
        ## Chrome - add_argument='headless' , Firefox - add_argument="--headless"
        if browser == 'chrome' or browser == 'ch' or browser == 'google':
            from selenium.webdriver.chrome.options import Options
            myoption = Options()
            # myoption.add_argument('headless')
            myoption.set_headless(headless=True)
            myoption.add_argument("--proxy-server='direct://'")
            myoption.add_argument("--proxy-bypass-list=*")
            self.driver = webdriver.Chrome(options=myoption)
        elif browser == 'firefox' or browser == "ff":
            from selenium.webdriver.firefox.options import Options
            myoption = Options()
            myoption.add_argument('--headless')
            myoption.add_argument("--proxy-server='direct://'")
            myoption.add_argument("--proxy-bypass-list=*")
            self.driver = webdriver.Firefox(options=myoption)
        else:
            self.driver = webdriver.Chrome()
            self.driver.quit()
        self.driver.implicitly_wait(2)
        ### GET python version & Browser version
        print()
        print('Python Version = ' + sys.version)
        print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['version'])
        print()
        return self.driver

    def bywhatattribute(self, attribute):
        if attribute == 'id' or attribute == 'i' or attribute[0].lower() == 'i':
            attribute1 = 'id'
        elif attribute == 'xpath' or attribute == 'x' or attribute[0].lower() == 'x':
            attribute1 = 'xpath'
        elif attribute == 'name' or attribute == 'n' or attribute[0].lower() == 'n':
            attribute1 = 'name'
        elif attribute == 'tagname' or attribute == 't' or attribute[0].lower() == 't':
            attribute1 = 'tag_name'
        elif attribute == 'linktext' or attribute == 'l' or attribute[0].lower() == 'l':
            attribute1 = 'link_text'
        elif attribute[0].lower() == 'c':
            if attribute[1].lower() == 's':
                attribute1 = 'css_selector'
            elif attribute[1].lower() == 'l':
                attribute1 = 'class_name'
            else:
                attribute1 = 'no_attribute'
        else:
            attribute1 = 'no_attribute'
        return attribute1

    def bywhatelement(self, driver, attribute, valuetofind):
        if attribute == 'id':
            element1 = driver.find_elements_by_id(valuetofind)
        elif attribute == 'xpath':
            element1 = driver.find_elements_by_xpath(valuetofind)
        elif attribute == 'name':
            element1 = driver.find_elements_by_name(valuetofind)
        elif attribute == 'tag_name':
            element1 = driver.find_elements_by_tag_name(valuetofind)
        elif attribute == 'class_name':
            element1 = driver.find_elements_by_class_name(valuetofind)
        elif attribute == 'link_text':
            element1 = driver.find_elements_by_link_text(valuetofind)
        elif attribute == 'css_selector':
            element1 = driver.find_elements_by_css_selector(valuetofind)
        else:
            element1 = 'no_element'
        return element1

    def test_one(self, attribute, elementid, valuetofind):
        print()
        if len(elementid) >= 1 and elementid is not 'no_element':
            print('List of ElementID for -- > ' + attribute + ' = ' + valuetofind + ' :')
            i = 1
            for ii in elementid:
                try:
                    if attribute != 'name' and ii.get_attribute('name') is not None and ii.get_attribute('name') != '':
                        print(str(i) + ') ' + str(ii._id) + ' / name = ' + str(ii.get_attribute('name')))
                    elif attribute != 'id' and ii.get_attribute('id') is not None and ii.get_attribute('id') != '':
                        print(str(i) + ') ' + str(ii._id) + ' / id = ' + str(ii.get_attribute('id')))
                    elif attribute != 'link_text' and ii.get_attribute('text') is not None and ii.get_attribute('text') != '':
                        print(str(i) + ') ' + str(ii._id) + ' / text = ' + str(ii.get_attribute('text')))
                    elif attribute != 'class_name' and ii.get_attribute('class') is not None and ii.get_attribute('class') != '':
                        print(str(i) + ') ' + str(ii._id) + ' / class = ' + str(ii.get_attribute('class')))
                    elif attribute != 'title' and ii.get_attribute('title') is not None and ii.get_attribute('title') != '':
                        print(str(i) + ') ' + str(ii._id) + ' / title = ' + str(ii.get_attribute('title')))
                    elif attribute != 'tag_name' and ii.get_attribute('tag_name') is not None and ii.get_attribute('tag_name') != '':
                        print(str(i) + ') ' + str(ii._id) + ' / tag_name = ' + str(ii.get_attribute('tag_name')))
                    elif attribute != 'text' and ii.get_attribute('text') is not None and ii.get_attribute('text') != '':
                        print(str(i) + ') ' + str(ii._id) + ' / text = ' + str(ii.get_attribute('text').replace('\n', "\ENTER\ ").replace('  ', ' ').replace('   ', ' ')[:200]))
                    else:
                        print(str(i) + ') ' + str(ii._id) + ' / id_or_name NOT_EXIST')
                    i+=1
                except:
                    print(str(i) + ') ' + str(ii._id) + ' / ERROR (element is not attached to the page document)')
                    i+=1
        else:
            print('NO ElementID EXIST for -- > ' + attribute + ' = ' + valuetofind)

    def tearDown(self, driver):
        driver.quit()

    def final_execution(self):
        self.setUp_webdriver(self.browser)
        attribute2 = self.bywhatattribute(self.attribute)
        texttofind = input("Value for '" + attribute2 + "' to execute = ")
        self.driver.get(self.base_url)
        element1 = self.bywhatelement(self.driver, attribute2, texttofind)
        self.test_one(attribute2, element1, texttofind)
        ## END
        self.tearDown(self.driver)

## STARTUP
print()
base_url = input('Put URL = ')
# base_url = 'mengkome.pythonanywhere.com'
if base_url.split('://')[0] == base_url and base_url is not None:
    base_url = 'https://' + base_url
print('URL = ' + base_url)
attribute1 = input('id / xpath / name / tagname / classname / linktext / css_selector = ')

output1 = CheckAnyByType('chrome', base_url, attribute1)
output1.final_execution()