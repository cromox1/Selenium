__author__ = 'cromox'

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
# import time

class GooglePlayPage(BasePage):

    # masani = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _avatar_field = '//*[@id="gb"]/div[1]/div[1]/div[2]/div[4]/div[1]/a/span'
    _avatar_field_type = 'xpath'
    _emailid_field = '//*[@id="gb"]/div[1]/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[2]'
    _emailid_field_type = 'xpath'
    _music_field = '//*[@id="wrapper"]/div[1]/div/ul/li[4]/a/span/span[1]/span'
    _music_field_type = 'xpath'
    _search_field = '//*[@id="gbqfq"]'
    _search_field_type = 'xpath'
    _search_button = '//*[@id="gbqfb"]/span'
    _search_button_type = 'xpath'

    def gotogoogleplay(self):
        googlePlayURL = "https://play.google.com"
        print("Google Play URL = " + googlePlayURL)
        self.driver.get(googlePlayURL)

    def getLoginUserEmail(self):
        return self.verifyUserEmailId(self._avatar_field, self._avatar_field_type, self._emailid_field, self._emailid_field_type)

    def getGmailUserStatus(self):
        return self.verifyGmailUserStillLogin(self._avatar_field, self._avatar_field_type)

    def myPlayXtvt(self, driver):
        print("TEST1")
        pass

    def verifyFreeItems(self, itemsURL, textsearch):
        self.driver.get(itemsURL)
        self.elementClick(self._search_field, self._search_field_type)
        self.sendKeys(textsearch, self._search_field, self._search_field_type)
        self.elementClick(self._search_button, self._search_button_type)
