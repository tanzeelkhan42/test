from time import sleep

import base64
import os
from flask import Flask, render_template, request, send_from_directory
# from werkzeug import secure_filename
from selenium import webdriver
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64

app = Flask(__name__)


def convert_base64_to_image(base_64):
    imgdata = base64.b64decode(base_64)
    # I assume you have a way of picking unique filenames
    with open(os.getcwd() + '/image.jpg', 'wb') as f:
        f.write(imgdata)


def convert_base64_to_image2(base_64):
    imgdata = base64.b64decode(base_64)
    # I assume you have a way of picking unique filenames
    with open(os.getcwd() + '/image.png', 'wb') as f:
        f.write(imgdata)


def convert_image_into_hexa():
    with open("image.png", "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
    os.remove('image.png')
    return my_string


@app.route('/', methods=['GET'])
def fun():
    return {'message': "Hello from flask"}


@app.route('/img/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            base_64 = str(request.form["image"])
            chrome_options = webdriver.ChromeOptions()
            prefs = {"download.default_directory": str(os.getcwd())}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
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
            os.remove(os.getcwd() + '/image.jpg')
            base_64_output = convert_image_into_hexa()
            # convert_base64_to_image2(str(base_64_output)[2:])
            return {'status': '1', 'response': str(base_64_output)[2:]}

        except Exception as e:
            print(e)
            return {'status': '0', 'response': str(e)}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
