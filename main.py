
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time


browser = webdriver.Ie('C:/Users/111237/PycharmProjects/wingui/IEDriverServer.exe')
# browser.get('https://www.naver.com/')
browser.get('http://ep.hitejinro.com/')
browser.maximize_window()

delay = 15 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'pt_top_aprv1')))
    scp = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'quick-s46')))
    erp = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'quick-s18')))
    ebill = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'quick-s33')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

erp.click()

window_before = browser.window_handles[0]

time.sleep(2)

window_after = browser.window_handles[1]

browser.switch_to.window(window_after)

browser.maximize_window()

time.sleep(5)



# try:
#     # root_elem = WebDriverWait(browser, delay).until(EC.presence_of_element_located(By.ID, "52282:20018:-1:0"))
#     root_elem = browser.find_element_by_class_name("rootmenu")
#     print("erp page in ready")
# except TimeoutException:
#     print("Loading took too much time!")
#
# time.sleep(2)

import pyautogui

pyautogui.moveTo(119,276)
pyautogui.click()

time.sleep(2)

pyautogui.moveTo(140,495)
pyautogui.click()

time.sleep(2)

pyautogui.moveTo(137,513)
pyautogui.click()

time.sleep(4)

pyautogui.moveTo(562,602)
pyautogui.click()

time.sleep(2)

pyautogui.moveTo(775,602)
pyautogui.click()

time.sleep(9)
pyautogui.moveTo(562,602)
pyautogui.click()

time.sleep(2)

pyautogui.moveTo(775,602)
pyautogui.click()

time.sleep(9)

pyautogui.moveTo(115,166)
pyautogui.click()
pyautogui.write("10")
pyautogui.press("enter")

pyautogui.moveTo(126, 203)
pyautogui.click()
pyautogui.write("114580")
pyautogui.press("enter")

pyautogui.moveTo(146, 270)
pyautogui.click()

pyautogui.moveTo(212, 271)
pyautogui.click()


time.sleep(2)
pyautogui.moveTo(572, 515)
pyautogui.doubleClick()

pyautogui.moveTo(74, 123)
pyautogui.click()

pyautogui.moveTo(235, 220)
pyautogui.click()

pyautogui.moveTo(331, 220)
pyautogui.click()

time.sleep(2)
pyautogui.moveTo(522, 573)
pyautogui.click()
pyautogui.write("4")
pyautogui.press("enter")
pyautogui.press("enter")

time.sleep(3)


#input item

def next_line():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('f')
    pyautogui.keyDown('n')
    pyautogui.keyUp('n')
    pyautogui.keyUp('f')
    pyautogui.keyUp('alt')

def input_item(item_num, count):
    pyautogui.write(item_num)
    time.sleep(2)
    pyautogui.press("enter")
    pyautogui.write(count)

pyautogui.moveTo(130,380)
pyautogui.click()

input_item("10310981", "10")
next_line()

time.sleep(3)

input_item("10310981", "10")
next_line()

time.sleep(2)

input_item("10310981", "10")
next_line()

#
# pyautogui.moveTo(130,380)
# pyautogui.click()
# pyautogui.write("10310981")
# time.sleep(2)
# pyautogui.press("enter")
# pyautogui.write("10")
