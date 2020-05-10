__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class TestGitHub(unittest.TestCase):
    cromox_url = ''

    def setUp(self):
        chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        self.driver = webdriver.Chrome(chromedriverpath)
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.co.uk"
        self.verificationErrors = []

    def test_one(self):
        print('\n---->  ' + str(self._testMethodName) + '\n')
        # GET python version & Browser version
        driver = self.driver
        from sys import version as pythonversion
        print('Python Version = ' + pythonversion)
        try:
            print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['version']) # Python 3.7 and below
        except:
            print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['browserVersion']) # Python 3.8 & above
        print()

        if driver.name == 'chrome':
            driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_name('q').click()
        driver.find_element_by_name('q').send_keys("github cromox1" + Keys.ENTER)
        # 'cromox1 (Rosli Talib) · GitHub'
        list_cromox1 = driver.find_elements_by_xpath("//*[contains(text(), 'cromox1 (Rosli Talib) · GitHub')]")
        count_cromox1 = len([x for x in list_cromox1])
        self.assertGreaterEqual(count_cromox1, 1)
        print('Number GITHUB LINK = ' + str(count_cromox1))
        if count_cromox1 >= 1:
            list_cromox1[0].click()
            cromox1_url = driver.current_url
            print('CURRENT URL = ' + driver.current_url)
        else:
            cromox1_url = self.base_url
            print('NO cromox1 GITHUB found')
        # TestGitHub.cromox_url = cromox1_url
        self.__class__.cromox_url = cromox1_url

    def test_two(self):
        print('\n---->  ' + str(self._testMethodName) + '\n')
        driver = self.driver
        # cromox1_url = TestGitHub.cromox_url -- # TestGitHub (className) vs self.__class__ #
        cromox1_url = self.__class__.cromox_url
        print('CROMOX1_URL = ' + cromox1_url)
        driver.get(cromox1_url + '?tab=repositories')
        print('CURRENT URL = ' + driver.current_url)
        list_repo1 = driver.find_elements_by_class_name('wb-break-all')
        print('NUMBER OF REPO = ' + str(len(list_repo1)))
        i = 1
        for element in list_repo1:
            print(str(i) + ') ' + element.text)
            i = i+1
        self.assertEqual(i - 1, len(list_repo1))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
