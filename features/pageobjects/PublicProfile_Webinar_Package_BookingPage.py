from features.pageobjects.BasePage import BasePage
from utilities import log_util

log = log_util.get_logs()


class PublicProfileWebinarPackageDocumentBookingPage(BasePage):

    def __init__(self, driver, booking_type):
        super().__init__(driver)
        if booking_type.lower() == 'document service':
            page_title = self.wait_for_element_to_be_visible('document_service_page_title_CSS', 10)
        else:
            page_title = self.wait_for_element_to_be_visible('webinar_package_page_title_CSS', 10)

        if self.get_text(page_title) == booking_type:
            log.info(f'Navigation to {booking_type} Booking Page of Public Profile id SUCCESSFUL!')
        else:
            raise RuntimeError(f'Navigation to {booking_type} Booking Page of Public Profile id FAILED!')

    def book_seat_for_webinar(self):
        log.info('booking seat for webinar')
        book_seat_button = self.wait_for_element_to_be_clickable('book_seat_button_XPATH', 10)
        self.click(book_seat_button)
        log.info('seat has been booked successfully')

    def click_on_buy_package(self):
        log.info('clicking on buy package for webinar')
        buy_package_button = self.wait_for_element_to_be_clickable('buy_package_button_XPATH', 10)
        self.click(buy_package_button)
        log.info('buy package has been clicked successfully')

    def click_on_purchase(self):
        log.info('clicking on purchase for webinar')
        self.wait(3)
        purchase_button = self.wait_for_element_to_be_clickable('purchase_button_XPATH', 10)
        self.click(purchase_button)
        log.info('purchase has been clicked successfully')
