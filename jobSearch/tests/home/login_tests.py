__author__ = 'cromox'

from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import datetime #, time
# from pyvirtualdisplay import Display
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
        # self.loginpage.indeedJobs()
        # self.adminpswd = userPasswordRead("ADMINPSWD#", self.masani).replace(' ','').split(',')[0]
        print('SETUP 1')

    @pytest.mark.run(order=1)
    def test_1IndeedJobsSearch(self):
        self.log.info("test_1IndeedJobsSearch started")
        self.loginpage.indeedJobs()
        #self.loginpage.loginAdvSetting(self.adminpswd)    # GO TO Advanced Setting
        #result = self.loginpage.verifyPageTitle('advanced dns') # Test 3
        #self.tstatus.mark(result, "Advanced Page's Title verified")
        #print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        #result = self.loginpage.firewallBlockAll()      # Test 4
        #self.tstatus.mark(result, "Firewall block all selected verified")
        #print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        #result = self.loginpage.verifyPageURL("http://192.168.1.254/advanced_firewall.html") # Test 5
        #self.tstatus.mark(result, "URL verified")
        #print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        #result = self.loginpage.verifyPageTitle('advanced firewall')    # Test 6
        #self.tstatus.mark(result, "Page Title verified")
        #print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        #result = self.loginpage.verifyFirewallIsBlockAll()       # Test 7
        #print("ResultLast = " + str(result) + '\n')
        #self.tstatus.markFinal("test_FirewallSettingBlock was successful", result, "Firewall OFF button is selected")

    #@pytest.mark.run(order=2)
    #def test_2MonsterJobsSearch(self):
    #    self.log.info("test_2MonsterJobsSearch started")
    #    self.loginpage.monsterJobs()
    #
    #@pytest.mark.run(order=3)
    #def test_3TotalJobsSearch(self):
    #    self.log.info("test_3TotalJobsSearch started")
    #    self.loginpage.totalJobs()
    #
    #@pytest.mark.run(order=4)
    #def test_4DiceJobsSearch(self):
    #    self.log.info("test_4DiceJobsSearch started")
    #    self.loginpage.diceJobs()

    @pytest.fixture(autouse=True)
    def tearDown(self):
    #    # self.driver.quit()
    #    self.display.stop()
        print('TEAR DOWN 1')



#ff = LoginTests()
#ff.test_FirewallSettingOff()