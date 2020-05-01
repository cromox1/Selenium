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

    ## Locators Google
    _search_area = "//*[@title='Search']"
    _search_area_type = 'xpath'
    _search_data = "github cromox1"

    ## Google page
    def gotoSearchArea(self):
        self.elementClick(self._search_area, locatorType=self._search_area_type)

    def searchGitHubCromox1(self):
        self.sendKeys(self._search_data, self._search_area)
        self.sendKeys(Keys.ENTER, self._search_area)

    def filldataarea(self, data, locator, locatorType='id'):
        self.elementClick(locator, locatorType)
        self.getElement(locator, locatorType).clear()
        self.sendKeys(data, locator, locatorType)

    ## General
    def returnCurrentURL(self):
        return self.driver.current_url

    def gotosite(self, URL):
        return self.driver.get(URL)