from time import sleep

from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
# driver.get('https://www.google.com/')
# print(driver.page_source)
driver.implicitly_wait(3)
driver.get("https://jumpstory.com/remove-background/")
sleep(2)
# temp = driver.find_elements_by_xpath('//*[@id="page-content"]/div[1]/div/div/div[1]/div/div[1]')

file=driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/p[1]/label/input').send_keys(os.getcwd()+'/beautiful-1274361_1920.jpg')
# file.send_keys('1.jpg')
sleep(3)
driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/button[1]').click()
sleep(10)
driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/a/span').click()
sleep(4)
print("Successful")
driver.close()
