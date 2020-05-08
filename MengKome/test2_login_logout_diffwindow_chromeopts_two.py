__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import unittest

class TestMengkome1(unittest.TestCase):
    mengkome_url = None
    chromedatadir = "chrome-data"
    userone = 'bacaone'
    pswdone = 'qawsed123456'

    def setUp(self):
        self.base_url = "https://mengkome.pythonanywhere.com/admin/login/"
        self.chromedriverpath = r'C:\Users\taverner\Documents\chromedriver\chromedriver.exe'
        # self.driver = webdriver.Chrome(self.chromedriverpath)
        print('\n--- >> SETUP')

    def test_one_login(self):
        print('\n---->  ' + str(self._testMethodName) + '\n')
        # GET python version & Browser version
        driver = webdriver.Chrome(self.chromedriverpath)
        from sys import version as pythonversion
        print('Python Version = ' + pythonversion)
        print('Browser version ( ' + driver.name + ' ) = ' + driver.capabilities['browserVersion'])
        print()

        chrome_options = Options()
        # chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--user-data-dir=" + self.__class__.chromedatadir)
        driver = webdriver.Chrome(self.chromedriverpath, options=chrome_options)
        chrome_options.add_argument("user-data-dir=" + self.__class__.chromedatadir)
        print("CHROME_OPTIONS = " + str(chrome_options.arguments))
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
        # sleep(5)

        ## current URL
        print('CURRENT URL = ' + driver.current_url)
        self.__class__.mengkome_url = driver.current_url
        driver.close()
        # driver.quit()

    def test_two_relogin_chkinfos(self):
        sleep(5)
        print('\n---->  ' + str(self._testMethodName) + '\n')
        user1 = self.__class__.userone
        urlone = self.__class__.mengkome_url

        chrome_options = Options()
        # chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--user-data-dir=" + self.__class__.chromedatadir)
        driver = webdriver.Chrome(self.chromedriverpath, options=chrome_options)

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
        # driver.close()
        # sleep(5)
        driver.quit()

    def test_x_relogin_then_logout(self):
        sleep(10)
        print('\n---->  ' + str(self._testMethodName) + '\n')
        urlone = self.__class__.mengkome_url

        chrome_options = Options()
        # chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--user-data-dir=" + self.__class__.chromedatadir)
        driver = webdriver.Chrome(self.chromedriverpath, options=chrome_options)

        driver.get(urlone)
        driver.find_element_by_xpath("//*[contains(text(), 'Log out')]").click()
        if driver.find_element_by_xpath("//*[@id='content']/h1").text == 'Logged out':
            print('User ' + self.__class__.userone + ' successfully LOGGED OUT')
        # driver.close()
        driver.quit()

    def tearDown(self):
        # driver.quit()
        print('\n--- >> TEARDOWN')
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()