__author__ = 'cromox'

from pages.p01google.p01searchpixitmedia import P01SearchPixitMedia
from utilities.teststatus import TestStatus as tStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time
from requests import get as urlget
from PyPDF2 import PdfFileReader as PDFread
from os import remove as removefile

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class P01SearchPixitMediaTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.googlesearchpage = P01SearchPixitMedia(self.driver)
        self.tstatus = tStatus(self.driver)
        self.tmpfilename = 'tmptest123.pdf'

    @pytest.mark.run(order=1)
    def test1_google_pixitmedia_page(self):
        self.log.info("test1_goto_google_page_started")
        result = self.googlesearchpage.verifyPageURLlow("https://www.google.co.uk")
        self.tstatus.mark(result, "Currently At Google Page Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googlesearchpage.verifyWordExistInURL('google')
        self.tstatus.mark(result, "google word Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.googlesearchpage.gotoSearchArea()
        self.googlesearchpage.searchPixitMedia()
        self.googlesearchpage.gotoPixitMediaPage()
        result = self.googlesearchpage.verifyWordExistInURL('pixitmedia')
        self.tstatus.mark(result, "pixitmedia word Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googlesearchpage.verifyPageURLlow("https://www.pixitmedia.com/")
        print("ResultLast = " + str(result))
        self.tstatus.markFinal("URL pixitmedia verified", result, "test1_google_pixitmedia")

    @pytest.mark.run(order=2)
    def test2_products_page(self):
        self.log.info("test2_goto_pixstor_page_started")
        self.basepixitmediaurl = self.googlesearchpage.returnCurrentURL()
        self.googlesearchpage.gotoProductsPage()
        result = self.googlesearchpage.verifyWordExistInURL('products')
        self.tstatus.mark(result, "products word Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.googlesearchpage.gotoPixStor()
        result = self.googlesearchpage.verifyWordExistInURL('PixStor-Search')
        self.tstatus.mark(result, "PixStor-Search word Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.googlesearchpage.viewDatasheet()
        result = self.googlesearchpage.verifyWordExistInURL('Datasheet')
        self.tstatus.mark(result, "Datasheet word Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        time.sleep(3)
        req = urlget(self.driver.current_url)
        ## validate PDF file
        # validate1 - simple by check size & header (contain pdf type)
        result = self.googlesearchpage.verifyActualGreaterEqualExpected(int(req.headers['Content-Length']), 1000)
        self.tstatus.mark(result, "File bigger than 1000 bytes")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googlesearchpage.verifyTextEqual(req.headers['Content-Type'], 'application/pdf')
        self.tstatus.mark(result, "File has Content-Type application/pdf")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        # validate2 - download & check file using PyPDF2
        file1 = open(self.tmpfilename, "wb")
        file1.write(req.content)
        pdfproducer = PDFread(self.tmpfilename).getDocumentInfo().producer
        file1.close()
        pdfchklist = ['Adobe', 'PDF', 'Acrobat']  # search this words - to confirm PDF
        listintrsect = [x.upper() for x in pdfchklist if x.upper() in pdfproducer.upper()]
        result = self.googlesearchpage.verifyActualGreaterEqualExpected(len(listintrsect), 1)
        self.tstatus.mark(result, "File is PDF format")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googlesearchpage.verifyPageURL("https://www.pixitmedia.com/wp-content/uploads/2018/03/PixStor-Search-Datasheet.pdf")
        print("ResultLast = " + str(result))
        self.tstatus.markFinal("View pdf doc verified", result, "test2_products_page")
        self.googlesearchpage.gotosite(self.basepixitmediaurl)
        ## Finally - remove tmpfile
        try:
            removefile(self.tmpfilename)
        except WindowsError as exxe:
            print('  Error = ' + str(exxe) + ' / file = ' + str(self.tmpfilename))

    @pytest.mark.run(order=3)
    def test3_contactus_page(self):
        self.log.info("test3_fill_in_contactus_page_started")
        self.googlesearchpage.gotoContactUs()
        time.sleep(3)
        result = self.googlesearchpage.verifyPageURL("https://www.pixitmedia.com/contact-us/")
        self.tstatus.mark(result, "ContactUs URL Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        result = self.googlesearchpage.verifyWordExistInURL('contact-us')
        self.tstatus.mark(result, "ContactUs word Verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.googlesearchpage.fillfirstname('Rosli1')
        self.googlesearchpage.filllastname('Talib1')
        self.googlesearchpage.fillemailadd('roslitalib2017@gmail.com')
        emailx = self.googlesearchpage.email_on_emailsection()
        result = self.googlesearchpage.verifyEmailFormat(emailx)
        self.tstatus.mark(result, "Email address verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.googlesearchpage.fillorganisation('TesterOne')
        self.googlesearchpage.fillcontactno('07799888444')
        phonex = self.googlesearchpage.phone_on_phonesection()
        result = self.googlesearchpage.verifyPhoneNumber(phonex)
        self.tstatus.mark(result, "PhoneNumber verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        self.googlesearchpage.fillsubject('LastTest - before wrap-up')
        self.googlesearchpage.fillmessage('This is a test for Jez')
        result = self.googlesearchpage.verifyMessageTab()
        self.tstatus.mark(result, "Text messages verified")
        print("Result " + str(len(self.tstatus.resultList)) + "  =  " + str(result))
        sendtxt = self.googlesearchpage.clickToSendMessage()
        result = self.googlesearchpage.verifyTextEqual(sendtxt, 'SEND')
        print("ResultLast = " + str(result))
        self.tstatus.markFinal("Contact Us page verified", result, "test3_contactus_page")