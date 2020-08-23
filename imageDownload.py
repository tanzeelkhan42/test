from time import sleep
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

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
    os.getcwd() + '/resized_image-fashion-3080644.jpg')
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
# sleep(10)
# driver.close()
