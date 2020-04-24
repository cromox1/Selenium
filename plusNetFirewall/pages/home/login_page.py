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

    # Locators Base
    _password_field = 'password'
    _password_field_type = 'id'
    _pswd_next_button = "passwordNext"
    _pswd_next_button_type = "id"

    # Locator Advanced Settings
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

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, self._password_field_type)

    def clickButtonAfterWait(self, locator, locatorType):
        elementone = self.waitForElement(locator, locatorType, timeout=5, pollFrequency=1)
        self.elementClick(element=elementone)

    def loginAdvSetting(self, password=""):
        time.sleep(1)
        if self.verifyPageURLlow('http://192.168.1.254') == True:
            self.elementClick(self._advanced_sttg, self._common_loc_type)
        else:
            # return
            self.plusNet()
            time.sleep(1)
            self.elementClick(self._advanced_sttg, self._common_loc_type)
        if self.isElementPresent(self._admin_pswd_fld, self._common_loc_type) == True:
            self.sendKeys(password, self._admin_pswd_fld, self._common_loc_type)
            self.elementClick(self._login_button, self._common_loc_type)
            time.sleep(1)
        if self.isElementPresent(self._understand_bttn, self._common_loc_type) == True:
            self.clickButtonAfterWait(self._understand_bttn, self._common_loc_type)
            time.sleep(1)

    def firewallAllowAll(self):
        self.clickButtonAfterWait(self._firewall_bttn, self._common_loc_type)
        time.sleep(2)
        if self.getElementIsSelected(self._off_all_bttn) == False:
            self.log.info('Off button is not selected')
            self.getElement(self._off_all_bttn, self._common_loc_type).click()
            self.getElement(self._apply_bttn, self._common_loc_type).click()
        else:
            self.log.info('Off button is selected')
        return self.getElementIsSelected(self._off_all_bttn)

    def firewallBlockAll(self):
        self.clickButtonAfterWait(self._firewall_bttn, self._common_loc_type)
        time.sleep(2)
        if self.getElementIsSelected(self._block_all_bttn) == False:
            self.log.info('Block All button is not selected')
            self.getElement(self._block_all_bttn, self._common_loc_type).click()
            self.getElement(self._apply_bttn, self._common_loc_type).click()
        else:
            self.log.info('Block All button is selected')
        return self.getElementIsSelected(self._block_all_bttn)

    def verifyFirewallIsOff(self):
        return self.getElementIsSelected(self._off_all_bttn)

    def verifyFirewallIsBlockAll(self):
        return self.getElementIsSelected(self._block_all_bttn)
