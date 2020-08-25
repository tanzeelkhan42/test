from time import sleep
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import cv2
import numpy as np

import cv2
import numpy as np
from PIL import Image


def IMAGE_CROP():
    im = Image.open("resized_beautiful-1274361_1920.png")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    bg.paste(im, im)
    bg.save("image.jpg") # os.remove('image.png')
    img = cv2.imread('image.jpg')
    ## (1) Convert to gray, and threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    ## (2) Morph-op to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)
    ## (3) Find the max-area contour
    cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cnt = sorted(cnts, key=cv2.contourArea)[-1]
    ## (4) Crop and save it
    x, y, w, h = cv2.boundingRect(cnt)
    dst = img[y:y + h, x:x + w]
    cv2.imwrite("103.png", dst)

    img = Image.open('103.png')
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save("image.png", "PNG")
IMAGE_CROP()

def centerImg():
    img = cv2.imread('beautiful-1274361_1920.jpg')
    ## (1) Convert to gray, and threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    ## (2) Morph-op to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

    ## (3) Find the max-area contour
    cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    cnt = sorted(cnts, key=cv2.contourArea)[-1]

    ## (4) Crop and save it
    x, y, w, h = cv2.boundingRect(cnt)
    dst = img[y:y + h, x:x + w]
    cv2.imwrite("bilL.png", dst)

# centerImg()

options = Options()
prefs = {"download.default_directory": str(os.getcwd())}
options.add_experimental_option("prefs", prefs)

options.add_argument("--disable-notifications")
chrome_path = "chromedriver.exe"

driver = webdriver.Chrome(chrome_path, chrome_options=options)
driver.implicitly_wait(3)
driver.get("https://jumpstory.com/remove-background/")
# sleep(2)
# temp = driver.find_elements_by_xpath('//*[@id="page-content"]/div[1]/div/div/div[1]/div/div[1]')


WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               '//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/p[1]/label/input')))

file = driver.find_element_by_xpath(
    '//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/p[1]/label/input').send_keys(
    os.getcwd() + '/resized_beautiful-1274361_1920.jpg')
# file.send_keys('1.jpg')
print("file uploaded")
# sleep(10)
element = driver.find_element_by_class_name("elementor-button-wrapper")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# sleep(3)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                            '#content > div > div > div > section.elementor-element.elementor-element-aac8557.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default.elementor-section.elementor-top-section > div > div > div > div > div > div > div > div > div > div > div > button.btn.btn-blue'))).click()

print("file bg removing")
wait = WebDriverWait(driver, 30)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/a/span')))
element.click()
print("file bg downloaded")
print("successful")
# centerImg()
# sleep(10)
# driver.close()
IMAGE_CROP()