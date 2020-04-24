__author__ = 'cromox'

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import time

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    # _avatar_field = '//*[@id="gb"]/div[2]/div[3]/div/div[2]/div/a/span'
    _avatar_field = '//*[@id="gb"]/*[2]/*[3]/*/*[2]/*/*/*'
    _avatar_field_type = 'xpath'
    _email_field = "identifierId"
    _email_field_type = "id"
    _email_next_button = "identifierNext"
    _email_next_button_type = "id"
    _password_field = 'password'
    _password_field_type = 'id'
    _password_field2 = '//*[@id="password"]/div[1]/div/div[1]/input'
    _password_field_type2 = 'xpath'
    # _password_field_type2 = 'id'
    _pswd_next_button = "passwordNext"
    _pswd_next_button_type = "id"
    _next_button = "span.RveJvd.snByac"
    _next_button_type = "css"
    # _next_button = "RveJvd.snByac"
    # _next_button_type = "class"

    def clickNextButton(self, locator, locatorType):
        self.elementClick(locator, locatorType)

    def enterPassword(self, password):
        self.clickNextButton(self.pilihanPswdFieldType(self.driver.name)[0], self.pilihanPswdFieldType(self.driver.name)[1])
        # self.clearFields(self.pilihanPswdFieldType(self.driver.name)[0], self.pilihanPswdFieldType(self.driver.name)[1])
        self.sendKeys(password, self.pilihanPswdFieldType(self.driver.name)[0], self.pilihanPswdFieldType(self.driver.name)[1])

    def login(self, password=""):
        time.sleep(2)
        self.clickNextButton(self._email_next_button, self._email_next_button_type)
        time.sleep(2)
        if self.getElement(self.pilihanPswdFieldType(self.driver.name)[0], self.pilihanPswdFieldType(self.driver.name)[1]) is not None:
            self.enterPassword(password)
            self.clickNextButton(self._pswd_next_button, self._pswd_next_button_type)
            time.sleep(2)
            if self.verifyPageTitle("Account Recovery Options") == True:
                self.clickNextButton(self._next_button, self._next_button_type)
                self.clickNextButton(self._next_button, self._next_button_type)
        else:
            return

    def verifyLoginSuccessful(self):
        testelement = "span.dropDown__value.header__user__name"
        testloctype = "css"
        self.waitForElement(testelement, locatorType=testloctype)
        result = self.isElementPresent(locator=testelement, locatorType=testloctype)
        return result

    def verifyLoginFailed(self):
        testelement = "//div[contains(text(),'Login failed. Make sure credentials are correct')]"
        testloctype = "xpath"
        result = self.isElementPresent(testelement, locatorType=testloctype)
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("My Account")

    def logout(self):
        time.sleep(1)
        gmaillogout = "https://accounts.google.com/Logout"
        self.driver.get(gmaillogout)
        time.sleep(1)

    def verifyNotLogin(self):
        return self.verifyPageTitle("Sign in - Google Accounts")

    def clearFields(self, locator, locatorType):
        self.getElement(locator, locatorType).clear()

    def pilihanPswdFieldType(self, drivername):
        if drivername == 'chrome':
            return self._password_field2,self._password_field_type2
        else:
            return self._password_field,self._password_field_type

    def gotoGmailBox(self):
        #gmailURL = "https://mail.google.com"
        #print("Gmail URL = " + gmailURL)
        #self.driver.get(gmailURL)
        self.clickNextButton("//a[@class='WaidBe']", 'xpath')

    def getGmailUserStatus(self):
        return self.verifyGmailUserStillLogin(self._avatar_field, self._avatar_field_type)
