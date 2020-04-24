__author__ = 'cromox'

### modified from this URL
## https://medium.com/the-andela-way/introduction-to-web-scraping-using-selenium-7ec377a8cf72

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
# import sys

option = webdriver.ChromeOptions()
option.add_argument("— incognito")

# urlgithubtogo = sys.argv[1]
urlgithubtogo = "https://github.com/cromox1"
print('\n'+'URL to query = '+str(urlgithubtogo)+'\n')
browser = webdriver.Chrome(chrome_options=option)
browser.get(urlgithubtogo)

# Wait 20 seconds for page to load
timeout = 10
try:
    # Wait until the final element [Avatar link] is loaded.
    # Assumption: If Avatar link is loaded, the whole page would be relatively loaded because it is among
    # the last things to be loaded.
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))

except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

print('')

# Get all of the titles for the pinned repositories
# We are not just getting pure titles but we are getting a selenium object
# with selenium elements of the titles.

# find_elements_by_xpath returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath("//a[@class='text-bold']")

# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
# print out all the titles.
print('titles: ', end='')
print(titles, '\n')

language_element = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
# same concept as for list-comprehension above.
languages = [x.text for x in language_element]
print("languages: ", end='')
print(languages, '\n')

print("RepoName : Language")
print("======== = ========")
## zip(titles, languages) = dict(zip(titles, languages)).items()
# for title, language in zip(titles, languages):
# for title, language in dict(zip(titles, languages)).items():
for title, language in zip(titles, languages):
   print(title + " : " + language)

lama=5
print('\n' + 'count 1 - ' + str(lama))
for i in range(1,lama+1):
    print(i); time.sleep(1)

print('\n'+'Semua nampak OK jer'); browser.quit()