from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chromedriver_path = "chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver_path)
url = "https://www.lazada.co.th/products/-i312672563-s562516846.html?"

topics_xpath = '//*[@id="module_sku-select"]/div/div[1]/div/div/div[2]/span[1]/div/img'
states_xpath = '//*[@id="module_sku-select"]/div/div[1]/div/div/div[2]/span[3]/div/img'
browser.get(url)
WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, topics_xpath)))

browser.find_element_by_xpath(states_xpath).click()
# browser.find_element_by_xpath(states_xpath).click()