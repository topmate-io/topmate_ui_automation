import datetime
import allure
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utilities import configReader
from utilities.util_helper import UtilHelper


def before_all(context):
    browser_type = context.config.userdata.get('browser')
    print(browser_type)
    if browser_type is None:
        context.browser_type = configReader.readConfig('basic info', 'browser').lower().strip()
    else:
        context.browser_type = browser_type


def before_scenario(context, driver):
    headless_mode = configReader.readConfig('basic info', 'headless').lower().strip()
    url = configReader.readConfig('basic info', 'test_site_url').lower().strip()
    run_type = configReader.readConfig('basic info', 'run_type').lower().strip()
    selenium_hub_url = 'http://localhost:4444/hub'

    if context.browser_type == 'chrome':
        chrome_options = ChromeOptions()
        if headless_mode == 'true':
            chrome_options.headless = True
        elif headless_mode == 'false':
            chrome_options.headless = False

        if run_type == 'local':
            context.driver = webdriver.Chrome(options=chrome_options)
        elif run_type == 'remote':
            context.driver = webdriver.Remote(command_executor=selenium_hub_url,
                                              desired_capabilities=DesiredCapabilities.CHROME, options=chrome_options)

    if context.browser_type == 'firefox':
        firefox_options = FirefoxOptions()
        if headless_mode == 'true':
            firefox_options.headless = True
        elif headless_mode == 'false':
            firefox_options.headless = False

        if run_type == 'local':
            context.driver = webdriver.Firefox(options=firefox_options)
        elif run_type == 'remote':
            context.driver = webdriver.Remote(command_executor=selenium_hub_url,
                                              desired_capabilities=DesiredCapabilities.FIREFOX, options=firefox_options)

    context.driver.get(url)


def after_step(context, step):
    print()
    report_name = 'error_screenshot_' + str(datetime.datetime.now()) + '_' + UtilHelper.get_random_string_with_uuid()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name=report_name,
                      attachment_type=allure.attachment_type.PNG)


def after_scenario(context, driver):
    context.driver.quit()
