import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

form_url = os.environ['FORM_URL']
zillow_url = os.environ['ZILLOW_URL']

driver.get(zillow_url)
time.sleep(4)

results = driver.find_elements(By.CLASS_NAME, "jhnswL")

addr_list = []
price_list = []
link_list = []

for i in results:
    try:
        addr_list.append(i.find_element(By.CSS_SELECTOR, 'a').text)
        price_list.append(re.sub("[^0-9]", "", i.find_element(By.CSS_SELECTOR, 'span').text))
        link_list.append(i.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'))
    except NoSuchElementException:
        pass

driver.get(form_url)

time.sleep(2)

for i in range(0, len(addr_list) - 1):

    question_list = driver.find_elements(By.CLASS_NAME, "whsOnd")

    addr_question = question_list[0]
    price_question = question_list[1]
    link_question = question_list[2]

    addr_question.send_keys(addr_list[i])
    price_question.send_keys(price_list[i])
    link_question.send_keys(link_list[i])

    submit_button = driver.find_element(By.XPATH, '//*[text()="Submit"]')
    submit_button.click()

    time.sleep(1)

    try:
        sar_button = driver.find_element(By.XPATH, '//*[text()="Submit another response"]')
        sar_button.click()

    except NoSuchElementException:
        print(f"Can't find button at {sar_button.get_attribute('href')}")

    time.sleep(2)

print(f"Load complete.\nRecords entered: {len(addr_list)}")

driver.quit()




