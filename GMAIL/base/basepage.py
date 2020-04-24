__author__ = 'cromox'

"""
@package base
Base Page class implementation
It implements methods which are common to all the pages throughout the application
This class needs to be inherited by all the page classes
This should not be used by creating object instances
Example:
    Class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
import time
# import os

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class
        Returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title
        Parameters:
            titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def verifyPageURL(self, expectedURL):
        currentURL = self.driver.current_url
        self.log.info("expectedURL ( " + expectedURL + " ) VS currentURL ( " + currentURL + " )")
        return currentURL == expectedURL

    def verifyPageURLlow(self, expectedURL):
        currentURL1 = self.driver.current_url
        a1 = currentURL1.split('//')[0]
        a2 = currentURL1.split('//')[1]
        b1 = a2.split('/')[0]
        currentURL = a1+'//'+b1
        self.log.info("expectedURL ( " + expectedURL + " ) VS currentURL ( " + currentURL + " )")
        return currentURL == expectedURL

    def verifyPageText(self, locator, locatorType, expectedText):
        result = self.getText(locator, locatorType)
        self.log.info("expectedText ( " + expectedText + " ) VS pageText ( " + result + " )")
        return result == expectedText

    def verifyPageTextNotNone(self, locator, locatorType):
        result = self.getText(locator, locatorType)
        return result is not None

    def verifyUserEmailId(self, avatar_field, avatar_field_type, emailid_field, emailid_field_type):
        self.elementClick(avatar_field, avatar_field_type)
        return self.getText(emailid_field, emailid_field_type)

    def loginGmailUser(self, gmailemail, gmailpswd):
        from pages.home.login_page import LoginPage
        userURL = "https://accounts.google.com/signin" + '?Email=' + gmailemail
        self.log.info("GMAIL URL : " + userURL)
        self.driver.get(userURL)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.login(gmailpswd)

    def verifyGmailUserStillLogin(self, avatar_email, avatar_email_type):
        return self.isElementPresent(avatar_email, avatar_email_type)
