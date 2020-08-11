import csv
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

try:
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome()
    chrome_path = "chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    count = 1
    while count < 138:

        driver.get('https://wallmine.com/screener?d=d&nd=730&o=m&page=' + str(count) + '&r=n&s=AAPL&symbols=AAPL')
        time.sleep(10)
        # driver.find_element_by_class_name("pSO8Ic").click()

        body = driver.find_elements_by_tag_name('tbody')
        rows = body[0].find_elements_by_tag_name('tr')
        text = ''
        for i in range(len(rows)):
            # temp = driver.find_elements_by_xpath('/html/body/main/section/div[4]/div/div[2]/div/table/tbody/tr[1]/th')
            try:
                temp2 = rows[i].find_elements_by_tag_name('th')
                temp3 = rows[i].find_elements_by_tag_name('td')
                if len(temp2) == 1:
                    text = temp2[0].text
                elif len(temp3):
                    symbol = temp3[0].text
                    title = temp3[1].text
                    source = temp3[2].text
                    print(text)
                    with open('waalmineNewsAgain.csv', 'a', newline='', encoding='utf-8') as f:
                        rowList = [text, symbol, title, source]
                        tempDic = []
                        w = csv.writer(f)
                        w.writerow(rowList)
                        f.close()

            except:
                continue

        count = count + 1

    driver.quit()

except:

    driver.quit()
    print("invalid arguments OR No lyrics found on page")
