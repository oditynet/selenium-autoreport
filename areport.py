from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://site.ru/ss/Edit.aspx?empid=13825&date=2024-02-12")

pyautogui.write('username') # Логин
pyautogui.press('tab')        # Tab
pyautogui.write('pass!!!') # Пароль
pyautogui.press('enter')      # Enter
driver.get("https://site.ru/ss/Edit.aspx?empid=13825&date=2024-02-12")


all = driver.find_element(By.ID, 'SendApprove').click()

pyautogui.press('enter')      # Enter
