import datetime
import os

import allure
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utilities import configReader
from utilities.util_helper import UtilHelper


def before_all(context):
    url = context.config.userdata.get('url')
    browser = context.config.userdata.get('browser')
    headless = context.config.userdata.get('headless')
    if url is None:
        context.url = configReader.readConfig('basic info', 'test_site_url').lower().strip()
    else:
        context.url = url
    if browser is None:
        context.browser = configReader.readConfig('basic info', 'browser').lower().strip()
    else:
        context.browser = browser

    if headless is None:
        context.headless = configReader.readConfig('basic info', 'headless').lower().strip()
    else:
        context.headless = headless

    os.environ['browser'] = context.browser
    print(f'BROWSER: {context.browser} | HEADLESS: {context.headless} | URL: {context.url}')


def before_scenario(context, driver):
    run_type = configReader.readConfig('basic info', 'run_type').lower().strip()
    selenium_hub_url = 'http://localhost:4444/hub'

    if context.browser == 'chrome':
        chrome_options = ChromeOptions()

        """"--disable-dev-shm-usage" Only added when CI system environment variable is set 
        or when inside a docker instance. The /dev/shm partition is too small in certain VM environments, 
        causing Chrome to fail or crash.
        It overcomes the limited resources problem
        """
        chrome_options.add_argument('--disable-dev-shm-usage')  # overcomes the limited resources problem
        chrome_options.add_argument('--no-sandbox')  # Bypass OS security model

        if context.headless == 'true':
            chrome_options.headless = True
        elif context.headless == 'false':
            chrome_options.headless = False

        if run_type == 'remote':
            context.driver = webdriver.Remote(command_executor=selenium_hub_url,
                                              desired_capabilities=DesiredCapabilities.CHROME, options=chrome_options)
        else:
            context.driver = webdriver.Chrome(ChromeDriverManager(version="111.0.5563.64").install(), chrome_options=chrome_options)
            # context.driver = webdriver.Chrome(options=chrome_options)
            # context.driver = WebDriver(options=chrome_options)

    if context.browser == 'firefox':
        firefox_options = FirefoxOptions()
        if context.headless == 'true':
            firefox_options.headless = True
        elif context.headless == 'false':
            firefox_options.headless = False

        if run_type == 'remote':
            context.driver = webdriver.Remote(command_executor=selenium_hub_url,
                                              desired_capabilities=DesiredCapabilities.FIREFOX, options=firefox_options)
        else:
            context.driver = webdriver.Firefox(options=firefox_options)
    context.driver.get(context.url)


def after_step(context, step):
    print()
    report_name = 'error_screenshot_' + str(datetime.datetime.now()) + '_' + UtilHelper.get_random_string_with_uuid()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name=report_name,
                      attachment_type=allure.attachment_type.PNG)


def after_scenario(context, driver):
    context.driver.quit()
