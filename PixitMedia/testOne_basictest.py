__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from requests import get as urlget
from PyPDF2 import PdfFileReader as PDFread
from os import remove as removefile

class TestOne(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.base_url = "https://www.google.com"
        self.verificationErrors = []
        self.tmpfilename = 'tmptest123.pdf'

    def test_one(self):
        driver = self.driver
        if driver.name == 'chrome':
            driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_id("lst-ib").click()
        driver.find_element_by_id("lst-ib").send_keys("pixitmedia" + Keys.ENTER)
        if driver.find_element_by_xpath("//*[contains(text(),'https://www.pixitmedia.com/')]").text == "https://www.pixitmedia.com/":
            driver.get("https://www.pixitmedia.com/")
        basepixitmediaurl = driver.current_url
        # Products
        driver.find_element_by_xpath('//*[@id="menu-item-48"]/a/span').click()
        # PixStor Search
        driver.find_element_by_link_text("PixStor Search").click()
        # View Datasheet - PDF file
        driver.find_element_by_xpath("//span[@class='elementor-button-text']").click()

        ## validate PDF file
        currenturl = driver.current_url
        req = urlget(currenturl)
        # validate1 - simple by check header
        self.assertGreater(int(req.headers['Content-Length']), 1000)
        self.assertEqual(req.headers['Content-Type'], 'application/pdf')
        # validate2 - download & check file using PyPDF2
        file1 = open(self.tmpfilename, "wb")
        file1.write(req.content)
        pdfproducer = PDFread(self.tmpfilename).getDocumentInfo().producer
        file1.close()
        pdfchklist = ['Adobe', 'PDF', 'Acrobat']  # words to confirm PDF
        listintrsect = [x.upper() for x in pdfchklist if x.upper() in pdfproducer.upper()]
        self.assertGreaterEqual(len(listintrsect), 1)

        # Contact Us Form
        driver.get(basepixitmediaurl)
        driver.find_element_by_xpath('//*[@id="menu-item-8974"]/a/span').click()
        driver.find_element_by_id("field_qh4icy2").click()
        driver.find_element_by_id("field_qh4icy2").clear()
        # driver.find_element_by_id("field_qh4icy2").send_keys("Rosli")
        driver.find_element_by_id("field_qh4icy2").send_keys("TesterOne")
        driver.find_element_by_id("field_ocfup12").click()
        driver.find_element_by_id("field_ocfup12").clear()
        # driver.find_element_by_id("field_ocfup12").send_keys("Talib")
        driver.find_element_by_id("field_ocfup12").send_keys("LastNameOne")
        driver.find_element_by_id("field_29yf4d2").click()
        driver.find_element_by_id("field_29yf4d2").clear()
        driver.find_element_by_id("field_29yf4d2").send_keys("xxxxxx@gmail.com")
        driver.find_element_by_id("field_fz52u").click()
        driver.find_element_by_id("field_fz52u").clear()
        driver.find_element_by_id("field_fz52u").send_keys("Ranorexxx")
        driver.find_element_by_id("field_yuy03").click()
        driver.find_element_by_id("field_yuy03").clear()
        # driver.find_element_by_id("field_yuy03").send_keys("xxxxxxxxxxxxx")
        driver.find_element_by_id("field_yuy03").send_keys("07777999111")
        driver.find_element_by_id("field_e6lis62").click()
        driver.find_element_by_id("field_e6lis62").clear()
        driver.find_element_by_id("field_e6lis62").send_keys("Test1")
        driver.find_element_by_id("field_9jv0r12").click()
        driver.find_element_by_id("field_9jv0r12").clear()
        # driver.find_element_by_id("field_9jv0r12").send_keys("This is a test for Jez")
        driver.find_element_by_id("field_9jv0r12").send_keys("abcdefghijkl1234567890")
        # driver.find_element_by_xpath("//button[@type='submit']").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        try:
            removefile(self.tmpfilename)
            # print('  Successfully remove tmp file ' + str(self.tmpfilename))
        except WindowsError as exx:
            print('  Error = ' + str(exx) + ' / file = ' + str(self.tmpfilename))

if __name__ == "__main__":
    unittest.main()
