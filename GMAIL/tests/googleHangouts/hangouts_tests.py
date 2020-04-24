__author__ = 'cromox'

from pages.googleHangouts.hangouts_page import HangOutsPage
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import datetime
# import time
from tests.conftest import userPasswordRead

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class HangOutsTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    masani = datetime.datetime.now().strftime("%Y%m%d")

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.tstatus = tStatus(self.driver)
        self.hangouts = HangOutsPage(self.driver)
        usrpswd = userPasswordRead("USRPSWD#", self.masani)
        self.adminuser = usrpswd.replace(' ','').split(',')[0]
        self.adminpswd = usrpswd.replace(' ','').split(',')[1]
        if self.hangouts.getGmailUserStatus() == False:
            self.hangouts.loginGmailUser(self.adminuser, self.adminpswd)

    @pytest.mark.run(order=1)
    def test_gotoHangOutsBase(self):
        self.log.info("test_gotoHangOutsBase started 1")
        self.hangouts.gotoHangOuts()
        result = self.hangouts.verifyPageTitle('Google Hangouts')
        self.tstatus.mark(result, "Title Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.hangouts.verifyPageURLlow('https://hangouts.google.com')
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("test_gotoHangOutsBase OK", result, "URL Verified")

    @pytest.mark.run(order=2)
    def test_xcheckMainHangOutsBars(self):
        self.log.info("test_xcheckMainHangOutsBars started 1")
        if self.hangouts.verifyPageURLlow('https://hangouts.google.com') == False:
            self.hangouts.gotoHangOuts()
        # //*[@id="yDmH0d"]/div[4]/div[1]/div[1]/content/span
        result = self.hangouts.isElementPresent('//*[@id="yDmH0d"]/*[4]/*[1]', 'xpath')
        self.tstatus.mark(result, "Main Bar Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.hangouts.verifyPageText('//div[@class="g-Ue-zr-ma"]', 'xpath', 'Get started by calling or messaging a friend below.')
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("test_checkMainHangOutsBars OK", result, "Title Text Verified")
