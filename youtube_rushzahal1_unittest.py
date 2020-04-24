__author__ = 'cromox'

### NOTE : Browser version ( chrome ) = 63.0.3239.84 / Selenium version = 3.8.0
## IN-PROGRESS 
## TO DO - 
# 1) change into main scripts (or create main scripts and modify this)
# 2) add more unittests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import unittest, time #, re

class YoutubeRushzahal1(unittest.TestCase):
    def setUp(self):
        # self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_argument("--mute-audio")
        # self.chrome_options.add_argument("--incognito")
        # self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.youtube.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_youtube_rushzahal1(self):
        driver = self.driver
        driver.get(self.base_url + "/watch?v=aUX2nzVo0uM")
        # wait for video tag to show up
        wait = WebDriverWait(driver, 1)
        video = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'video')))
        driver.execute_script("arguments[0].muted = true;", video)
        driver.find_element_by_css_selector("button.ytp-play-button.ytp-button").click()
        driver.find_element_by_css_selector("button.ytp-play-button.ytp-button").click()
        self.assertEqual("The Land of Gibbery - YouTube", driver.title)

        try:
            self.assertEqual("The Land of Gibbery - YouTube", driver.title)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        for i in range(60):
            try:
                if "The Land of Gibbery - YouTube" == driver.title:
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")

        lama = 15
        for i in range(1, lama+1):
            print(i)
            time.sleep(1)

        try:
            self.assertTrue(self.is_element_present(By.XPATH, "(//div[@id='dismissable']/a)[6]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
