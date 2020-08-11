import self as self
from selenium import webdriver
import sys
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

#

try:
    options = Options()
    prefs = {
        "translate_whitelists": {"vi": "en"},
        "translate": {"enabled": "true"}
    }
    options.add_experimental_option("prefs", prefs)
    chrome_path = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_path, chrome_options=options)
    # chrome_path = "chromedriver.exe"
    # driver = webdriver.Chrome(chrome_path)
    # baseUrl = 'https://www.tripadvisor.com'
    driver.get(
        'https://shopee.vn/-GIA-H%E1%BB%A6Y-DI%E1%BB%86T-%C3%81o-Tr%C3%B9m-Vali-%C3%81o-B%E1%BB%8Dc-Vali-Gi%C3%BAp-Ch%E1%BB%91ng-Tr%E1%BA%A7y-X%C6%B0%E1%BB%9Bc-(Ch%E1%BB%8Dn-M%C3%A0u-VS-Size)-i.13350150.965045641')

    # element = driver.find_elements_by_xpath('//*[@id="module_sku-select"]/div/div/div/div/div[2]/span[2]/div/img')
    # hov = ActionChains(element).move_to_element(element)
    # hov.perform()
    # driver.find_elements_by_class_name('_z5c42ow').click()
    # driver.find_elements_by_class_name('_72kmbi0').click()
    SCROLL_PAUSE_TIME = 2

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    row = driver.find_elements_by_class_name('shopee-product-rating__author-name')
    # row1 = driver.find_element_by_class_name('shopee-icon-button--right').click()
    # row2 = driver.find_element_by_class_name('shopee-icon-button--right').click()
    print(len(row))
    # print(row)
    # num = len(row)
    # for i in range(len(row)):
    #     # if (i == 0):
    #     # a = row[i].find_element_by_tag_name('span')
    #     print(row[i].text)
    #     # print(a.text)
    #     # if (i == 1):
    #     #     a = row[i].find_elements_by_tag_name('span')
    #     #     print(len(a))
    #     #     print(a[3].text)
    #     # print(row2[i].text)
    #     # print(temp[i].text)
    #     print('------------------------------')
    # print("Total Records:::", num)

except:

    driver.close()
    print("invalid arguments OR No lyrics found on page")
