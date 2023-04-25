import time

from api.api_utils import api_requests
from api.endpoints import endpoints
from features.pageobjects.BasePage import BasePage
from utilities import log_util

log = log_util.get_logs()


class PublicProfileBookingConfirmationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        url = self.get_present_url()
        if 'booking-confirmation' in url or 'query-success' in url or 'buydoc-success' in url:
            log.info('Successfully navigated to Booking Form Page of Public Profile')
        else:
            log.error('Booking Confirmation Page is not loaded successfully')
            raise Exception('Booking Confirmation Page is not loaded successfully')

    def verify_booking_status_for_all_services(self, expected_message1, expected_message2):
        log.info('verifying booking status')
        booking_status_element = self.wait_for_element_to_be_visible('booking_status_CSS', 15)
        booking_status_message = self.get_text(booking_status_element)
        log.info(f'expected status message: {expected_message1}')
        log.info(f'actual status message: {booking_status_message}')

        if expected_message2 == '':
            if booking_status_message == expected_message1:
                return True
        else:
            service_title_element = self.get_element('service_title_CSS')
            service_title_text = self.get_text(service_title_element)
            log.info(f'expected service_title_text: {expected_message2}')
            log.info(f'actual service_title_text: {service_title_text}')
            if booking_status_message == expected_message1 and service_title_text == expected_message2:
                return True

    def get_bookingID_from_page_title(self) -> str:
        url = self.get_present_url()
        booking_id = str(url).split('?')[0].split('/')[-1]
        return booking_id

    #################################################################--API--#########################################################################################

    def get_payment_status_API(self, booking_type: str, booking_id: str):
        host = 'https://gravitron.run'
        endpoint = endpoints.get_booking_status_endpoint(booking_type, booking_id)
        res_json = api_requests.get(host=host, endpoint=endpoint)
        return res_json.get('status')
