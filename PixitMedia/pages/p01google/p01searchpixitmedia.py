__author__ = 'cromox'

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
from selenium.webdriver.common.keys import Keys
# import datetime

class P01SearchPixitMedia(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ## Locators Google
    _search_area = "//*[@title='Search']"
    -search_area_type = 'xpath'
    _search_data = "pixitmedia"
    #_pixitmedia_txt1 = u"pixitmedia – High Performance Software Defined Storage"
    #_pixitmedia_txt2 = u"pixitmedia – High Performance Software Defined Sto"
    #_pixitmedia_txt3 = "Pixit Media"

    ## Locators PixitMedia page
    _products_link = '//*[@id="menu-item-48"]/*/*'
    _pixstor_link = "PixStor Search"
    _pdf_datasheet = "//span[@class='elementor-button-text']"

    ## ContactUs page
    _contactus = '//*[@id="menu-item-8974"]/*/*'
    _firstname = "field_qh4icy2"
    _lastname = "field_ocfup12"
    _emailadd = "field_29yf4d2"
    _organztn = "field_fz52u"
    _contctno = "field_yuy03"
    _subjectt = "field_e6lis62"
    _messages = "field_9jv0r12"
    _sendmsgs = "//button[@type='submit']"

    ## Google page
    def gotoSearchArea(self):
        self.elementClick(self._search_area, locatorType=self._search_area_type)

    def searchPixitMedia(self):
        self.sendKeys(self._search_data, self._search_area)
        self.sendKeys(Keys.ENTER, self._search_area)

    def gotoPixitMediaPage(self):
        #if self.isElementPresent(self._pixitmedia_txt1, locatorType="link") == True:
        #    self.elementClick(self._pixitmedia_txt1, locatorType="link")
        #elif self.isElementPresent(self._pixitmedia_txt2, locatorType="link") == True:
        #    self.elementClick(self._pixitmedia_txt2, locatorType="link")
        #elif self.isElementPresent(self._pixitmedia_txt3, locatorType="link") == True:
        #    self.elementClick(self._pixitmedia_txt3, locatorType="link")
        if self.getText("//*[contains(text(),'https://www.pixitmedia.com/')]", locatorType="xpath") == "https://www.pixitmedia.com/":
            self.gotosite("https://www.pixitmedia.com/")

    ## PixitMedia page
    def gotoProductsPage(self):
        self.elementClick(self._products_link, locatorType='xpath')

    def gotoPixStor(self):
        self.elementClick(self._pixstor_link, locatorType="link")

    def viewDatasheet(self):
        self.elementClick(self._pdf_datasheet, locatorType="xpath")

    ## ContactUs page
    def gotoContactUs(self):
        self.elementClick(self._contactus, locatorType="xpath")

    def fillfirstname(self, firstname):
        self.filldataarea(firstname, self._firstname)

    def filllastname(self, lastname):
        self.filldataarea(lastname, self._lastname)

    def fillemailadd(self, emailadd):
        self.filldataarea(emailadd, self._emailadd)

    def fillorganisation(self, organisation):
        self.filldataarea(organisation, self._organztn)

    def fillcontactno(self, contactno):
        self.filldataarea(contactno, self._contctno)

    def fillsubject(self, subject):
        self.filldataarea(subject, self._subjectt)

    def fillmessage(self, message):
        self.filldataarea(message, self._messages)

    def clickToSendMessage(self):
        text = self.getText(self._sendmsgs, locatorType="xpath")
        self.elementClick(self._sendmsgs, locatorType="xpath")
        return text

    def filldataarea(self, data, locator, locatorType='id'):
        self.elementClick(locator, locatorType)
        self.getElement(locator, locatorType).clear()
        self.sendKeys(data, locator, locatorType)

    def verifyMessageTab(self):
        if self.isElementPresent(self._messages) == True:
            if len(self.getValueSend(self._messages)) > 1:
                return True
            else:
                return False
        else:
            return False

    ## General
    def returnCurrentURL(self):
        return self.driver.current_url

    def gotosite(self, URL):
        return self.driver.get(URL)

    def email_on_emailsection(self):
        if self.isElementPresent(self._emailadd) == True:
            return self.getValueSend(self._emailadd)

    def phone_on_phonesection(self):
        if self.isElementPresent(self._contctno) == True:
            return self.getValueSend(self._contctno)
