from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os


SIMILAR_ACCOUNT = "python.hub"
IG_EMAIL = os.environ['IG_EMAIL']
IG_PW = os.environ['IG_PW']


class InstaFollower:

    def __init__(self):

        self.follower_list = None
        self.opts = webdriver.ChromeOptions()
        self.service = Service("C:\Development\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service, options=self.opts)

    def login(self):

        self.driver.get("https://www.instagram.com/")
        time.sleep(5)

        self.driver.find_element(By.XPATH, '//*[@name="username"]').send_keys(IG_EMAIL)
        self.driver.find_element(By.XPATH, '//*[@name="password"]').send_keys(IG_PW)

        self.driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        time.sleep(10)

    def find_followers(self):

        self.driver.find_element(By.XPATH, '//*[@aria-label="Search"]').click()
        search_bar = self.driver.find_element(By.XPATH, '//*[@aria-label="Search input"]')
        search_bar.send_keys(SIMILAR_ACCOUNT)
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        # Open followers window
        self.driver.find_element(By.XPATH, '//*[text()=" followers"]').click()
        time.sleep(1)

        self.follower_list = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div').find_elements(By.XPATH, '//*[@role="button"]')

    def follow(self):

        for i in self.follower_list:
            try:
                follow_button = i.find_element(By.XPATH, '//*[@type="button"]')
                follow_button.click()
                time.sleep(1)

            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
