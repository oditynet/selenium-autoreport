from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time

project='J001'

now = datetime.now()
#now = now + timedelta(days=9) # for future (test)
get=now
wdatnow = datetime.weekday(now)
if (now.day > wdatnow):
   get = now-timedelta(days=wdatnow)
   get=get.date()

driver = webdriver.Firefox()
driver.get(f"https://site.ru/TS/Edit.aspx?empid=13825&date={get}")

pyautogui.write('username') # Логин
pyautogui.press('tab')        # Tab
pyautogui.write('apss') # Пароль
pyautogui.press('enter')      # Enter
driver.get(f"https://site.ru/TS/Edit.aspx?empid=13825&date={get}")

#all = driver.find_element(By.ID, 'SendApprove').click()
#pyautogui.press('enter')      # Enter

add = driver.find_element(By.ID, 'newItemControl')
add = add.send_keys(project)
time.sleep(1)

pyautogui.press('enter')      # Enter

w1 = driver.find_element(By.ID, 'newItemControl_wl0')
w1.send_keys('8')

w2 = driver.find_element(By.ID, 'newItemControl_wl1')
w2.send_keys('8')

w3 = driver.find_element(By.ID, 'newItemControl_wl2')
w3.send_keys('8')

w4 = driver.find_element(By.ID, 'newItemControl_wl3')
w4.send_keys('8')

w5 = driver.find_element(By.ID, 'newItemControl_wl4')
w5.send_keys('8')

all = driver.find_element(By.ID, 'AddButton2').click()
pyautogui.press('enter')      # Enter
