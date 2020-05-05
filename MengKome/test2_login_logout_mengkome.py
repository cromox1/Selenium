__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class TestMengkome1(unittest.TestCase):
    kome_url = None

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

        user1 = 'bacaone'
        pswd1 = 'qawsed123456'
        if driver.name == 'chrome':
            driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_name('username').click()
        driver.find_element_by_name('username').send_keys(user1 + Keys.ENTER)
        driver.find_element_by_name('password').click()
        driver.find_element_by_name('password').send_keys(pswd1 + Keys.ENTER)
        print('CURRENT URL = ' + driver.current_url)
        # this from test_two and test_zxy_logout
        userpage1 = driver.find_element_by_xpath('//*[@id="user-tools"]/strong').text
        print('Name of the user = ' + userpage1)
        # driver.find_element_by_class_name('model-user').click()
        driver.find_element_by_xpath("//*[contains(text(), 'Users')]").click()
        driver.find_element_by_xpath("//*[contains(text(), '" + user1 + "')]").click()
        # join1 = driver.find_element_by_xpath("//*[contains(text(), 'Date joined:')]").text
        # email1 = driver.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[2]/div[3]/div/div').text
        # join1 = driver.find_element_by_xpath('//*[@id="user_form"]/div/fieldset[4]/div[2]/div/div').text
        email1 = driver.find_element_by_xpath('//*[@class="form-row field-email"]/*/*[@class="readonly"]').text
        join1 = driver.find_element_by_xpath('//*[@class="form-row field-date_joined"]/*/*[@class="readonly"]').text
        print('User email = ' + email1)
        print('User Joined date = ' + join1)
        # i = 1
        # for element in join1:
        #     print(str(i) + ') ' + element.text)
        #     i = i + 1

        driver.find_element_by_xpath("//*[contains(text(), 'Home')]").click()
        driver.find_element_by_xpath("//*[contains(text(), 'Log out')]").click()

        ############# TUNGGU DULU... SKRG GUNA ONE BIG TEST
    #     self.__class__.kome_url =  driver.current_url
    #
    # def test_two_checkinfo(self):
    #     driver = self.driver
    #     driver.get(self.__class__.kome_url)
    #     print('CURRENT URL = ' + driver.current_url)
    #     user1 = driver.find_element_by_xpath('//*[@id="user-tools"]/strong').text
    #     print('Name of the user = ' + user1)
    #
    # def test_zxy_logout(self):
    #     driver = self.driver
    #     driver.get(self.__class__.kome_url)
    #     driver.find_element_by_link_text('Log out').click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()