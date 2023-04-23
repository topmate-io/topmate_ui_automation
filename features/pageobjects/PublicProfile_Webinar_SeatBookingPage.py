import time

from features.pageobjects.BasePage import BasePage
from utilities import log_util
from utilities.util_helper import UtilHelper

log = log_util.get_logs()


class PublicProfileWebinarSeatBookingBookingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        webinar_page_title = self.wait_for_element_to_be_visible('webinar_page_title_CSS', 10)
        if self.get_text(webinar_page_title) == 'Webinar':
            log.info('Navigation to Webinar Seat Booking Page of Public Profile id SUCCESSFUL!')
        else:
            raise RuntimeError('Navigation to Webinar Seat Booking Page of Public Profile id FAILED!')

    def book_seat_for_webinar(self):
        log.info('booking seat for webinar')
        book_seat_button = self.get_element('confirm_button_CSS')
        self.click(book_seat_button)
        log.info('seat has been booked successfully')
