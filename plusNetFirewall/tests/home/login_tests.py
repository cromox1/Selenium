__author__ = 'cromox'

from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import datetime #, time
from tests.conftest import userPasswordRead

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    masani = datetime.datetime.now().strftime("%Y%m%d")

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.tstatus = tStatus(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.plusNet()
        self.adminpswd = userPasswordRead("ADMINPSWD#", self.masani).replace(' ','').split(',')[0]
        result = self.loginpage.verifyPageURL("http://192.168.1.254/")  # Test 1
        self.tstatus.mark(result, "PlusNet Page URL verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.loginpage.verifyPageTitle('Home')     # Test 2
        self.tstatus.mark(result, "PlusNet Page's Title verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))

    @pytest.mark.run(order=1)
    def test_FirewallSettingBlock(self):
        self.log.info("test_FirewallSettingBlock started")
        self.loginpage.loginAdvSetting(self.adminpswd)    # GO TO Advanced Setting
        result = self.loginpage.verifyPageTitle('advanced dns') # Test 3
        self.tstatus.mark(result, "Advanced Page's Title verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.loginpage.firewallBlockAll()      # Test 4
        self.tstatus.mark(result, "Firewall URL verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.loginpage.verifyPageURL("http://192.168.1.254/advanced_firewall.html") # Test 5
        self.tstatus.mark(result, "URL verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.loginpage.verifyPageTitle('advanced firewall')    # Test 6
        self.tstatus.mark(result, "Page Title verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.loginpage.verifyFirewallIsBlockAll()       # Test 7
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("test_FirewallSettingBlock was successful", result, "Firewall Off button is selected")

    @pytest.mark.run(order=2)
    def test_FirewallSettingOff(self):
        self.log.info("test_FirewallSettingOff started")
        self.loginpage.loginAdvSetting(self.adminpswd)    # GO TO Advanced Setting
        result = self.loginpage.verifyPageTitle('advanced dns') # Test 3
        self.tstatus.mark(result, "Advanced Page's Title verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.loginpage.firewallAllowAll()      # Test 4
        self.tstatus.mark(result, "Firewall URL verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.loginpage.verifyPageURL("http://192.168.1.254/advanced_firewall.html") # Test 5
        self.tstatus.mark(result, "URL verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.loginpage.verifyPageTitle('advanced firewall')    # Test 6
        self.tstatus.mark(result, "Page Title verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.loginpage.verifyFirewallIsOff()       # Test 7
        print("ResultLast = " + str(result) + '\n')
        self.tstatus.markFinal("test_FirewallSettingOff was successful", result, "Firewall Off button is selected")

#ff = LoginTests()
#ff.test_FirewallSettingOff()
