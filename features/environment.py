import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from Utilities import configReader


def before_scenario(context, driver):
    if configReader.readConfig("basic info", "browser") == "chrome":
        service_obj = ChromeService(executable_path=ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service_obj)
    if configReader.readConfig("basic info", "browser") == "firefox":
        service_obj = FirefoxService(executable_path=GeckoDriverManager().install())
        context.driver = webdriver.Firefox(service=service_obj)


def after_scenario(context, driver):
    context.driver.quit()

# def after_step(context, step):
#     print()
#     if step.status == 'failed':
#         allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
#                       attachment_type=allure.attachment_type.PNG)
