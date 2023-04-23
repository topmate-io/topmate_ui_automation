from features.pageobjects.BasePage import BasePage
from utilities import log_util

log = log_util.get_logs()


class PublicProfileWebinarPackageBookingPage(BasePage):

    def __init__(self, driver, booking_type):
        super().__init__(driver)
        webinar_page_title = self.wait_for_element_to_be_visible('webinar_page_title_CSS', 10)
        if self.get_text(webinar_page_title) == booking_type:
            log.info('Navigation to Webinar Seat Booking Page of Public Profile id SUCCESSFUL!')
        else:
            raise RuntimeError('Navigation to Webinar Seat Booking Page of Public Profile id FAILED!')

    def book_seat_for_webinar(self):
        log.info('booking seat for webinar')
        book_seat_button = self.get_element('book_seat_button_XPATH')
        self.click(book_seat_button)
        log.info('seat has been booked successfully')

    def click_on_buy_package(self):
        log.info('clicking on buy package for webinar')
        buy_package_button = self.get_element('buy_package_button_XPATH')
        self.click(buy_package_button)
        log.info('buy package has been clicked successfully')
