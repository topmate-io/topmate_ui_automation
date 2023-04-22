from features.pageobjects.BasePage import BasePage
from utilities import log_util

log = log_util.get_logs()


class PublicProfileEntryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_pubic_profile(self, url):
        self.driver.get(url)
        log.info(f'Navigated successfully to Public Profile Page for this url: {url}')

    def book_video_call(self, duration: int):
        element = self.wait_for_element_to_be_clickable(f'{duration}_min_video_call_XPATH', 10)
        self.scroll_into_view_middle_JS(element)
        self.hover_and_click(element)
        log.info(f'{duration} minutes video call has been clicked successfully')

    def book_query(self):
        element = self.wait_for_element_to_be_clickable('query_XPATH', 10)
        self.scroll_into_view_middle_JS(element)
        self.hover_and_click(element)
        log.info(f'Query service has been clicked successfully')
