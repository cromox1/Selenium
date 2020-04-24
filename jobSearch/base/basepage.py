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
# import time
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

    def verifyLocatorText(self, locator, locatorType, expectedText):
        result = self.getText(locator, locatorType)
        self.log.info("expectedText ( " + expectedText + " ) VS LocatorText ( " + result + " )")
        return result == expectedText

    def verifyLocatorTextNotNone(self, locator, locatorType):
        result = self.getText(locator, locatorType)
        self.log.info("LocatorText = " + str(result) + " locator (" + str(locator) + ") + locatorType (" + locatorType + ")")
        return result is not None