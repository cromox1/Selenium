__author__ = 'cromox'

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from selenium.webdriver.common.keys import Keys
# import datetime

class P01SearchGitHubCromox1(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators Google
    # _search_area = "//*[@title='Search']"
    # _search_area_type = 'xpath'
    _search_area = 'q'
    _search_area_type = 'name'
    _search_data = "github cromox1"

    # Google page
    def gotoSearchArea(self):
        self.elementClick(self._search_area, locatorType=self._search_area_type)

    def searchGitHubCromox1(self):
        self.sendKeys(self._search_data, self._search_area, locatorType=self._search_area_type)
        self.sendKeys(Keys.ENTER, self._search_area, locatorType=self._search_area_type)

    def gotoGitHubCromox1(self):
        containtext = "//*[contains(text(),'cromox1 (Rosli Talib) · GitHub')]"
        cromox1_txt = 'cromox1 (Rosli Talib) · GitHub'

        element = self.getElementList(containtext, locatorType='xpath')
        count_cromox1 = len([x for x in element])
        print('Number GITHUB LINK = ' + str(count_cromox1))
        if count_cromox1 >= 1:
            element[0].click()
            cromox1_url = self.returnCurrentURL()
            print('CURRENT URL = ' + self.returnCurrentURL())
        else:
            # cromox1_url = self.base_url
            print('NO cromox1 GITHUB found')

    ## General
    def returnCurrentURL(self):
        return self.driver.current_url

    def gotosite(self, URL):
        return self.driver.get(URL)