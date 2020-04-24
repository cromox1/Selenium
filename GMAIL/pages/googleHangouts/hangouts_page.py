__author__ = 'cromox'

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time

class HangOutsPage(BasePage):

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
    _google_apps = '//*[@id="gbwa"]/*/*/*/*'  # '//*[@id="gbwa"]/div/a/svg/path'        //*[@id="gbwa"]/div[1]/a
    _google_apps_type = 'xpath'
    _apps_more = '//*[contains(text(),"More")]' # "//a[@class='gb_ja gb_3f']"
    _apps_more_type = 'xpath'
    _hangouts = '//*/span[contains(text(),"Hangouts")]' # '//*[@id="gb300"]/span[contains(text(),"Hangouts")]'
    _hangouts_type = 'xpath'


    def gotoHangOuts(self):
        self.elementClick(self._google_apps, self._google_apps_type)
        time.sleep(1)
        self.elementClick(self._apps_more, self._apps_more_type)
        time.sleep(1)
        self.elementClick(self._hangouts, self._hangouts_type)
        time.sleep(1)

    def getGmailUserStatus(self):
        return self.verifyGmailUserStillLogin(self._avatar_field, self._avatar_field_type)