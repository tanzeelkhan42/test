# from selenium import webdriver
# import sys
# import time
# import requests
#
# # 52.144.108.174:8181,35.224.31.171:8080,200.127.1.233:8080,41.65.89.52:8080,178.57.115.124:8080,51.68.61.17:80
#
# try:
#
#     # PROXY = "52.144.108.174:8181"  # IP:PORT or HOST:PORT
#     #
#     # chrome_options = webdriver.ChromeOptions()
#     # chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
#
#     chrome_path = "chromedriver.exe"
#     driver = webdriver.Chrome(chrome_path)
#     driver.get(
#         'https://www.facebook.com/campaign/landing.php?&campaign_id=1653377901&extra_1=s%7Cc%7C318305677148%7Ce%7Cfacebook%20com%20login%7C&placement=&creative=318305677148&keyword=facebook%20com%20login&partner_id=googlesem&extra_2=campaignid%3D1653377901%26adgroupid%3D65139787642%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D1t1%26target%3D%26targetid%3Dkwd-296947902365%26loc_physical_ms%3D1011078%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMIzMmX2vW-5AIVirHtCh3_CQGCEAAYASAAEgKUrfD_BwE')
#
#     SCROLL_PAUSE_TIME = 2
#
#     # Get scroll height
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     while True:
#         # Scroll down to bottom
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#         # Wait to load page
#         time.sleep(SCROLL_PAUSE_TIME)
#
#         # Calculate new scroll height and compare with last scroll height
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height
#
#     price = driver.find_elements_by_class_name('uiButtonConfirm')
#     price.click()
#     # driver.find_elements_by_class_name('recaptcha-checkbox-border').click()
#     # price.click()
#     time.sleep(10)
#     counter = 0
#     for post in price:
#         print(post.text)
#         counter += 1
#
#     driver.close()
#     print("counter======>" + str(counter))
# except:
#     driver.close()
#     print("invalid arguments OR No lyrics found on page")


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

chrome_path = "chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('https://www.facebook.com')
print("Opened facebook...")
a = driver.find_element_by_id('email')
a.send_keys('03317775080')
print("Email Id entered...")
b = driver.find_element_by_id('pass')
b.send_keys('942722')
print("Password entered...")
c = driver.find_element_by_id('loginbutton')
c.click()
# driver.get("https://www.facebook.com/groups/1040612819352699/")
# post_box = driver.find_element_by_xpath("//*[@name='xhpc_message']")
# post_box.click()
# post_box.send_keys("Testing using Name not ID.Selenium is easy.")



# a=driver.find_elements_by_class_name('see_more_link_inner')
# a[0].click()
text = driver.find_elements_by_class_name('_5wj-')
print(text[0].text)
sleep(2)
# post_it = driver.find_element_by_xpath("//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
# post_it.click()
print("Posted...")


