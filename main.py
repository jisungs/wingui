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
window_after = browser.window_handles[1]
browser.switch_to.window(window_after)
browser.maximize_window()

try:
    myElem2 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'rootmenu')))
    billOnProgress = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[onclick^=''경비입력중'']")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")





try:
    myElem3 = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, '52282:20018:86580:0')))
    # billOnProgress = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[onclick^=''경비입력중'']")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

#----#

# br.find_element_by_css_selector("a[onclick^='fastener']").click()
# import PIL
# import cv2
# import numpy
#
# img = cv2.imread('Z:/기본업무/component/root_menu.jpg')
#
# root_menu = pyautogui.locateCenterOnScreen(img)
# pyautogui.click(root_menu)
# print(pyautogui.position())
#기본담보 조회 클릭
# pyautogui.click(x=1223, y=719)
# pyautogui.click(x=151, y=429)
# # erP  경고창 제거 클릭
# pyautogui.click(x=432, y=604)
# pyautogui.click(x=773, y=601)

# point = pyautogui.position()

# pyautogui.screenshot('1.png', region=(281, 147, 30,30))

# num1 = pyautogui.locateCenterOnScreen('1.png')
#
# pyautogui.click()
