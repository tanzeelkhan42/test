from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

try:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.trendsmap.com/local/united+kingdom#collapse_trends')

    # driver.find_element_by_class_name("pSO8Ic").click()

    price = driver.find_elements_by_class_name('inline-tweet-text')

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
