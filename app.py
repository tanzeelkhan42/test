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

app = Flask(__name__)


@app.route('/', methods=['GET'])
def fun():
    return {'message': "Hello from flask"}


@app.route('/img/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                                      chrome_options=chrome_options)
            # driver.implicitly_wait(3)
            driver.get("https://jumpstory.com/remove-background/")

            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                            '//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/p[1]/label/input')))

            file = driver.find_element_by_xpath(
                '//*[@id="content"]/div/div/div/section[3]/div/div/div/div/div/div/div/div/div/div/div/p[1]/label/input').send_keys(
                os.getcwd() + '/beautiful-1274361_1920.jpg')
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

            return {'status': 'ok'}

        except Exception as e:
            print(e)
            return {'status': 'failed'}


if __name__ == '__main__':
    app.run(debug=True)
