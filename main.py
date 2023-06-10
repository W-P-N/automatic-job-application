from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as t

# Constants
url = '<linked in url> '
username = '<mailid>'
password = '<password>'
phone = '<phone>'
# Code body
service = Service("C:/Users/HP/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url)
# Click sign in button
sign_in_but = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in_but.click()
# Wait for page to load
t.sleep(5)
# Enter details
ent_username = driver.find_element(By.XPATH, '//*[@id="username"]')
ent_username.send_keys(username)
ent_pass = driver.find_element(By.XPATH, '//*[@id="password"]')
ent_pass.send_keys(password)
# Click sign-in button
sign_in_but_ = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_but_.click()
# CLick easy apply
apply = driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')
apply.click()
t.sleep(3)
# Catch phone number element and enter
phn_number = driver.find_element(By.CLASS_NAME, 'fb-single-line-text__input')
if phn_number == "":
    phn_number.send_keys(phone)
# Submit the application
submit_button = driver.find_element(By.CSS_SELECTOR, 'footer button')
submit_button.click()
