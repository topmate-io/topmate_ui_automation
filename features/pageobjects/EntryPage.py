from features.pageobjects.BasePage import BasePage
from utilities import log_util

log = log_util.get_logs()


class EntryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to(self, url):
        self.driver.get(url)
        log.info(f'Navigated successfully to Entry Page for this url: {url}')

    def click_login_button(self):
        button = self.wait_for_element_to_be_clickable('login_button_CSS', 5)
        self.click(button)
