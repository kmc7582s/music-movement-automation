from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip

url = "https://www.music-flo.com/member/singin"
browser = webdriver.Chrome("c:/chromedriver.exe")
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

#ID
id = browser.find_element_by_css_selector("#id")
id.click()
pyperclip.copy("아이디")
pyautogui.hotkey("ctrl","v")
time.sleep(1)

#PW


