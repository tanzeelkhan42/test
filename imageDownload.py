from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_path = "chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.implicitly_wait(3)
driver.get("https://jumpstory.com/remove-background/")
sleep(2)
# temp = driver.find_elements_by_xpath('//*[@id="page-content"]/div[1]/div/div/div[1]/div/div[1]')

file=driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/p[1]/label/input').send_keys(r'C:\Users\TanzeelKhan\PycharmProjects\dynamicCrawl\beautiful-1274361_1920.jpg')
# file.send_keys('1.jpg')
sleep(3)
driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/button[1]').click()
sleep(10)
driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/a/span').click()
sleep(4)
driver.close()
