from features.pageobjects.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_element_to_be_visible('sign_in_text_XPATH', 5)
        print('successfully landed to Login Page')

    def set_username(self, name):
        element = self.wait_for_element_to_be_clickable('username_ID', 5)
        self.type(element, value=name)

    def set_password(self, password):
        element = self.get_element('password_ID')
        self.type(element, password)

    def click_sign_in(self):
        element = self.get_element('sign_in_button_CSS')
        self.click(element)

    def get_login_error_message(self):
        element = self.wait_for_element_to_be_visible('login_error_message_CSS', 15)
        return self.get_text(element)
