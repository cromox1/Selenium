__author__ = 'cromox'

from pages.googleplay.googleplay_page import GooglePlayPage
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import datetime
import time
from tests.conftest import userPasswordRead

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PlayGoogleTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    masani = datetime.datetime.now().strftime("%Y%m%d")

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.tstatus = tStatus(self.driver)
        self.googleplay = GooglePlayPage(self.driver)
        usrpswd = userPasswordRead("USRPSWD#", self.masani)
        self.adminuser = usrpswd.replace(' ','').split(',')[0]
        self.adminpswd = usrpswd.replace(' ','').split(',')[1]
        if self.googleplay.getGmailUserStatus() == False:
            self.googleplay.loginGmailUser(self.adminuser, self.adminpswd)

    @pytest.mark.run(order=1)
    def test_gotoGooglePlayBase(self):
        self.log.info("test_gotoGooglePlay started 1")
        self.googleplay.gotogoogleplay()
        result = self.googleplay.verifyPageTitle('Google Play')
        self.tstatus.mark(result, "Title Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        useremailgot = self.googleplay.getLoginUserEmail()
        if useremailgot == self.adminuser:
            result = True
        else:
            result = False
        print("ResultLast = " + str(result) + '\n')
        self.log.info("User's email ( " + str(useremailgot) + " ) VS Expected email ( " + self.adminuser + " )")
        self.tstatus.markFinal("test_gotoGooglePlayBase OK", result, "Email Verified")

    @pytest.mark.run(order=2)
    def test_musicFree(self):
        self.log.info("test_musicFree started 2")
        self.googleplay.verifyFreeItems('https://play.google.com/store/music', 'free music')
        time.sleep(2)
        result = self.googleplay.verifyPageURL('https://play.google.com/store/search?q=free%20music&c=music')
        self.tstatus.mark(result, "URL Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googleplay.isElementPresent('//*[@id="body-content"]/*[2]/*/*[1]/*/*[1]/*/*[1]', 'xpath')
        self.tstatus.mark(result, "Albums Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googleplay.isElementPresent('//*//*[1]/*[1]/*[2]/*[1]/*[1]/*[1]', 'xpath')
        self.tstatus.mark(result, "Album Cover Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googleplay.verifyPageText('//*[@id="body-content"]/*[2]/*/*[1]/*/*[1]/*/*[2]/*[1]/*/*[3]/*/*/*[2]/*/*', 'xpath', 'Free')
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("test_musicFree OK", result, "Free Musics Verified")

    @pytest.mark.run(order=3)
    def test_moviesFree(self):
        self.log.info("test_moviesFree started 3")
        self.googleplay.verifyFreeItems('https://play.google.com/store/movies', 'free movies')
        time.sleep(2)
        result = self.googleplay.verifyPageURL('https://play.google.com/store/search?q=free%20movies&c=movies')
        self.tstatus.mark(result, "URL Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googleplay.isElementPresent('//*[@id="body-content"]/*[2]/*/*[1]/*/*[1]/*/*[1]', 'xpath')
        self.tstatus.mark(result, "Free Movies Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googleplay.verifyPageText('//*[@id="body-content"]/*/*/*[1]/*/*[1]/*/*[1]/*/*[1]', 'xpath', 'Free Movies')
        self.tstatus.mark(result, "Free Movies text Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googleplay.isElementPresent('//*[@id="body-content"]/*[2]/*/*[1]/*/*[1]/*/*[2]/*[1]/*/*[1]', 'xpath')
        self.tstatus.mark(result, "Movies Cover Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googleplay.verifyPageText('//*[@id="body-content"]/*[2]/*/*[1]/*/*[1]/*/*[2]/*[1]/*/*[3]/*/*/*[2]/*/*', 'xpath', 'Free')
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("test_moviesFree OK", result, "Free Movies Verified")

    @pytest.mark.run(order=4)
    def test_xbooksFree(self):
        self.log.info("test_xbooksFree started 4")
        self.googleplay.verifyFreeItems('https://play.google.com/store/books', 'free books')
        time.sleep(2)
        result = self.googleplay.verifyPageURL('https://play.google.com/store/search?q=free%20books&c=books')
        self.tstatus.mark(result, "URL Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googleplay.verifyPageText('//*[@id="body-content"]/*/*/*[1]/*/*[1]/*/*[2]/*[1]/*/*[3]/*/*/*[2]/*/*', 'xpath', 'Free')
        self.tstatus.mark(result, "Free Ebooks Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googleplay.verifyPageText('//*[@id="body-content"]/*/*/*[1]/*/*[2]/*/*[2]/*[1]/*/*[3]/*/*/*[2]/*/*', 'xpath', 'Free')
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("test_xbooksFree OK", result, "Free Audiobooks Verified")