import pyautogui
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


browser = webdriver.Ie('C:/Users/111237/PycharmProjects/wingui/IEDriverServer.exe')
# browser.get('https://www.naver.com/')
browser.get('http://ep.hitejinro.com/')
browser.maximize_window()

delay = 10 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'pt_top_aprv1')))
    scp = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'quick-s46')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")


# print(pyautogui.position())

# point = pyautogui.position()

# pyautogui.screenshot('1.png', region=(281, 147, 30,30))

# num1 = pyautogui.locateCenterOnScreen('1.png')
#
# pyautogui.click()
