__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from requests import get as urlget
from PyPDF2 import PdfFileReader as PDFread
from os import remove as removefile
from selenium.webdriver.common.action_chains import ActionChains as hoover

class TestOne(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        self.driver = webdriver.Chrome(self.chromedriverpath)
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.co.uk"
        self.verificationErrors = []
        self.tmpfilename = 'tmptest123.pdf'

    def test_one(self):
        driver = self.driver
        if driver.name == 'chrome':
            driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_name('q').click()
        driver.find_element_by_name('q').send_keys("pixitmedia" + Keys.ENTER)
        list_pixitmedia = driver.find_elements_by_xpath("//*[contains(text(),'Pixit Media')]")
        # for element in list_pixitmedia:
        #     if element.text == "https://www.pixitmedia.com/":
        #         element.click()
        # if driver.find_element_by_xpath("//*[contains(text(),'https://www.pixitmedia.com/')]").text == "https://www.pixitmedia.com/":
        #     driver.get("https://www.pixitmedia.com/")
        list_pixitmedia[0].click()
        basepixitmediaurl = driver.current_url
        print('PIXITMEDIA URL = ' + str(basepixitmediaurl))
        # Products -- HAS EXPIRED & HAS CHANGED
        # driver.find_element_by_xpath('//*[@id="menu-item-48"]/a/span').click()
        # PixStor -- HAS EXPIRED & CHANGED... NOW USE HOOVER
        # driver.find_element_by_link_text('PixStor').click()
        # driver.find_element_by_link_text("PixStor Search").click()
        element_pixstor = driver.find_elements_by_xpath("//*[contains(text(),'PixStor')]")[0]
        hoover(driver).move_to_element(element_pixstor).perform()
        features_el = driver.find_element_by_xpath("//*[contains(text(),'Features')]")
        hoover(driver).move_to_element(features_el).perform()
        powersearch_el = driver.find_element_by_xpath("//*[contains(text(),'Powerful Search')]")
        hoover(driver).move_to_element(powersearch_el).perform()
        powersearch_el.click()

        # # View Datasheet - PDF file -- NOW NO LONGER EXIST !!!!
        # driver.find_element_by_xpath("//span[@class='elementor-button-text']").click()
        #
        # ## validate PDF file
        # currenturl = driver.current_url
        # req = urlget(currenturl)
        # # validate1 - simple by check header
        # self.assertGreater(int(req.headers['Content-Length']), 1000)
        # self.assertEqual(req.headers['Content-Type'], 'application/pdf')
        # # validate2 - download & check file using PyPDF2
        # file1 = open(self.tmpfilename, "wb")
        # file1.write(req.content)
        # pdfproducer = PDFread(self.tmpfilename).getDocumentInfo().producer
        # file1.close()
        # pdfchklist = ['Adobe', 'PDF', 'Acrobat']  # words to confirm PDF
        # listintrsect = [x.upper() for x in pdfchklist if x.upper() in pdfproducer.upper()]
        # self.assertGreaterEqual(len(listintrsect), 1)

        # Contact Us Form
        driver.get(basepixitmediaurl)
        driver.find_element_by_xpath("//*[contains(text(),'Contact Us')]").click()
        print("URL Contact Us = " + str(driver.current_url))
        driver.find_element_by_xpath('//*[@placeholder="First Name"]').click()
        driver.find_element_by_xpath('//*[@placeholder="First Name"]').clear()
        driver.find_element_by_xpath('//*[@placeholder="First Name"]').send_keys("Rosli")
        # driver.find_element_by_id("input_2_1_3").click()
        # driver.find_element_by_id("input_2_1_3").clear()
        # driver.find_element_by_id("input_2_1_3").send_keys("Rosli")
        # driver.find_element_by_id("input_2_1_3").send_keys("TesterOne")
        driver.find_element_by_id("input_2_1_6").click()
        driver.find_element_by_id("input_2_1_6").clear()
        driver.find_element_by_id("input_2_1_6").send_keys("Talib")
        # driver.find_element_by_id("input_2_1_6").send_keys("LastNameOne")
        driver.find_element_by_id("input_2_2").click()
        driver.find_element_by_id("input_2_2").clear()
        driver.find_element_by_id("input_2_2").send_keys("roslitalib2017@gmail.com")
        driver.find_element_by_id("input_2_3").click()
        driver.find_element_by_id("input_2_3").clear()
        driver.find_element_by_id("input_2_3").send_keys("Ranorexxx")
        driver.find_element_by_id("input_2_7").click()
        driver.find_element_by_id("input_2_7").clear()
        # driver.find_element_by_id("input_2_7").send_keys("xxxxxxxxxxxxx")
        driver.find_element_by_id("input_2_7").send_keys("07777999111")
        driver.find_element_by_id("input_2_4").click()
        driver.find_element_by_id("input_2_4").clear()
        driver.find_element_by_id("input_2_4").send_keys("Test1")
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
