__author__ = 'cromox'

### NOTE : Browser version ( chrome ) = 63.0.3239.84 / Selenium version = 3.8.0
## IN-PROGRESS 
## TO DO - 
# 1) change into main scripts (or create main scripts and modify this)
# 2) add more unittests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test3yahooXixa01(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://login.yahoo.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_3yahoo_xixa01(self):
        driver = self.driver
        driver.get(self.base_url + "/?.src=ym&.intl=us&.done=https%3A%2F%2Fmg.mail.yahoo.com%2F")
        # driver.find_element_by_id("persistent").click()
        driver.find_element_by_id("login-username").clear()
        driver.find_element_by_id("login-username").send_keys("xixa01")
        driver.find_element_by_id("login-signin").click()
        driver.find_element_by_id("login-passwd").clear()
        driver.find_element_by_id("login-passwd").send_keys("Apasajerlah!")
        driver.find_element_by_id("login-signin").click()
        self.assertEqual("Yahoo - Yahoo Mail", driver.title)
        try: self.assertEqual("Yahoo - Yahoo Mail", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        # driver.get('https://login.yahoo.com/account/logout?logout=1&.direct=2&.src=cdgm&.crumb=fO0CfL55OFQ&.intl=uk&.lang=en-GB&.done=https%3A%2F%2Fuk.yahoo.com%2F')
        driver.get('https://login.yahoo.com/account/logout')
        driver.get('https://login.yahoo.com/account/logout?crumb=AUX5cBCL32I&done=https%3A%2F%2Fwww.yahoo.com&logout=1')
        # driver.find_element_by_id("yucs-signout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
