from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os

LINKEDIN_USER = os.environ['LINKEDIN_USER']
LINKEDIN_PW = os.environ['LINKEDIN_PW']

opts = webdriver.ChromeOptions()
opts.add_argument("--start-maximized")
service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=opts)

driver.get("https://www.linkedin.com/jobs/")

driver.find_element(By.ID, "session_key").send_keys(LINKEDIN_USER)
driver.find_element(By.ID, "session_password").send_keys(LINKEDIN_PW)
driver.find_element(By.CLASS_NAME, "sign-in-form__submit-btn--full-width").click()

# Sleep time here is long in the case of a captcha
time.sleep(15)

# Searching for jobs using JOB_KEYWORD on LinkedIn
JOB_KEYWORD = "python developer"
job_search = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
job_search.click()
job_search.send_keys(JOB_KEYWORD)
time.sleep(2)
job_search.send_keys(Keys.ENTER)

time.sleep(3)

# Selecting the Easy Apply filtering option
filter_button = driver.find_element(By.XPATH, '//*[text()="Easy Apply"]')
filter_button.click()

time.sleep(3)

# Creating a list of available jobs on the webpage
job_apply = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")

# Applying to each job 1 by 1
for i in job_apply:

    text = i.find_element(By.CLASS_NAME, "job-card-list__title").text
    i.click()

    time.sleep(1)

    # Click Easy Apply button
    try:
        apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        time.sleep(3)
        apply_button.click()
        time.sleep(1)
    except:
        print("Job has been closed or unlisted")

    # Attempt to instantly submit, if we can't then we try to hit Next once to see if we can get away with applying
    # without filling any info out
    try:
        submit_button = driver.find_element(By.XPATH, '// *[ @ aria-label = "Submit application"]')
        submit_button.click()
        time.sleep(1)

        done_button = driver.find_element(By.XPATH, '// *[text()= "Done"]')
        done_button.click()

    except NoSuchElementException:

        try:
            next_button = driver.find_element(By.XPATH, '// *[ @ aria-label = "Continue to next step"]')
            next_button.click()
            time.sleep(2)
            review_button = driver.find_element(By.XPATH, '// *[ @ aria-label = "Review your application"]')
            review_button.click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            secondary_submit_button = driver.find_element(By.XPATH, '// *[ @ aria-label = "Submit application"]')
            secondary_submit_button.click()

        except NoSuchElementException:

            print("Too in-depth. Saving this application and moving to the next...")
            close_button = driver.find_element(By.XPATH, '// *[ @ aria-label = "Dismiss"]')
            close_button.click()
            time.sleep(1)
            save_button = driver.find_element(By.XPATH, '// *[ @ data-control-name = "save_application_btn"]')
            save_button.click()

driver.quit()

