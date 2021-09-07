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
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/div[1]/div/ul/li[2]/a")))
    element.click()
    time.sleep(1)
    hover = ActionChains(driver).move_to_element(driver.find_element_by_class_name('product-surface'))
    hover.perform() #除了時尚服飾
    # hover = ActionChains(driver).move_to_element(driver.find_element_by_class_name('square-wrapper'))
    # hover.perform() #時尚服飾
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'product-surface-button-wrapper')))
    element.click() #除了時尚服飾
    # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'fashionProductBriefButton')))
    # element.click() #時尚服飾
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'qtyInputBox')))
    element.clear()
    time.sleep(1)
    element.send_keys('99')
    element.send_keys('\ue007')
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'addToCartButton')))
    element.click()
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cboxClose')))
    element.click()
except:
    'driver.quit()'