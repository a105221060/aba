from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

driver.get("https://accstorefront.csz8zfle01-shoaltert1-d1-public.model-t.cc.commerce.ondemand.com/zh")
driver.maximize_window()

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"btnCloseLarge" )))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "bannerTopCloseButton")))
    element.click()
    time.sleep(2)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'SuggestionSearch-input')))
    element.send_keys('大街市')
    element.send_keys('\ue007')
except:
    'driver.quit()'