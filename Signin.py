import parameters
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
# driver.get('https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22au%3A0%22%5D&keywords=ANZ%20Bank&origin=FACETED_SEARCH&page=1')
driver.get(
    'https://cds.frost.com/#!/')

linkedin_username = 'architha.iitkgp@gmail.com'
linkedin_password = 'cjEDyDmf91#'

username = driver.find_element_by_id('j_username')
username.send_keys(linkedin_username)
time.sleep(0.5)

password = driver.find_element_by_id('j_password')
password.send_keys(linkedin_password)
time.sleep(2)

sign_in_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/div/form/div[3]/button').click()
time.sleep(5)

# username = driver.find_element_by_class_name('even')
# username.send_keys('hr manager in Dubai')
# driver.find_element_by_class_name('search-typeahead-v2').send_keys(u'\ue007')
# sleep(30)
driver.get(
    'https://cds.frost.com/p/17119#!/nts/c?id=9541-00-AB-00-00')
time.sleep(5)

SCROLL_PAUSE_TIME = 2

# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)
#
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div[1]/form').click()
counter1 = 0

time.sleep(10)
for i in range(len(names)):
    t = names[i].find_elements_by_class_name('name-and-icon')
    if len(t) > 0:
        counter1 = counter1 + 1
print(counter1)
print(len(names))
# print(names[5].text)
counter = 0
for post in names:
    print(post.text)
    counter += 1

# driver.find_element_by_class_name('search-global-typeahead__input').send_keys("ENTER")
# sleep(0.5)

# search_query = 'site:linkedin.com/in/ AND "python developer" AND "London"'
# file_name = 'results_file.csv'
#
#
# search_query = driver.find_element_by_name('q')
# search_query.send_keys(search_query)
# sleep(0.5)
#
# search_query.send_keys(Keys.RETURN)
# sleep(3)
#
# linkedin_urls = driver.find_elements_by_class_name('iUh30')
# linkedin_urls = [url.text for url in linkedin_urls]
# sleep(0.5)

driver.quit()
