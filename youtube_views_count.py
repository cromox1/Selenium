__author__ = 'cromox'

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_logout_gmail import logingmail, logoutgmail
import sys
import time
import re

def youtube_browse(weburl):
    driver1.get(weburl)
    wait = WebDriverWait(driver1, 0)
    video = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'video')))

    driver1.execute_script("arguments[0].muted = true;", video)
    driver1.find_element_by_css_selector("button.ytp-play-button.ytp-button").click()
    driver1.find_element_by_css_selector("button.ytp-play-button.ytp-button").click()
    print('Title = ' + driver1.title)
    print('URL YOUTUBE = ' + str(driver1.current_url))
    print('video = ' + str(video))
    session = str(video).split(sep='=')[1].split(sep='"')[1]
    element = str(video).split(sep='=')[2].split(sep='"')[1]
    print('session = ' + session + ' , element = ' + element)

    pagesrcs = driver1.page_source
    likes = re.search("with (\d*.\d*.\d*)", str(pagesrcs)).group(1).split()[0]
    # likesint = int(likes)
    # print('likes(int) = ' + str(likesint))
    print('likes(str) = ' + likes)
    views = re.search("(\d*.\d*.\d*) views", str(pagesrcs)).group(1).split(sep='"')[-1]
    print('views(str) = ' + views)

    lama = 15
    for i in range(1, lama+1):
        # print(i)
        time.sleep(1)
    print('last i = ' + str(i) + '\n')

if __name__ == "__main__":
    print('Python Version = ' + sys.version + '\n')

    gmailuser = 'rushzahal@gmail.com'     ## YOUR GMAIL USER'S EMAIL
    gmailpswd = 'Apsajerlah!'             ## YOUR GMAIL USER'S PASSWORD
    driver1 = logingmail(gmailuser, gmailpswd)

    ### login youtube
    base_url = "https://www.youtube.com"
    youtubeid = "/watch?v=aUX2nzVo0uM"
    # youtubeid = "/watch?v=kszdBNWEUwU" ## Wings - Bazooka Penaka (Full Album)
    # youtubeid = "/watch?v=gzmOZti-l5Y"
    youtubeurl = base_url + youtubeid

    youtube_browse(youtubeurl)

    ### logout gmail
    logoutgmail(driver1)

## Note :
# Browser version ( chrome ) = 63.0.3239.84
# Browser version ( firefox ) = 52.5.0
# Selenium version = 3.8.0
