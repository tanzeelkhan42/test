import csv

import self as self
from selenium import webdriver
import sys
import time

#
i = 69
try:
    chrome_path = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    # baseUrl = 'https://www.tripadvisor.com'

    while i < 103:
        driver.get(
            'https://www.lazada.co.th/shop-living-room-furniture/?page=' + str(
                i) + '&spm=a2o4m.pdp.cate_7_1.2.5c9642f3GzHRX8')

        row = driver.find_elements_by_class_name('c5TXIP')
        num = len(row)
        for page in row:
            tag = page.find_elements_by_tag_name('a')
            linkList = []
            link = tag[0].get_attribute('href')
            print(tag[0].get_attribute('href'))
            linkList.append(link)
            print('------------------------------')
            with open('Home&Lifestyle_living.csv', 'a', encoding='utf-8') as f:
                w = csv.writer(f)
                w.writerow(linkList)
                f.close()

        print("Total Records:::", num)
        i += 1
        print(i)
        time.sleep(70)
except:
    print(i)
    driver.close()
    print("invalid arguments OR No lyrics found on page")
