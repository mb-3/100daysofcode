from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os

TINDER_USER = os.environ['TINDER_USER']
TINDER_PW = os.environ['TINDER_PW']

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://tinder.com/app/recs")

time.sleep(3)

login_button = driver.find_element(By.XPATH, '//*[text()="Log in"]')
login_button.click()

time.sleep(2)

fb_login_button = driver.find_element(By.XPATH, '//*[text()="Log in with Facebook"]')
fb_login_button.click()

time.sleep(5)

tinder_handle = driver.window_handles[0]
login_handle = driver.window_handles[1]
driver.switch_to.window(login_handle)

time.sleep(1)

driver.find_element(By.ID, "email").send_keys(TINDER_USER)
driver.find_element(By.ID, "pass").send_keys(TINDER_PW)

time.sleep(1)

submit_fb_login_button = driver.find_element(By.XPATH, '//*[@name="login"]')
submit_fb_login_button.click()

time.sleep(5)

driver.switch_to.window(tinder_handle)
time.sleep(3)

driver.find_element(By.XPATH, '//*[@aria-label="Allow"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@aria-label="Not interested"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[text()="I accept"]').click()

time.sleep(5)

like_count = 0

buttons = driver.find_element(By.XPATH, '//*[@data-keyboard-gamepad="true"]').find_elements(By.XPATH, '//*[@type="button"]')

# Having a hard time pinning down the like button since there is no concrete identifier
for i in buttons:
    if i.text == 'LIKE':
        like_button = i

while like_count < 10:

    try:

        like_button.click()

    except:
        # Needed to write this in the case we're prompted with the 
        # "Would you like to add Tinder to your desktop?" question.
        try:
            btt_button = driver.find_element(By.XPATH, '//*[@title="Back to Tinder"]')
            btt_button.click()
        except NoSuchElementException:
            not_interested = driver.find_element(By.XPATH, '//*[text()="Not Interested"]')
            not_interested.click()

    time.sleep(1)

    like_count += 1

time.sleep(5)

driver.quit()
