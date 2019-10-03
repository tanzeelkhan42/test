from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

try:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)
    driver.get('https://www.yellowpages.com.au/search/listings?clue=Panel+Beater&eventType=pagination&locationClue=sydney+eastern+suburbs+nsw&pageNumber=7&referredBy=www.yellowpages.com.au')

    # driver.find_element_by_class_name("pSO8Ic").click()

    price = driver.find_elements_by_class_name('listing-heading')

    i = 1
    print('\n')
    for post in price:
        if (':' or '/') in post.text:
            break
        if (i > 2):
            print(post.text)
        i += 1

    driver.quit()

except:

    driver.quit()
    print("invalid arguments OR No lyrics found on page")
