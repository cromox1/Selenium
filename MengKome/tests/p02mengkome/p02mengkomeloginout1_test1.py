__author__ = 'cromox'

from pages.p02mengkome.p02mengkomeloginout1 import P02LoginLogoutCookie
from utilities.teststatus import TestStatus as tStatus
# import datetime
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import sys

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class P02MengkomeLoginLogoutTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    mengkome_url = 'https://mengkome.pythonanywhere.com'
    urlnow = ''
    cookie = {}

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.mengkomepage = P02LoginLogoutCookie(self.driver)
        self.tstatus = tStatus(self.driver)
        print('\n--- >> SETUP')

    # @pytest.mark.run(order=1)
    @pytest.mark.tryfirst
    def test1_login_mengkome_add_cookie_page(self):
        # login with user/pswd auth & add cookie
        self.log.info("=== >> " + sys._getframe().f_code.co_name + " started")
        self.mengkomepage.gotosite(self.mengkome_url)
        result = self.mengkomepage.verifyPageURLlow(self.mengkome_url)
        self.tstatus.mark(result, "Currently At Mengkome Page Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.mengkomepage.verifyWordExistInURL('mengkome')
        self.tstatus.mark(result, "mengkome word Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.mengkomepage.keyinUserAuthentication()
        self.cookies = self.mengkomepage.returnCookies()
        result = self.mengkomepage.verifyActualGreaterEqualExpected(len(self.cookies), 1)
        self.tstatus.mark(result, "Cookies list Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        domainmengkome = self.mengkomepage.returnDomainFrURL(self.mengkome_url)
        self.__class__.cookie = self.mengkomepage.returnLoginCookie(self.cookies, domainmengkome)
        result = self.mengkomepage.verifyDateIsFuture(self.__class__.cookie['expiry'])
        self.tstatus.mark(result, "Cookie expiry date Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.mengkomepage.verifyTextEqual(self.__class__.cookie['domain'], domainmengkome)
        print("ResultLast = " + str(result))
        self.tstatus.markFinal("Login & cookie Verified", result, sys._getframe().f_code.co_name)
        self.__class__.urlnow = self.mengkomepage.returnCurrentURL()

    # @pytest.mark.run(order=2)
    @pytest.mark.trylast
    def test2_relogin_bycookie_chkinfos(self):
        # auto login using test1 cookie & chk infos
        self.log.info("=== >> " + sys._getframe().f_code.co_name + " started")
        urlcurrent = self.__class__.urlnow
        print('MENGKOME_URL = ' + urlcurrent)
        self.mengkomepage.gotosite(urlcurrent)
        result = self.mengkomepage.verifyPageURLlow('https://mengkome.pythonanywhere.com')
        self.tstatus.mark(result, "Currently At Mengkome Page Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.mengkomepage.addcookietosite(self.__class__.cookie)
        self.mengkomepage.gotosite(urlcurrent)
        print('URL = ' + str(self.mengkomepage.returnCurrentURL()))
        userinfos = self.mengkomepage.gotoUsersPage()
        result = self.mengkomepage.verifyActualGreaterEqualExpected(len(userinfos[0]), 1)
        self.tstatus.mark(result, "Username " + userinfos[0] + ' existance Verified')
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.mengkomepage.verifyEmailFormat(userinfos[1])
        self.tstatus.mark(result, "Email (format) Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))

        # # date joined format = 'Nov. 8, 2018, 2:08 p.m.'
        # joineddate = datetime.datetime.strptime(userinfos[2], '%M %d, %Y').strftime("%s")
        # print('Date1 = ' + str(userinfos[2]) + ' / Date2 = ' + str(joineddate))
        # result = self.mengkomepage.verifyDateIsHistory(joineddate)
        # self.tstatus.mark(result, "Date joined Verified")
        # print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))

        # result = self.googlesearchpage.verifyActualEqualExpected(i - 1, len(list_repo1))
        # self.tstatus.mark(result, "Repositories number verified")
        # print("ResultLast = " + str(result))
        # self.tstatus.markFinal("GitHub cromox1 repositories verified", result, sys._getframe().f_code.co_name)

    def tearDown(self):
        print('\n--- >> TEARDOWN')
