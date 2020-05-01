__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
# from requests import get as urlget
# from PyPDF2 import PdfFileReader as PDFread
from os import remove as removefile

class TestOne(unittest.TestCase):
    def setUp(self):
        chromedriverpath = r'C:\tools\python3\Scripts\chromedriver.exe'
        self.driver = webdriver.Chrome(chromedriverpath)
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.co.uk"
        self.verificationErrors = []
        # self.tmpfilename = 'tmptest123.pdf'

        ### GET python version & Browser version
        from sys import version as pythonversion
        print()
        print('Python Version = ' + pythonversion)
        print('Browser version ( ' + self.driver.name + ' ) = ' + self.driver.capabilities['browserVersion'])
        print()

    def test_one(self):
        driver = self.driver
        if driver.name == 'chrome':
            driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_name('q').click()
        driver.find_element_by_name('q').send_keys("github cromox1" + Keys.ENTER)
        # 'cromox1 (Rosli Talib) · GitHub'
        cromox1_google_url =  driver.find_elements_by_xpath("//*[contains(text(), 'cromox1 (Rosli Talib) · GitHub')]")
        # cromox1_google_url = driver.find_elements_by_xpath("//*[contains(text(), 'cromox1 (Rosli Talib)')]")
        print('Elements GITHUB LINK = ' + str(cromox1_google_url))
        # count1 = driver.find_element_by_xpath("//*[contains(text(), 'cromox1 (Rosli Talib) · GitHub')]").Count
        # count1 = cromox1_google_url
        count1 = len([x for x in cromox1_google_url])
        print('Number GITHUB LINK = ' + str(count1))
        if count1 == 1:
            cromox1_google_url[0].click()

        githubcromox1url = driver.current_url
        print('CURRENT URL = ' + str(githubcromox1url))


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        # try:
        #     removefile(self.tmpfilename)
        #     # print('  Successfully remove tmp file ' + str(self.tmpfilename))
        # except WindowsError as exx:
        #     print('  Error = ' + str(exx) + ' / file = ' + str(self.tmpfilename))

if __name__ == "__main__":
    unittest.main()
