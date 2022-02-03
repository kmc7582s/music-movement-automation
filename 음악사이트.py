from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip

driver = webdriver.Chrome()
driver.get('https://stackoverflow.com/')
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
time.sleep(0.5)
driver.find_element_by_id('identifierId').send_keys('')
driver.find_element_by_xpath(
    '//*[@id="identifierNext"]/div/button/div[2]').click()
time.sleep(2)

driver.find_element_by_xpath(
    '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('')
driver.find_element_by_xpath(
    '//*[@id="passwordNext"]/div/button/div[2]').click()
time.sleep(2)

driver.get('https://music.youtube.com/')
time.sleep(2)


# url = "https://accounts.google.com/"
# browser = webdriver.Chrome("c:/chromedriver.exe")
# browser.implicitly_wait(5)
# browser.maximize_window()
# browser.get(url)


