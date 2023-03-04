from behave import *

from Utilities import configReader
from features.pageobjects.EntryPage import EntryPage
from features.pageobjects.HomePage import HomePage
from features.pageobjects.LoginPage import LoginPage


@given('user navigates to topmate.io')
def step_impl(context):
    url = configReader.readConfig("basic info", "test_site_url")
    context.entry_page = EntryPage(context.driver)
    context.entry_page.navigate_to(url)


@given('user clicks on login')
def step_impl(context):
    context.entry_page.click_login_button()


@when('user enters "{username}" and "{password}"')
def step_impl(context, username, password):
    print(f'Testing with username: {username} password: {password}')
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
    assert '/dashboard/home' in current_url


@then('verify login error message is displayed')
def step_impl(context):
    expected_error_message = 'The username or password seems incorrect. Please check & try again'
    actual_error_message = context.login_page.get_login_error_message()
    print(f'actual err: {actual_error_message} \nexpected err: {expected_error_message}')
    assert expected_error_message == actual_error_message
    print('Login Failure!')
