import self as self
from selenium import webdriver
import sys
import time
import csv
import pandas as pd
from googletrans import Translator

#
from selenium.webdriver.chrome.options import Options

header = ['Title', 'Price', 'colors', 'Volume', 'styles', 'Sizes', 'Description', 'Brand', 'images']
# writer.writerow(row)
try:
    csfile_open = open('Home&Lifestyle_bedroom_furniture_Products.csv', 'a')
    writer = csv.writer(csfile_open)
    writer.writerow(header)
    csfile_open.close()
    chrome_path = "chromedriver.exe"
    # browser = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Chrome(chrome_path)
    # baseUrl = 'https://www.tripadvisor.com'
    urlClasList = []
    df = pd.read_csv('Mobile_Product.csv')
    linkList = df['Links'].tolist()

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
    for k in range(len(linkList)):
        try:
            driver.get(linkList[k])
            print(linkList[k])
            translator = Translator()
            title = driver.find_element_by_class_name('pdp-mod-product-badge-title')
            engTitle = translator.translate(title.text, dest='en')
            title = engTitle.text
            price = driver.find_element_by_class_name('pdp-product-price')
            price = price.text
            description = driver.find_element_by_class_name('pdp-product-detail')
            engDesc = translator.translate(description.text, dest='en')
            description = engDesc.text
            brand = driver.find_element_by_class_name('pdp-product-brand__brand-link')
            engBrand = translator.translate(brand.text, dest='en')
            brand = engBrand.text
            img = driver.find_elements_by_class_name('item-gallery')
            img_src = ''
            GalleryList = []
            for i in img:
                imgsList = i.find_elements_by_tag_name('img')
                for j in imgsList:
                    GalleryList.append(j.get_attribute('src'))
            rows = driver.find_elements_by_class_name('sku-prop')
            num = len(rows)
            color = ''
            volume = []
            style = ''
            size = []
            translator = Translator()
            for index in rows:
                content = index.find_element_by_class_name('section-title')
                content = translator.translate(content.text, dest='en')
                if 'color' in str(content.text).lower():
                    colorTemp = index.find_element_by_class_name('sku-name')
                    colorTemp = translator.translate(colorTemp.text, dest='en')
                    color = colorTemp.text
                if 'style' in str(content.text).lower():
                    styleTemp = index.find_element_by_class_name('sku-name')
                    style = style.text
                if 'volume' in str(content.text).lower():
                    volumeTemp = index.find_element_by_class_name('sku-prop-content')
                    span = volumeTemp.find_elements_by_tag_name('span')
                    for title in span:
                        text = title.get_attribute('title')
                        volume.append(text)
                if 'size' in str(content.text).lower():
                    sizeTemp = index.find_element_by_class_name('sku-prop-content')
                    span = sizeTemp.find_elements_by_tag_name('span')
                    for title in span:
                        text = title.get_attribute('title')
                        size.append(text)
            rowList = [str(title), str(price), str(color), str(volume), str(style), str(size),
                       str(description),
                       str(brand), str(GalleryList)]
            # print(rowList)
            print(linkList[k]+'-------------------- done')
            with open('Home&Lifestyle_bedroom_furniture_Products.csv', 'a', newline='') as f:
                w = csv.writer(f)
                w.writerow(rowList)
                f.close()
            # time.sleep(100)
            print('------------------------------index--------------------------'+str(k))
        except Exception as e:
            #print(str(index))
            continue

except Exception as e:
    print(e)
