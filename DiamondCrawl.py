from selenium import webdriver
import sys
import time

# www.adiamor.com

try:
    chrome_path = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get(
        'https://www.adiamor.com/Diamonds/Search/Princess')

    priceLow = driver.find_element_by_class_name("low").clear()
    priceLow = driver.find_element_by_class_name("low")
    priceLow.send_keys('300')

    priceHigh = driver.find_element_by_class_name("high").clear()
    priceHigh = driver.find_element_by_class_name("high")
    priceHigh.send_keys('5000')
    driver.find_element_by_class_name("jumbotron").click()

    driver.implicitly_wait(20)

    i = 0
    while i < 20:
        driver.find_element_by_class_name("show-next-page").click()
        driver.implicitly_wait(10)
        i += 1

    price = driver.find_elements_by_class_name('diamond-row')

    counter=0
    for post in price:
        counter+=1
        print(post.text)
    print(counter)
    driver.close()
except:
    driver.close()
    print("invalid arguments OR No lyrics found on page")
