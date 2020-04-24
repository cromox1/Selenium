__author__ = 'cromox'

from pages.youtube.youtube_page import YoutubePage
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import datetime
from tests.conftest import userPasswordRead

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class YoutubeTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    masani = datetime.datetime.now().strftime("%Y%m%d")

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.tstatus = tStatus(self.driver)
        self.youtube = YoutubePage(self.driver)
        usrpswd = userPasswordRead("USRPSWD#", self.masani)
        self.adminuser = usrpswd.replace(' ','').split(',')[0]
        self.adminpswd = usrpswd.replace(' ','').split(',')[1]
        if self.youtube.getGmailUserStatus() == False:
            self.youtube.loginGmailUser(self.adminuser, self.adminpswd)

    @pytest.mark.run(order=1)
    def test_gotoYoutubeRushdi(self):
        self.log.info("test_gotoYoutubeRushdi started")
        self.viewingyoutube("aUX2nzVo0uM", 'The Land of Gibbery - YouTube')
        self.viewingyoutube("-tNXUFiKA_Y", 'Bersih 4.0 & Iklan Merdeka 2015 (Wrecking Ball Parody) - YouTube')
        self.viewingyoutube("2jxsXJF14vQ", 'FOOTBALL CHALLENGES (with Messi) - YouTube')

    @pytest.mark.run(order=2)
    def test_userloginEmailId(self):
        self.log.info("test_userloginEmailId started")
        useremailgot = self.youtube.getLoginUserEmail()
        if useremailgot == self.adminuser:
            result = True
        else:
            result = False
        self.tstatus.mark(result, "Email id Verified = " + str(useremailgot))
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))

        self.driver.get('https://myaccount.google.com/email')
        result = self.youtube.verifyPageTitle('Email')
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("test_userloginEmailId", result, "Email page Verified")

    ## function for viewing youtube for pytest
    def viewingyoutube(self, youtubeid, youtubetitle):
        self.youtube.gotoyoutube(youtubeid)
        youtubevideoinfo = self.youtube.youtubevideo(self.driver)
        result = self.youtube.verifyPageTitle(youtubetitle)
        self.tstatus.mark(result, "Title Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        if int(youtubevideoinfo[1]) > 1:
            result = True
        else:
            result = False
        self.tstatus.mark(result, "Number of Views Verified = " + youtubevideoinfo[1])
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        if int(youtubevideoinfo[2]) > 1:
            result = True
        else:
            result = False
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("test_gotoYoutubeRushdi", result, "Number of Likes Verified = " + youtubevideoinfo[2])
