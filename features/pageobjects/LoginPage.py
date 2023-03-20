from features.pageobjects.BasePage import BasePage
from utilities import log_util

log = log_util.get_logs()


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_element_to_be_visible('sign_in_text_XPATH', 5)
        log.info('successfully landed to Login Page')

    def set_username(self, name):
        log.info('typing username in username field')
        element = self.wait_for_element_to_be_clickable('username_ID', 5)
        self.type(element, value=name)

    def set_password(self, password):
        log.info('typing password in password field')
        element = self.get_element('password_ID')
        self.type(element, password)

    def click_sign_in(self):
        log.info('Clicking on sign in button')
        element = self.get_element('sign_in_button_CSS')
        self.click(element)

    def get_login_error_message(self):
        log.info('fetching login error message for incorrect login creds')
        element = self.wait_for_element_to_be_visible('login_error_message_CSS', 15)
        return self.get_text(element)
