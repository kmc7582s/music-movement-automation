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
id = browser.find_element_by_css_selector("#email")
id.click()
pyperclip.copy("아이디")
pyautogui.hotkey("ctrl","v")
time.sleep(1)

#PW
pw = browser.find_element_by_css_selector("#password")
pw.click()
pyperclip.copy("비밀번호")
pyautogui.hotkey("ctrl","v")
time.sleep(1)

#login button
login_btn = browser.find_element_by_css_selector("#btnSubmitSignin")
login_btn.click()
time.sleep(1)

#플레이리스트로 이동
browser.get("https://www.music-flo.com/storage/mylist")
time.sleep(1)

#플레이리스트 복사

