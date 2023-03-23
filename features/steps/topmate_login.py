import sys

from behave import *
from features.pageobjects.EntryPage import EntryPage
from features.pageobjects.HomePage import HomePage
from features.pageobjects.LoginPage import LoginPage
from utilities import log_util

log = log_util.get_logs()


@given('user navigates to entry page of topmate.io')
def step_impl(context):
    log.info(f'Navigating to Entry Page for {context.url}')
    context.entry_page = EntryPage(context.driver)
    context.entry_page.maximize_window()


@given('user clicks on login')
def step_impl(context):
    context.entry_page.click_login_button()


@when('user enters username as "{username}" and password as "{password}"')
def step_impl(context, username, password):
    log.info(f'Testing with username: {username} password: {password}')
    context.login_page = LoginPage(context.driver)
    context.login_page.set_username(username)
    context.login_page.set_password(password)


@when('user clicks on Sign-in')
def step_impl(context):
    context.login_page.click_sign_in()


@then('verify user is navigated to homepage')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    current_url = context.home_page.get_current_url()
    assert '/dashboard/home' in current_url, f"'/dashboard/home' is not present in current title {current_url}"
    log.info(' current URL is matched for HOMEPAGE')
    log.info('Test Case Passed... | Login Successful!')


@then('verify login error message is displayed')
def step_impl(context):
    expected_error_message = 'The username or password seems incorrect. Please check & try again'
    actual_error_message = context.login_page.get_login_error_message()
    log.info(f'Expected error message: {expected_error_message}')
    log.info(f'Actual error message: {actual_error_message}')
    assert expected_error_message == actual_error_message, "Error Message Mismatched"
    log.info('Test Case Passed... | Login Failure!')
