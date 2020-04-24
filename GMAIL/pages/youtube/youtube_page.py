__author__ = 'cromox'

from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
# import time

class YoutubePage(BasePage):

    # masani = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _avatar_field = '//*[@id="img"]'
    _avatar_field_type = 'xpath'
    #_emailid_field = '//*[@id="email"]'
    #_emailid_field = '//*[@id="gbw"]/div/div/div[2]/div[4]/div[2]/div[1]/div/div[2]'
    #_emailid_field_type = 'xpath'
    #_emailid_field = 'email'
    #_emailid_field_type = 'id'
    # _emailid_field = 'gb_db.gbii'
    _emailid_field = 'yt-formatted-string.ytd-active-account-header-renderer:nth-child(2)'
    _emailid_field_type = 'css'


    def clickAvatarButton(self, locator, locatorType):
        self.elementClick(locator, locatorType)

    def gotoyoutube(self, youtubeid):
        youtubeBaseURL = "https://www.youtube.com"
        youtubeURL = youtubeBaseURL + "/watch?v=" + youtubeid
        self.driver.get(youtubeURL)

    def verifyUserEmailId(self):
        self.clickAvatarButton(self._avatar_field, self._avatar_field_type)
        return self.getText(self._emailid_field, self._emailid_field_type)

    def youtubevideo(self, driver):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        import re
        import time
        wait = WebDriverWait(driver, 0)
        video = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'video')))
        driver.execute_script("arguments[0].muted = true;", video)
        driver.find_element_by_css_selector("button.ytp-play-button.ytp-button").click()
        driver.find_element_by_css_selector("button.ytp-play-button.ytp-button").click()
        print('\nTitle = ' + str(driver.title))
        print('URL YOUTUBE = ' + str(driver.current_url))
        pagesrcs = driver.page_source
        likes = re.search("along with (\d*.\d*.\d*)", str(pagesrcs)).group(1).split()[0]
        print('likes(str) = ' + str(likes))
        views = re.search("(\d*.\d*.\d*) views", str(pagesrcs)).group(1).split(sep='"')[-1]
        print('views(str) = ' + str(views) + '\n')
        time.sleep(15)
        return str(driver.title),str(views.replace(',','')),str(likes.replace(',',''))