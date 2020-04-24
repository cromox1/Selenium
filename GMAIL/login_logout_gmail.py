__author__ = 'cromox'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import selenium as checkselenium
import sys

def logingmail(gmailuser, gmailpswd, browser='chrome', loginoption='option1'):
    gmaillogin = "https://accounts.google.com/signin"

    if browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-extensions')
        #chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--start-maximized")
        driver1 = webdriver.Chrome(chrome_options=chrome_options)
        strver = 'version'
    elif browser == 'firefox':
        driver1 = webdriver.Firefox()
        strver = 'browserVersion'
    else:
        browserapp = browser.capitalize()+'()'
        driver1 = webdriver+'.'+browserapp
        print(driver1)
        # break
        strver = 'browserVersion'

    driver1.delete_all_cookies()
    driver1.implicitly_wait(30)

    ### browser + version
    print('Browser version ( ' + driver1.name + ' ) = ' + driver1.capabilities[strver])
    print('Selenium version = '+ str(checkselenium.__version__))
    # print('webdriver version = '+ str(driver1.capabilities) + '\n')

    if loginoption == 'option1':
        driver1.get(gmaillogin+'?Email='+gmailuser)
        print('URL 1 = ' + str(driver1.current_url))
        driver1.find_element_by_css_selector("span.RveJvd.snByac").click()
        time.sleep(3)
        driver1.find_element_by_name("password").send_keys(gmailpswd)
        print('URL 2 = ' + str(driver1.current_url))
        driver1.find_element_by_css_selector("span.RveJvd.snByac").click()
    elif loginoption == 'option2':
        driver1.get(gmaillogin)
        print('URL 1 = ' + str(driver1.current_url))
        driver1.find_element_by_id("identifierId").click()
        driver1.find_element_by_id("identifierId").clear()
        driver1.find_element_by_id("identifierId").send_keys(gmailuser+Keys.ENTER)
        time.sleep(3)
        driver1.find_element_by_name("password").send_keys(gmailpswd+Keys.ENTER)

    time.sleep(5)
    return driver1

def logoutgmail(driver1):

    gmaillogout = "https://accounts.google.com/Logout"
    driver1.get(gmaillogout)
    print('URL 3 = ' + str(driver1.current_url))
    time.sleep(5)
    driver1.quit()

if __name__ == "__main__":
    print('Python Version = ' + sys.version + '\n')
    gmailuser = 'rushzahal@gmail.com'     ## YOUR GMAIL USER'S EMAIL
    gmailpswd = 'Apsajerlah!'             ## YOUR GMAIL USER'S PASSWORD
    driver1 = logingmail(gmailuser, gmailpswd)
    logoutgmail(driver1)
