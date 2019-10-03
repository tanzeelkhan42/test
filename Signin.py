import parameters
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://tjenester.avinor.no/cdm/login.html')

linkedin_username = 'oslcdm'
linkedin_password = 'oslcdm'

username = driver.find_element_by_id('username')
username.send_keys(linkedin_username)
sleep(0.5)

password = driver.find_element_by_id('password')
password.send_keys(linkedin_password)
sleep(2)

sign_in_button = driver.find_element_by_xpath('/html/body/div[1]/form/span/input').click()
sleep(5)

# username = driver.find_element_by_class_name('even')
# username.send_keys('hr manager in Dubai')
# driver.find_element_by_class_name('search-typeahead-v2').send_keys(u'\ue007')
# sleep(30)

names = driver.find_elements_by_class_name('even')
sleep(2)
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


