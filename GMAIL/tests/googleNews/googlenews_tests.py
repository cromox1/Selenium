__author__ = 'cromox'

from pages.googleNews.googlenews_page import NewsPage
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import datetime
# import time
from tests.conftest import userPasswordRead

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class NewsTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    masani = datetime.datetime.now().strftime("%Y%m%d")

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.tstatus = tStatus(self.driver)
        self.newspage = NewsPage(self.driver)
        usrpswd = userPasswordRead("USRPSWD#", self.masani)
        self.adminuser = usrpswd.replace(' ','').split(',')[0]
        self.adminpswd = usrpswd.replace(' ','').split(',')[1]
        if self.newspage.getGmailUserStatus() == False:
            self.newspage.loginGmailUser(self.adminuser, self.adminpswd)
        self.main_tab = self.driver.current_window_handle

    @pytest.mark.run(order=1)
    def test_gotoNewsBase(self):
        self.log.info("test_gotoNewsBase started 1")
        self.newspage.gotoGoogleNews()   ## GoogleNews will open new tab of the browser
        self.driver.switch_to_window(self.driver.window_handles[1])
        result = self.newspage.verifyPageTitle('Google News')
        self.tstatus.mark(result, "Title Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.newspage.verifyPageURLlow('https://news.google.com')
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("test_gotoNewsBase OK", result, "URL Verified")
        self.driver.close()
        self.driver.switch_to_window(self.main_tab)

    @pytest.mark.run(order=2)
    def test_xcheckMainNewsBars(self):
        self.log.info("test_xcheckMainNewsBars started 2")
        if self.newspage.verifyPageURLlow('https://news.google.com') == False:
            self.newspage.gotoGoogleNews()
            self.driver.switch_to_window(self.driver.window_handles[1])
        result = self.newspage.isElementPresent("//*[contains(text(),'Top stories')]", 'xpath')
        self.tstatus.mark(result, "Main Bar 1 Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.newspage.isElementPresent("//*[@class='ICsaqd'][contains(text(),'United Kingdom')]", 'xpath')
        self.tstatus.mark(result, "Main Bar 2 Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.newspage.isElementPresent("//*[contains(text(),'Send feedback')]", 'xpath')
        self.tstatus.mark(result, "Main Bar 3 Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.newspage.verifyPageText('//*[@id="yDmH0d"]/*/*/*[1]/*/*/*/*[1]/*[1]/*[1]/h3/a', 'xpath', 'Headlines')
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("test_xcheckMainNewsBars OK", result, "Title Text Verified")
        self.driver.close()
        self.driver.switch_to_window(self.main_tab)
