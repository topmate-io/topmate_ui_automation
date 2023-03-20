import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


def wait_for_element_to_be_visible(driver, locator_name: str, time_out: int):
    element = WebDriverWait(driver, time_out).until(
        expected_conditions.visibility_of_element_located((By.ID, locator_name)))
    return element

chrome_options = ChromeOptions()
chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)

# chrome_options = ChromeOptions()
# chrome_options.headless = False
service_obj = ChromeService(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(10)

driver.get('https://staging2.topmate.io/')
driver.implicitly_wait(5)
login_button = driver.find_element(By.CSS_SELECTOR, '.btn-login')
print('login: ', login_button.text)
login_button.click()

# driver.find_element(By.ID, 'LoginForm_loginId').send_keys('automate_topmate')
wait_for_element_to_be_visible(driver, 'LoginForm_loginId', 5).send_keys('automate_topmate')
driver.find_element(By.ID, 'LoginForm_password').send_keys('123456')
driver.find_element(By.CSS_SELECTOR, '.form-submit-button').click()

time.sleep(10)
url = driver.current_url
print(driver.current_url)

driver.quit()
