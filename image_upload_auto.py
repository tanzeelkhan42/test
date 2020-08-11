#
#
# import self as self
# import os
# from selenium import webdriver
# import sys
# import time
#
# #
#
# try:
#
#     chrome_path = "chromedriver.exe"
#     driver = webdriver.Chrome(chrome_path)
#     driver.implicitly_wait(15)
#     driver.get("https://www.base64-image.de/")
#     driver.find_element_by_id("drag-target-box").send_keys("1.jpg")
#     # driver.find_element_by_id("submit").click()
#
# except:
#     print('invalid')
#     driver.close()

from functools import reduce
from operator import add

li = [[1, 2], [3, 4]]
x = reduce(add, li)
print (x)