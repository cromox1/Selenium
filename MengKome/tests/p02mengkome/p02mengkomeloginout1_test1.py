__author__ = 'cromox'

from pages.p01google.p01searchgithubcromox1 import P01SearchGitHubCromox1
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import sys

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class P01SearchGitHubCromox1Tests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)
    urlnow = None

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.googlesearchpage = P01SearchGitHubCromox1(self.driver)
        self.tstatus = tStatus(self.driver)

    # @pytest.mark.run(order=1)
    @pytest.mark.tryfirst
    def test1_google_github_cromox1_page(self):
        self.log.info("=== >> " + sys._getframe().f_code.co_name + " started")
        result = self.googlesearchpage.verifyPageURLlow("https://www.google.co.uk")
        self.tstatus.mark(result, "Currently At Google Page Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googlesearchpage.verifyWordExistInURL('google')
        self.tstatus.mark(result, "google word Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.googlesearchpage.gotoSearchArea()
        self.googlesearchpage.searchGitHubCromox1()
        self.googlesearchpage.gotoGitHubCromox1()
        result = self.googlesearchpage.verifyWordExistInURL('cromox1')
        self.tstatus.mark(result, "GitHub cromox1 word Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googlesearchpage.verifyPageURL("https://github.com/cromox1/")
        self.__class__.urlnow = self.googlesearchpage.returnCurrentURL().rstrip('/')
        print("ResultLast = " + str(result))
        self.tstatus.markFinal("URL GitHub cromox1 verified", result, sys._getframe().f_code.co_name)

    # @pytest.mark.run(order=2)
    @pytest.mark.trylast
    def test2_github_cromox1_repo(self):
        self.log.info("=== >> " + sys._getframe().f_code.co_name + " started")
        urlcurrent = self.__class__.urlnow
        print('CROMOX1_URL = ' + urlcurrent)
        result = self.googlesearchpage.verifyPageURL("https://github.com/cromox1/")
        self.tstatus.mark(result, "GitHub cromox1 URL Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.googlesearchpage.gotosite(urlcurrent + '?tab=repositories')
        print('CURRENT URL = ' + self.googlesearchpage.returnCurrentURL())
        result = self.googlesearchpage.verifyPageURL("https://github.com/cromox1?tab=repositories")
        self.tstatus.mark(result, "GitHub cromox1 Repositories URL Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        list_repo1 = self.googlesearchpage.getElementList('wb-break-all', locatorType='class')
        # print('LIST = ' + str(list_repo1))
        print('NUMBER OF REPO = ' + str(len(list_repo1)))
        result = self.googlesearchpage.verifyActualGreaterEqualExpected(len(list_repo1), 1)
        self.tstatus.mark(result, "Repositories exist i.e. more than 0")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        i = 1
        for element in list_repo1:
            print(str(i) + ') ' + element.text)
            i = i + 1
        # self.assertEqual(i - 1, len(list_repo1))
        result = self.googlesearchpage.verifyActualEqualExpected(i - 1, len(list_repo1))
        self.tstatus.mark(result, "Repositories number verified")
        print("ResultLast = " + str(result))
        self.tstatus.markFinal("GitHub cromox1 repositories verified", result, sys._getframe().f_code.co_name)