__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import rmtree as removedir
from time import sleep
import unittest

class TestMengkome1(unittest.TestCase):
    mengkome_url = ''
    chromedatadir = 'chrome-data'
    userone = 'bacaone'
    pswdone = 'qawsed123456'

    def setUp(self):
        self.base_url = "https://mengkome.pythonanywhere.com/admin/login/"
        self.chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        # self.driver = webdriver.Chrome(self.chromedriverpath)
        print('\n--- >> SETUP')

    def test_01_login(self):
        print('\n---->  ' + str(self._testMethodName) + '\n')
        # GET python version & Browser version
        from sys import version as pythonversion
        print('Python Version = ' + pythonversion)
        from selenium import __version__ as seleniumversion
        print('Selenium version = ' + seleniumversion)

        chrome_options = Options()
        # chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--user-data-dir=" + self.__class__.chromedatadir)
        chrome_options.add_argument("user-data-dir=" + self.__class__.chromedatadir)
        # chrome_options.add_argument('--SameSite=None')
        # new one
        experimentalFlags = ['same-site-by-default-cookies@1', 'cookies-without-same-site-must-be-secure@1']
        chromeLocalStatePrefs = {'browser.enabled_labs_experiments': experimentalFlags}
        chrome_options.add_experimental_option('localState', chromeLocalStatePrefs)
        # chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument("--disable-web-security")
        # chrome_options.add_argument("--allow-running-insecure-content")
        # chrome_options.add_argument("--allow-cross-origin-auth-prompt")
        # chrome_options.add_argument("--disable-cookie-encryption")
        driver = webdriver.Chrome(self.chromedriverpath, options=chrome_options)
        try:
            print('Browser version ( ' + driver.name + ' ) = ' + driver.capabilities['version']) # Python 3.7 and below
        except:
            print('Browser version ( ' + driver.name + ' ) = ' + driver.capabilities['browserVersion']) # Python 3.8 & above
        print()

        print("CHROME_OPTIONS = " + str(chrome_options.arguments))
        # print("CHROME_OPTIONS = " + str(driver.desired_capabilities))
        driver.implicitly_wait(10)

        user1 = self.__class__.userone
        pswd1 = self.__class__.pswdone
        if driver.name == 'chrome':
            driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_name('username').click()
        driver.find_element_by_name('username').send_keys(user1 + Keys.ENTER)
        driver.find_element_by_name('password').click()
        driver.find_element_by_name('password').send_keys(pswd1 + Keys.ENTER)

        ## current URL
        print('CURRENT URL = ' + driver.current_url)
        self.__class__.mengkome_url = driver.current_url
        driver.close()
        # driver.quit()

    def test_02_relogin_chkinfos(self):
        # sleep(2)
        print('\n---->  ' + str(self._testMethodName) + '\n')
        user1 = self.__class__.userone
        urlone = self.__class__.mengkome_url

        chrome_options = Options()
        # chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--user-data-dir=" + self.__class__.chromedatadir)
        chrome_options.add_argument('SameSite=None')
        # chrome_options.add_argument('--Secure')
        chrome_options.add_argument("--autocomplete=current-password")
        # new one
        experimentalFlags = ['same-site-by-default-cookies@1', 'cookies-without-same-site-must-be-secure@1']
        chromeLocalStatePrefs = {'browser.enabled_labs_experiments': experimentalFlags}
        chrome_options.add_experimental_option('localState', chromeLocalStatePrefs)
        # now add chrome_options
        driver = webdriver.Chrome(self.chromedriverpath, options=chrome_options)
        # sleep(5)

        # headersx = {'autocomplete' : 'current-password'}
        # driver.get(urlone, headers=headersx)
        driver.get(urlone)
        userpage1 = driver.find_element_by_xpath('//*[@id="user-tools"]/strong').text
        print('Name of the user = ' + userpage1)
        driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
        driver.find_element_by_xpath("//*[contains(text(), '" + user1 + "')]").click()
        email1 = driver.find_element_by_xpath('//*[@class="form-row field-email"]/*/*[@class="readonly"]').text
        join1 = driver.find_element_by_xpath('//*[@class="form-row field-date_joined"]/*/*[@class="readonly"]').text
        print('User email = ' + email1)
        print('User Joined date = ' + join1)
        print('CURRENT URL = ' + driver.current_url)
        self.__class__.mengkome_url = driver.current_url
        driver.close()
        # driver.quit()

    # def test_99_relogin_then_logout(self):
    #     sleep(2)
    #     print('\n---->  ' + str(self._testMethodName) + '\n')
    #     urlone = self.__class__.mengkome_url
    #
    #     chrome_options = Options()
    #     # chrome_options.add_argument("--no-sandbox")
    #     chrome_options.add_argument("--user-data-dir=" + self.__class__.chromedatadir)
    #     driver = webdriver.Chrome(self.chromedriverpath, options=chrome_options)
    #     # sleep(5)
    #
    #     driver.get(urlone)
    #     driver.find_element_by_xpath("//*[contains(text(), 'Log out')]").click()
    #     if driver.find_element_by_xpath("//*[@id='content']/h1").text == 'Logged out':
    #         print('User ' + self.__class__.userone + ' successfully LOGGED OUT')
    #         print('CURRENT URL = ' + driver.current_url)
    #     driver.close()
        # driver.quit()

    def tearDown(self):
        # driver.quit()
        print('--- >> TEARDOWN')
        # self.assertEqual([], self.verificationErrors)

    # @classmethod
    # def tearDownClass(self):
    #     print('\n---->  tearDownClass -- ')
    #     try:
    #         # sleep(5)
    #         print(type(self.__class__.chromedatadir))
    #         removedir(str(self.__class__.chromedatadir))
    #         print('  Successfully remove tmp file ' + str(self.__class__.chromedatadir))
    #     except Exception as exx:  # except WindowsError as exx:
    #         print('Failed to delete %s' % (str(self.__class__.chromedatadir)))
    #         print('==  Error = ' + str(exx))

if __name__ == "__main__":
    unittest.main()