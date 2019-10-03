import self as self
from selenium import webdriver
import sys
import time

#

try:
    chrome_path = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    baseUrl = 'https://www.tripadvisor.com'
    driver.get(
        'https://avinor.no/en/airport/oslo-airport/flight-times/arrivals/')

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

    price = driver.find_elements_by_class_name('time')
    flight = driver.find_elements_by_class_name('flightNo')

    # price = driver.find_elements_by_xpath('//*[@id="ABOUT_TAB"]/div/div[2]/div[1]/div[2]/div[1]')

    num = len(price)
    for i in range(num):
        print("time: " + price[i].text)
        print("Flight number:" + flight[i].text)
        print('------------------------------')
    print("Total Records:::", num)
    # driver1 = webdriver.Chrome(chrome_path)
    # driver1.get(
    #     'https://www.tripadvisor.com/Hotels-g295424-Dubai_Emirate_of_Dubai-Hotels.html')
    #
    # elements = driver1.find_elements_by_css_selector("div.listing_title a")
    # for element in elements:
    #     print(element.get_attribute("href"))
    # counter = 0
    # # for post in price:
    # #     print(price.text)
    # #     counter += 1
    #
    # driver.close()
    # # print("counter======>" + str(counter))
except:

    driver.close()
    print("invalid arguments OR No lyrics found on page")
