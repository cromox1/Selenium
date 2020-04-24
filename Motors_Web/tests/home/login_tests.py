__author__ = 'cromox'

from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import datetime, time
import sys
# from tests.conftest import userPasswordRead

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)
    masani = datetime.datetime.now().strftime("%Y%m%d")

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        #self.display = Display(visible=0, size=(1600, 1200))
        #self.display.start()
        self.tstatus = tStatus(self.driver)
        self.loginpage = LoginPage(self.driver)
        # self.adminpswd = userPasswordRead("ADMINPSWD#", self.masani).replace(' ','').split(',')[0]

    @pytest.mark.run(order=1)
    def test1Main_NoLogin_InvalidPost(self):
        mytestname = str(sys._getframe().f_code.co_name)
        self.log.info(mytestname + ' start')
        self.loginpage.gotoMotorsMainSite('XX3 7ZZ')
        time.sleep(3)
        print('PASSED ' + mytestname)

    @pytest.mark.run(order=2)
    def test2Main_NoLogin_ValidPost_XMake_XModel_XMin_XMax(self):
        mytestname = str(sys._getframe().f_code.co_name)
        self.log.info(mytestname + ' start')
        self.loginpage.gotoMotorsMainSite('OX3 0LF')
        time.sleep(3)
        result = self.loginpage.verifyPageTitle('Motors.co.uk makes searching for a used car simple!') # Test 1
        self.tstatus.recordStatus(result, "Page's Title verified")
        result = self.loginpage.verifyPageURLlow('https://www.motors.co.uk')# Test 2
        self.tstatus.recordStatus(result, "Page's URL base verified")
        result = self.loginpage.verifyPageURL('https://www.motors.co.uk/search/car/')# Test 3
        self.tstatus.recordStatus(result, "Page's URL exact verified", True, mytestname + ' was successful')
        # result = self.loginpage.verifyLocatorValueText("//h2[contains(text(),'Smart Picks For You')]", 'xpath', 'Smart Picks For You')       # Test Last / # Test 6
        # self.tstatus.recordStatus(result, "Search button is verified", True, mytestname + ' was successful')
        ## 'Search' grey-out
        ## Postcode area give message - Please enter a valid UK postcode <-- postcode is UK one
        ### MakeAny --> ModelAny grey-out
        ### Make - X --> Model

        # time.sleep(3)

    @pytest.mark.run(order=3)
    def test3Main_NoLogin_ValidPost_XMake_XModel_XMin_XMax(self):
        mytestname = str(sys._getframe().f_code.co_name)
        self.log.info(mytestname + ' start')
        self.loginpage.gotoMotorsMainSite('OX3 0LF')
        time.sleep(3)
        print('PASSED ' + mytestname)

    @pytest.mark.run(order=4)
    def test4Main_NoLogin_ValidPost_Make_XModel_XMin_Max(self):
        mytestname = str(sys._getframe().f_code.co_name)
        self.log.info(mytestname + ' start')
        self.loginpage.gotoMotorsMainSite('OX3 0LF')
        time.sleep(3)
        print('PASSED ' + mytestname)

    @pytest.mark.run(order=5)
    def test5Main_NoLogin_ValidPost_Make_Model_Min_XMax(self):
        mytestname = str(sys._getframe().f_code.co_name)
        self.log.info(mytestname + ' start')
        self.loginpage.gotoMotorsMainSite('OX3 0LF')
        time.sleep(3)
        print('PASSED ' + mytestname)

    @pytest.mark.run(order=6)
    def test6Main_NoLogin_ValidPost_Make_Model_XMin_XMax(self):
        mytestname = str(sys._getframe().f_code.co_name)
        self.log.info(mytestname + ' start')
        self.loginpage.gotoMotorsMainSite('OX3 0LF')
        time.sleep(3)
        print('PASSED ' + mytestname)

#ff = LoginTests()
#ff.test_FirewallSettingOff()
