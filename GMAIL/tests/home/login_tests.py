__author__ = 'cromox'

from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import datetime, time
from tests.conftest import userPasswordRead

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    masani = datetime.datetime.now().strftime("%Y%m%d")

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.tstatus = tStatus(self.driver)
        self.loginpage = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.log.info("test_invalidLogin started")
        ### test invalid accounts
        if self.loginpage.getGmailUserStatus() == False:
            self.loginpage.loginGmailUser("akula12345@emailcubaan.com", "abcabcabc123")
        result = self.loginpage.verifyNotLogin()
        self.tstatus.mark(result, "Not Login email1 Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        if self.loginpage.getGmailUserStatus() == False:
            self.loginpage.loginGmailUser("test123cubaan@gmail.com", "qwerty456")
        result = self.loginpage.verifyNotLogin()
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("Test invalidLogin was successful", result, "Not Login email2 Verified")

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.log.info("test_validLogin started")
        usrpswd = userPasswordRead("USRPSWD#", self.masani)
        self.adminuser = usrpswd.replace(' ','').split(',')[0]
        self.adminpswd = usrpswd.replace(' ','').split(',')[1]
        if self.loginpage.getGmailUserStatus() == False:
            self.loginpage.loginGmailUser(self.adminuser, self.adminpswd)
        result = self.loginpage.verifyLoginTitle()
        self.tstatus.mark(result, "Login " + str(self.adminuser) + " Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.loginpage.verifyPageURL("https://myaccount.google.com/?pli=1")
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("Test validLogin was successful", result, "Login URL verified")

    @pytest.mark.run(order=3)
    def test_xcheckGmail(self):
        self.log.info("test_xcheckGmail started")
        usrpswd = userPasswordRead("USRPSWD#", self.masani)
        self.adminuser = usrpswd.replace(' ','').split(',')[0]
        self.adminpswd = usrpswd.replace(' ','').split(',')[1]
        if self.loginpage.getGmailUserStatus() == False:
            self.loginpage.loginGmailUser(self.adminuser, self.adminpswd)
        self.loginpage.gotoGmailBox()
        time.sleep(5)
        result = self.loginpage.verifyPageURLlow('https://mail.google.com')
        self.tstatus.mark(result, "Gmail URL verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.loginpage.isElementPresent("//div[@class='T-I J-J5-Ji T-I-KE L3']", "xpath")
        self.tstatus.mark(result, "Compose button verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.loginpage.verifyPageText("//div[@id=':i']//span[contains(text(),'Gmail')]", "xpath", "Gmail")
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("Test test_xcheckGmail was successful", result, "Gmail button OK")

#ff = LoginTests()
#ff.test_validLogin()
