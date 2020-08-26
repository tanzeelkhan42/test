from time import sleep

import base64
import os

from PIL import Image
from flask import Flask, render_template, request, send_from_directory, flash
# from werkzeug import secure_filename
from selenium import webdriver
import os
import cv2
import numpy as np
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)

# app.config['downloaded'] = os.getcwd() + ''
app.config['UPLOAD_FOLDER'] = os.getcwd() + '/UPLOAD_FOLDER'


def convert_base64_to_image(base_64):
    if os.path.exists(os.getcwd() + '/image.jpg'):
        os.remove(os.getcwd() + '/image.jpg')
    imgdata = base64.b64decode(base_64)
    # I assume you have a way of picking unique filenames
    with open(os.getcwd() + '/image.jpg', 'wb') as f:
        f.write(imgdata)


def convert_base64_to_image2(base_64):
    os.remove(os.getcwd() + '/image.png')
    imgdata = base64.b64decode(base_64)
    # I assume you have a way of picking unique filenames
    with open(os.getcwd() + '/image.png', 'wb') as f:
        f.write(imgdata)


def centerImg():

    img = cv2.imread('image.png')
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
    os.remove('image.png')
    cv2.imwrite("image.png", dst)


def convert_image_into_hexa():

    with open(os.getcwd() + "/image.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())


    return my_string


def IMAGE_CROP():
    im = Image.open(os.getcwd()+"/image.png")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    bg.paste(im, im)
    bg.save(os.getcwd()+"/image.jpg") # os.remove('image.png')
    img = cv2.imread(os.getcwd()+'/image.jpg')
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
    cv2.imwrite(os.getcwd()+"/103.png", dst)

    img = Image.open(os.getcwd()+'/103.png')
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save(os.getcwd()+"/image.png", "PNG")


@app.route('/', methods=['GET'])
def fun():
    return {'message': "Hello from flask"}


@app.route('/url/', methods=['GET'])
def download():
    app.config['DOWNLOADED'] = ''
    file = 'image.png'
    try:
        response = send_from_directory(directory=app.config['DOWNLOADED'], filename=file, as_attachment=False)
        response.headers['my-custom-header'] = 'my-custom-status-0'
        return response
    except Exception as e:
        print(e)
        print('')


@app.route('/file/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return {'status': 0, 'response': 'no file selected'}
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return {'status': 0, 'response': 'no file selected'}
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return {'status': 1, 'response': 'SUCCESSFUL'}


@app.route('/img/', methods=['GET', 'POST'])
def file():
    if request.method == 'POST':
        try:
            base_64 = str(request.form["image"])
            chrome_options = webdriver.ChromeOptions()
            prefs = {"download.default_directory": str(os.getcwd())}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            chrome_options.binary_location = os.environ.get("CHROMEDRIVER_PATH")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            convert_base64_to_image(base_64)

            driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                                      chrome_options=chrome_options)
            # driver = webdriver.Chrome(executable_path='chromedriver.exe',
            #                           chrome_options=chrome_options)

            driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

            params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': os.getcwd()}}
            command_result = driver.execute("send_command", params)
            # driver.implicitly_wait(3)
            driver.get("https://jumpstory.com/remove-background/")

            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/p[1]/label/input')))

            file = driver.find_element_by_xpath(
                '//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/p[1]/label/input').send_keys(
                os.getcwd() + '/image.jpg')
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
            element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             '//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/a/span')))
            element.click()
            print("file bg downloaded")
            print("successful")
            driver.close()
            # os.remove(os.getcwd() + '/image.jpg')
            IMAGE_CROP()
            base_64_output = convert_image_into_hexa()
            # convert_base64_to_image2(str(base_64_output)[2:])
            return {'status': '1', 'response': str(base_64_output)[2:],
                    'url': 'https://seleniumbg.herokuapp.com/url'}

        except Exception as e:
            print(e)
            return {'status': '0', 'response': str(e)}


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
