__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import unittest
# from requests import get as urlget
# from PyPDF2 import PdfFileReader as PDFread
# from os import remove as removefile
from selenium.webdriver.common.action_chains import ActionChains as hoover

class TestOne(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n--- > setUpClass\n')

    def setUp(self):
        print('\n--- > setUp\n')
        # self.driver = webdriver.Firefox()
        self.chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
        self.chrome_options = Options()
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument("--disable-web-security")
        self.chrome_options.add_argument("--incognito")
        self.chrome_options.add_argument("--allow-running-insecure-content")
        self.chrome_options.add_argument("--allow-cross-origin-auth-prompt")
        self.chrome_options.add_argument("--disable-cookie-encryption")
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.add_argument("--test-type")
        ## webdriver section
        self.driver = webdriver.Chrome(self.chromedriverpath, options=self.chrome_options)
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.co.uk"
        self.verificationErrors = []
        # self.tmpfilename = 'tmptest123.pdf'

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
        # print("URL Contact Us = " + str(driver.current_url))
        # Full Page scroll down
        # driver.find_element_by_xpath("//*[contains(text(),'Contact Us')]").send_keys(Keys.PAGE_DOWN)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.execute_script("window.scrollTo(0, Y)")
        # Half page scroll down
        try:
            last_height = driver.execute_script("return document.body.scrollHeight")
        except:
            last_height = 1800
        if last_height <= 1800:
            last_height = 1900
        print('HEIGHT = ' + str(last_height))
        one_height = int(0.5 * last_height)
        print('0.5HEIGHT = ' + str(one_height))
        driver.execute_script("window.scrollTo(0, " + str(one_height) + ");")
        element_firstname = driver.find_element_by_name('input_1.3')
        hoover(driver).move_to_element(element_firstname).perform()
        element_firstname.clear()
        element_firstname.send_keys('Rosli')
        element_lastname = driver.find_element_by_id("input_2_1_6")
        hoover(driver).move_to_element(element_lastname).perform()
        # element_lastname.click()
        element_lastname.clear()
        element_lastname.send_keys("Talib")
        element_email = driver.find_element_by_id("input_2_2")
        hoover(driver).move_to_element(element_email).perform()
        # element_email.click()
        element_email.clear()
        element_email.send_keys("roslitalib2017@gmail.com")
        element_company = driver.find_element_by_id("input_2_3")
        hoover(driver).move_to_element(element_company).perform()
        element_company.clear()
        element_company.send_keys("Ranorexxx")
        element_phone = driver.find_element_by_id("input_2_7")
        hoover(driver).move_to_element(element_phone).perform()
        element_phone.clear()
        element_phone.send_keys("07777999111")
        element_subject = driver.find_element_by_id("input_2_4")
        hoover(driver).move_to_element(element_subject).perform()
        element_subject.clear()
        element_subject.send_keys("Test1")
        element_message = driver.find_element_by_id("input_2_6")
        hoover(driver).move_to_element(element_message).perform()
        element_message.clear()
        element_message.send_keys("This is a test for Jez")
        # Half page scroll down
        driver.execute_script("window.scrollTo(0, " + str(one_height) + ");")
        driver.find_element_by_name('input_8.1').click()
        element_send = driver.find_element_by_xpath("//*[@value='Send']")
        hoover(driver).move_to_element(element_send).perform()
        element_send.click()

    def tearDown(self):
        print('\n--- > tearDown\n')
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        # try:
        #     removefile(self.tmpfilename)
        #     # print('  Successfully remove tmp file ' + str(self.tmpfilename))
        # except WindowsError as exx:
        #     print('  Error = ' + str(exx) + ' / file = ' + str(self.tmpfilename))

    @classmethod
    def tearDownClass(cls):
        print('\n--- > tearDownClass\n')

if __name__ == "__main__":
    unittest.main()
