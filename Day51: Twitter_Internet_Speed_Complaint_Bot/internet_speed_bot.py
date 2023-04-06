from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

PROMISED_DOWN = 500
PROMISED_UP = 500
TWITTER_EMAIL = os.environ['TWITTER_EMAIL']
TWITTER_PW = os.environ['TWITTER_PW']


class InternetSpeedTwitterBot:

    def __init__(self):

        self.opts = webdriver.ChromeOptions()
        self.service = Service("C:\Development\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service, options=self.opts)
        self.download_val = None
        self.upload_val = None

    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.XPATH, '//*[@aria-label = "start speed test - connection type multi"]')
        go_button.click()
        time.sleep(50)
        self.download_val = round(float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text))
        self.upload_val = round(float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text))

    def tweet_at_provider(self):

        self.driver.get("https://twitter.com/home")
        time.sleep(5)
        user_input = self.driver.find_element(By.XPATH, '//*[@autocomplete = "username"]')
        user_input.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, '//*[text() = "Next"]')
        next_button.click()
        time.sleep(1)
        pw_input = self.driver.find_element(By.XPATH, '//*[@autocomplete = "current-password"]')
        pw_input.send_keys(TWITTER_PW)
        time.sleep(1)
        login_button = self.driver.find_element(By.XPATH, '//*[text() = "Log in"]')
        login_button.click()
        time.sleep(5)
        tweet_box = self.driver.find_element(By.XPATH, '//*[@aria-label = "Tweet text"]')
        tweet_box.click()
        tweet_box.send_keys(f"Hey ISP, why is my internet speed {self.download_val}down/{self.upload_val}up "
                            f"when it should be {PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet_button = self.driver.find_element(By.XPATH, '//*[@data-testid = "tweetButtonInline"]')
        tweet_button.click()
        time.sleep(1000)
        self.driver.quit()
