from features.pageobjects.BasePage import BasePage
from features.pageobjects.LoginPage import LoginPage


class EntryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to(self, url):
        self.driver.get(url)

    def click_login_button(self):
        button = self.wait_for_element_to_be_clickable('login_button_CSS', 5)
        self.click(button)
