__author__ = 'cromox'

"""
@package base
WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations
Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
# import traceback
from selenium import webdriver
# import os

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class
        Returns:
            None
        """
        self.browser = browser
        #"""
        #Set chrome driver and iexplorer environment based on OS
        #
        #chromedriver = "C:/.../chromedriver.exe"
        #os.environ["webdriver.chrome.driver"] = chromedriver
        #self.driver = webdriver.Chrome(chromedriver)
        #
        #PREFERRED: Set the path on the machine where browser will be executed
        #"""

    def getWebDriverInstance(self, baseURL):
        """
        Get WebDriver Instance based on the browser configuration
        Returns:
            'WebDriver Instance'
        """
        # strver = 'version'
        strver = 'browserVersion'
        driver_name = 'unknown'
        driver_version = 'unknown'
        if self.browser == "iexplorer" or self.browser == "ie" or self.browser == "IE":
            # Set IE driver
            iedriverserver = r'C:\tools\Python36\Scripts\IEDriverServer_x64_2.42.0.exe'
            # iedriverserver = r'C:\tools\Python36\Scripts\IEDriverServer_x64_3.12.0.exe' ## not working
            # iedriverserver = r'C:\tools\Python36\Scripts\IEDriverServer_x32_3.4.0.exe'  ## work but 32bit
            driver = webdriver.Ie(iedriverserver)
        elif self.browser == 'safari':   ### Safari not working on Windows - need Safari 10 on OSX El Capitan
            safaridriver = r'C:\tools\Python36\Scripts\SafariDriver.exe'
            driver = webdriver.Safari(safaridriver)
        elif self.browser == 'opera':
            # OperaDriver - win64 2.36 - https://github.com/operasoftware/operachromiumdriver/releases
            from os import listdir
            from selenium.webdriver.common import desired_capabilities as operacapabilities
            from selenium.webdriver.opera import options as operaoptions
            # OperaDriver - win64 2.36 - https://github.com/operasoftware/operachromiumdriver/releases
            _operaDriverLoc = r'C:\tools\Python36\Scripts\operadriver_win64_2.36.exe'
            # Opera browser
            _operaInstDir = r'C:\Program Files\Opera\\'
            listOperaDir = listdir(_operaInstDir)
            listOperaVer = [char for char in listOperaDir if char[0].isdigit() and char[-1].isdigit()]
            # listOperaVer.sort(key=lambda version: [int(ver) for ver in version.split('.')])
            listOperaVer.sort()
            _operacurrentversion = listOperaVer[-1]
            _operaExeLoc = _operaInstDir + _operacurrentversion + r'\opera.exe'
            _operaCaps = operacapabilities.DesiredCapabilities.OPERA.copy()
            _operaOpts = operaoptions.ChromeOptions()
            _operaOpts._binary_location = _operaExeLoc
            # driver = webdriver.Chrome(executable_path = _operaDriverLoc, chrome_options = _operaOpts, desired_capabilities = _operaCaps)
            driver = webdriver.Opera(executable_path = _operaDriverLoc, options = _operaOpts, desired_capabilities = _operaCaps)
            driver_name = 'opera'
            driver_version = _operacurrentversion
        elif self.browser == "firefox" or self.browser == "ff":
            driver = webdriver.Firefox()
            # strver = 'browserVersion'
        elif self.browser == "headless" or self.browser == "nobrowser" or self.browser == "virtual":
            # This is for running without open Browser UI display - good for Jenkins
            chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument("--incognito")
            # chrome_options.add_argument("--disable-plugins-discovery")
            # chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--proxy-server='direct://'")
            chrome_options.add_argument("--proxy-bypass-list=*")
            driver = webdriver.Chrome(chromedriverpath, options=chrome_options)
        else:
            # Set chrome driver
            # self.browser == "chrome":
            chromedriverpath = r'C:\tools\chromedriver\chromedriver.exe'
            #os.environ["webdriver.chrome.driver"] = chromedriverpath
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--disable-extensions')
            #chrome_options.add_argument('--profile-directory=Default')
            chrome_options.add_argument("--incognito")
            # chrome_options.add_argument("--disable-plugins-discovery")
            # chrome_options.add_argument("--start-maximized")
            driver = webdriver.Chrome(chromedriverpath, options=chrome_options)
            #driver.set_window_size(1440, 900)

        # dah jadikan default browser = chrome
        # else:
        #    driver = webdriver.Firefox()
        #    strver = 'browserVersion'

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(10)

        # Maximize the window
        if driver.name == 'chrome' and driver_name == 'unknown':
            driver.maximize_window()

        # Loading browser with App URL
        driver.get(baseURL)

        if driver_name != 'unknown':
            print('Browser version ( ' + str(driver_name) + ' ) = ' + str(driver_version))
        else:
            print('Browser version ( ' + driver.name + ' ) = ' + driver.capabilities[strver])

        return driver