__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import pickle

class TestMengkome1(unittest.TestCase):
    kome_url = None
    userone = 'bacaone'
    pswdone = 'qawsed123456'
    cookiefile = "cookies.pkl"
    wopencookie = open(cookiefile, "wb")
    ropencookie = open(cookiefile, "rb")

    def setUp(self):
        chromedriverpath = r'C:\tools\python3\Scripts\chromedriver.exe'
        self.driver = webdriver.Chrome(chromedriverpath)
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://mengkome.pythonanywhere.com/admin/login/"
        self.verificationErrors = []

    def test_one_login(self):
        print('\n---->  ' + str(self._testMethodName) + '\n')
        # GET python version & Browser version
        driver = self.driver
        from sys import version as pythonversion
        print('Python Version = ' + pythonversion)
        print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['browserVersion'])
        print()

        user1 = self.__class__.userone
        pswd1 = self.__class__.pswdone
        if driver.name == 'chrome':
            driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_name('username').click()
        driver.find_element_by_name('username').send_keys(user1 + Keys.ENTER)
        driver.find_element_by_name('password').click()
        driver.find_element_by_name('password').send_keys(pswd1 + Keys.ENTER)
        pickle.dump(driver.get_cookies(), self.__class__.wopencookie)
        self.__class__.wopencookie.close()
        print('CURRENT URL = ' + driver.current_url)
        self.__class__.kome_url = driver.current_url

    def test_two_chkinfo(self):
        user1 = self.__class__.userone
        urlone = self.__class__.kome_url
        driver = self.driver
        cookies = pickle.load(self.__class__.ropencookie)
        print('COOKIES = ' + str(cookies))
        for cookie in cookies[-1]:
            driver.add_cookie(cookie)
        self.__class__.ropencookie.close()
        driver.get(urlone)
        userpage1 = driver.find_element_by_xpath('//*[@id="user-tools"]/strong').text
        print('Name of the user = ' + userpage1)
        driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
        driver.find_element_by_xpath("//*[contains(text(), '" + user1 + "')]").click()
        email1 = driver.find_element_by_xpath('//*[@class="form-row field-email"]/*/*[@class="readonly"]').text
        join1 = driver.find_element_by_xpath('//*[@class="form-row field-date_joined"]/*/*[@class="readonly"]').text
        print('User email = ' + email1)
        print('User Joined date = ' + join1)

    def test_zxy_logout(self):
        driver = self.driver
        urlone = self.__class__.kome_url
        cookies = pickle.load(self.__class__.ropencookie)
        for cookie in cookies[-1]:
            driver.add_cookie(cookie)
        self.__class__.ropencookie.close()
        driver.get(urlone)
        driver.find_element_by_xpath("//*[contains(text(), 'Home')]").click()
        driver.find_element_by_xpath("//*[contains(text(), 'Log out')]").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()