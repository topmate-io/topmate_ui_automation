from features.pageobjects.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_element_to_be_visible('welcome_message_XPATH', 5)
        print('Login Successful! Successfully landed to Home Page')

    def get_current_url(self):
        return self.get_present_url()

