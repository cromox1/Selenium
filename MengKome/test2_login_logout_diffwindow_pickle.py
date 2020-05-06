__author__ = 'cromox'

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from os import remove as removefile
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
        print('GET COOKIES = ' + str(driver.get_cookies()))
        sleep(5)
        self.__class__.wopencookie.close()
        print('CURRENT URL = ' + driver.current_url)
        self.__class__.kome_url = driver.current_url

    def test_two_chkinfo(self):
        # self.__class__.ropencookie.close()
        print('\n---->  ' + str(self._testMethodName) + '\n')
        user1 = self.__class__.userone
        urlone = self.__class__.kome_url
        driver = self.driver
        driver.get(urlone)
        cookies = pickle.load(self.__class__.ropencookie)
        # print('COOKIES2 = ' + str(cookies))
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie['expiry'] = int(cookie['expiry'])
            # print(cookie)
            driver.add_cookie(cookie)
        # print(cookies[-1])
        # driver.add_cookie(cookies[-1])
        self.__class__.ropencookie.close()
        print('GET COOKIES T2 = ' + str(driver.get_cookies()))
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
        # self.__class__.ropencookie.close()
        print('\n---->  ' + str(self._testMethodName) + '\n')
        driver = self.driver
        urlone = self.__class__.kome_url
        driver.get(urlone)
        cookies = pickle.load(self.__class__.ropencookie)
        print('COOKIESZXY = ' + str(cookies))
        for cookie in cookies:
            if 'expiry' in cookie:
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)
        print('GET COOKIES ZXY = ' + str(driver.get_cookies()))
        driver.get(urlone)
        driver.find_element_by_xpath("//*[contains(text(), 'Home')]").click()
        driver.find_element_by_xpath("//*[contains(text(), 'Log out')]").click()
        self.__class__.ropencookie.close()

    def tearDown(self):
        self.driver.quit()
        # self.assertEqual([], self.verificationErrors)
        # try:
        #     removefile(self.__class__.cookiefile)
        #     # print('  Successfully remove tmp file ' + str(self.__class__.cookiefile))
        # except WindowsError as exx:
        #     print('  Error = ' + str(exx) + ' / file = ' + str(self.__class__.cookiefile))

if __name__ == "__main__":
    unittest.main()