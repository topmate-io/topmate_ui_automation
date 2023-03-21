from features.pageobjects.BasePage import BasePage
from utilities import log_util

log = log_util.get_logs()


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_element_to_be_visible('welcome_message_XPATH', 10)
        log.info('Login Successful! Successfully landed to Home Page')

    def get_current_url(self):
        log.info('fetching current url of HomePage')
        return self.get_present_url()

