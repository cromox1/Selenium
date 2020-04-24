__author__ = 'cromox'

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
# import time

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators Base
    _common_loc_type = 'xpath'
    _advanced_sttg = "//b[contains(text(),'Advanced Settings')]"
    # _admin_pswd_fld = "/html/body/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/form/table/tbody/tr/td[3]/input"
    _admin_pswd_fld = "//input[@class='text_radius']"
    _login_button = "//input[@class='button_radius']"
    _understand_bttn = '//*[@value="  I  understand  "]'     # //input[@value="  I  understand  "]
    # _understand_bttn = '.button_radius'       ## _type = 'css'
    _firewall_bttn = "//b[contains(text(),'Firewall')]"

    ## Locator Firewall
    _all_radio_button = '//input[@name="firewall_setting"]'
    _off_all_bttn = '//html//tr[3]/td[1]/span[1]/input[1]'       # //big[contains(text(),'Off')] - ni word dia
    _block_all_bttn = '//html//tr[2]/td[1]/span[1]/input[1]'     # //big[contains(text(),'Block All')]
    # _default_bttn = '//html//tr[1]/td[1]/span[1]/input[1]'     # //big[contains(text(),'Default')]
    # _all_radio_button = '//input[@name="firewall_setting"]'
    _apply_bttn = '//input[@value="  Apply  "]'

    ## Indeed Jobs
    _what_space = '//*[@id="text-input-what"]'
    _where_space = '//input[@id="text-input-where"]'
    _submit_button = '//button[@type="submit"]'

    def clickButtonAfterWait(self, locator, locatorType):
        elementone = self.waitForElement(locator, locatorType, timeout=5, pollFrequency=1)
        self.elementClick(element=elementone)

    def loginjobsitesonebyone(self):
        self.indeedJobs()
        #self.monsterJobs()
        #self.diceJobs()
        #self.totalJobs()

    def indeedJobs(self):
        iJobURL = 'https://www.indeed.co.uk'
        print("\nindeedJob URL : " + iJobURL)
        self.log.info("indeedJob URL : " + iJobURL)
        self.driver.get(iJobURL)

        # self.sendKeys('QA tester', self._what_space, self._common_loc_type)
        ### to clear 'where'
        # wordada = self.getText(self._where_space, self._common_loc_type)
        # self.elementClick(self._where_space, self._common_loc_type)
        #elementwhere = self.getElement(locator="text-input-where", locatorType='id')
        #elementwhere.sendKeys(Keys.CONTROL + "a")
        #elementwhere.sendKeys(Keys.DELETE)

        #from selenium.webdriver.common.keys import Keys
        #
        #self.sendKeys(Keys.CONTROL + "a", self._where_space, self._common_loc_type)
        #self.sendKeys(Keys.DELETE, self._where_space, self._common_loc_type)
        #self.sendKeys('Oxford, Oxfordshire' + Keys.ENTER, self._where_space, self._common_loc_type)
        ## self.clickButtonAfterWait(self._submit_button, self._common_loc_type)
        #if self.isElementPresent('//*[@id="prime-popover-close-button"]/span', 'xpath') == True:
        #    self.elementClick('//*[@id="prime-popover-close-button"]/span', 'xpath')
        ## self.elementClick(self._submit_button, self._common_loc_type)

        iJobURL2 = iJobURL + '/jobs?q=QA+tester&l=Oxford+Oxfordshire'
        self.driver.get(iJobURL2)
        if self.isElementPresent('//*[@id="prime-popover-close-button"]/span', 'xpath') == True:
            self.elementClick('//*[@id="prime-popover-close-button"]/span', 'xpath')

    #def monsterJobs(self):
    #    iJobURL = 'https://www.monster.co.uk/jobs'
    #    print("\nmonsterJob URL : " + iJobURL)
    #    self.log.info("monsterJob URL : " + iJobURL)
    #    self.driver.get(iJobURL)
    #
    #def totalJobs(self):
    #    iJobURL = 'https://www.totaljobs.com/jobs'
    #    print("\ntotalJob URL : " + iJobURL)
    #    self.log.info("totalJob URL : " + iJobURL)
    #    self.driver.get(iJobURL)
    #
    #def diceJobs(self):
    #    iJobURL = 'https://uk.dice.com/jobs'
    #    print("\ndiceJob URL : " + iJobURL)
    #    self.log.info("diceJob URL : " + iJobURL)
    #    self.driver.get(iJobURL)



