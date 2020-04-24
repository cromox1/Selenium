__author__ = 'cromox'

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time

class NewsPage(BasePage):

    # masani = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _avatar_field = "//span[@class='gb_db gbii']"
    _avatar_field_type = 'xpath'
    _emailid_field = "//div[@class='gb_Ib']"
    _emailid_field_type = 'xpath'
    _google_apps = '//*[@id="gbwa"]/*/*/*/*'  # '//*[@id="gbwa"]/div/a/svg/path'        //*[@id="gbwa"]/div[1]/a
    _google_apps_type = 'xpath'
    _google_news = '//*/span[contains(text(),"News")]' # '//*[@id="gb300"]/span[contains(text(),"Hangouts")]'
    _google_news_type = 'xpath'

    def gotoGoogleNews(self):
        ## GoogleNews will open new tab of the browser
        self.elementClick(self._google_apps, self._google_apps_type)
        time.sleep(1)
        self.elementClick(self._google_news, self._google_news_type)
        time.sleep(5)
        ## Note -
        # Open link(of URL) in new tab
        # link.send_keys(Keys.CONTROL + Keys.SHIFT + Keys.RETURN)

    def getGmailUserStatus(self):
        return self.verifyGmailUserStillLogin(self._avatar_field, self._avatar_field_type)
