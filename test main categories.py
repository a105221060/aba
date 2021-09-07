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
    for number in range(2, 15):
        if number ==10:
            continue
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[4]/ul/li[{}]'.format(number))))
        element.click()
        count = driver.find_elements_by_xpath('//*[@id="subnav"]/ul/li')
        print(len(count))
        for number1 in range(1,len(count)+1):
            hover = ActionChains(driver).move_to_element(driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div[1]/div/ul/li[{}]/a'.format(number1)))
            print('/html/body/div[1]/div[1]/div[5]/div/div[1]/div/ul/li[{}]/a'.format(number1))
            hover.perform()
            time.sleep(1)
except:
    'driver.quit()'