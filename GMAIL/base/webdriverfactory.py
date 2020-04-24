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

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        Returns:
            'WebDriver Instance'
        """

        strver = 'version'
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
            _operaDriverLoc = r'C:\tools\Python36\Scripts\operadriver_win64_2.36.exe'
            # Opera browser # Version:	53.0.2907.68  # System:	Windows 7 64-bit
            _operaExeLoc = r'C:\Program Files\Opera\53.0.2907.68\opera.exe'
            from selenium.webdriver.common import desired_capabilities as operacapabilities
            from selenium.webdriver.opera import options as operaoptions
            _operaCaps = operacapabilities.DesiredCapabilities.OPERA.copy()
            _operaOpts = operaoptions.ChromeOptions()
            _operaOpts._binary_location = _operaExeLoc
            # driver = webdriver.Chrome(executable_path = _operaDriverLoc, chrome_options = _operaOpts, desired_capabilities = _operaCaps)
            driver = webdriver.Opera(executable_path = _operaDriverLoc, options = _operaOpts, desired_capabilities = _operaCaps)
        elif self.browser == "firefox" or self.browser == "ff":
            driver = webdriver.Firefox()
            strver = 'browserVersion'
        elif self.browser == "chrome":
            # Set chrome driver
            chromedriver = r'C:\tools\Python36\Scripts\chromedriver.exe'
            #os.environ["webdriver.chrome.driver"] = chromedriver
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--disable-extensions')
            #chrome_options.add_argument('--profile-directory=Default')
            chrome_options.add_argument("--incognito")
            # chrome_options.add_argument("--disable-plugins-discovery")
            # chrome_options.add_argument("--start-maximized")
            driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
            #driver.set_window_size(1440, 900)
        elif self.browser == "headless" or self.browser == "nobrowser" or self.browser == "virtual":
            # This is for running without open Browser UI display - good for Jenkins
            chromedriver = r'C:\tools\Python36\Scripts\chromedriver.exe'
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument("--incognito")
            # chrome_options.add_argument("--disable-plugins-discovery")
            # chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--proxy-server='direct://'")
            chrome_options.add_argument("--proxy-bypass-list=*")
            driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
        else:
            driver = webdriver.Firefox()
            strver = 'browserVersion'

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)

        # Maximize the window
        # driver.maximize_window()
        print('Browser version ( ' + driver.name + ' ) = ' + driver.capabilities[strver])

        return driver
