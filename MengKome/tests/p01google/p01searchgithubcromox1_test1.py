__author__ = 'cromox'

from pages.p01google.p01searchgithubcromox1 import P01SearchGitHubCromox1
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
# import time
# from requests import get as urlget
# from PyPDF2 import PdfFileReader as PDFread
# from os import remove as removefile

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class P01SearchGitHubCromox1Tests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.googlesearchpage = P01SearchGitHubCromox1(self.driver)
        self.tstatus = tStatus(self.driver)

    @pytest.mark.run(order=1)
    def test1_google_github_cromox1_page(self):
        self.log.info("test1_goto_google_page_started")
        result = self.googlesearchpage.verifyPageURLlow("https://www.google.co.uk")
        self.tstatus.mark(result, "Currently At Google Page Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googlesearchpage.verifyWordExistInURL('google')
        self.tstatus.mark(result, "google word Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.googlesearchpage.gotoSearchArea()
        self.googlesearchpage.searchGitHubCromox1()
        # self.googlesearchpage.gotoPixitMediaPage()
        result = self.googlesearchpage.verifyWordExistInURL('github cromox1')
        self.tstatus.mark(result, "GitHub cromox1 word Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googlesearchpage.verifyPageURLlow("https://www.github.com/cromox1/")
        print("ResultLast = " + str(result))
        self.tstatus.markFinal("URL GitHub cromox1 verified", result, "test1_google_github_cromox1")