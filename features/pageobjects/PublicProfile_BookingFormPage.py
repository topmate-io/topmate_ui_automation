import time

from api.api_utils import api_requests
from api.endpoints import endpoints
from features.pageobjects.BasePage import BasePage
from utilities import log_util

log = log_util.get_logs()


class PublicProfileBookingFormPage(BasePage):

    def __init__(self, driver, booking_type, booking_duration):
        super().__init__(driver)
        if booking_type == 'video call':
            meeting_details_heading_locator = self.get_locator('meeting_details_heading_XPATH').replace(
                '[replace duration here]', str(booking_duration))
            self.wait_for_element_to_be_visible_with_locator_value(meeting_details_heading_locator, 'XPATH', 10)
        elif booking_type == 'query':
            self.wait_for_element_to_be_visible('query_heading_XPATH', 10)
        elif booking_type == 'webinar':
            self.wait_for_element_to_be_visible('webinar_heading_XPATH', 10)
        elif booking_type == 'package':
            self.wait_for_element_to_be_visible('package_heading_XPATH', 10)

        log.info(f'Successfully navigated to Booking Form Page of Public Profile for {booking_type}')

    def user_fills_up_booking_form_data_for_video_call(self, name: str, email: str, about_call: str, phone_number: str,
                                                       duration):
        log.info('User filling up booking form data for video call')
        name_field = self.wait_for_element_to_be_clickable('name_field_ID', 5)
        email_field = self.get_element('email_field_ID')
        about_call_field = self.get_element(f'{duration}_mins_about_call_ID')
        phone_number_field = self.get_element('phone_number_field_ID')
        booking_update_checkbox = self.get_element('booking_update_checkbox_ID')

        self.type(name_field, name)
        self.type(email_field, email)
        self.type(about_call_field, about_call)
        self.type(phone_number_field, phone_number)
        # first uncheck the default checked booking update checkbox
        self.click(booking_update_checkbox)
        # then check again
        time.sleep(3)
        self.click(booking_update_checkbox)

    def user_fills_up_booking_form_data_for_query(self, name: str, email: str, query_text: str, phone_number: str):
        log.info('User filling up booking form data for query')
        name_field = self.wait_for_element_to_be_clickable('name_field_ID', 5)
        email_field = self.get_element('email_field_ID')
        query_field = self.get_element('query_ID')
        phone_number_field = self.get_element('phone_number_field_ID')
        booking_update_checkbox = self.get_element('booking_update_checkbox_ID')

        self.type(name_field, name)
        self.type(email_field, email)
        self.type(query_field, query_text)
        self.type(phone_number_field, phone_number)
        # first uncheck the default checked booking update checkbox
        self.click(booking_update_checkbox)
        # then check again
        time.sleep(3)
        self.click(booking_update_checkbox)

    def user_fills_up_booking_form_data_for_webinar(self, name: str, email: str, phone_number: str):
        log.info('User filling up booking form data for query')
        name_field = self.wait_for_element_to_be_clickable('name_field_ID', 5)
        email_field = self.get_element('email_field_ID')
        phone_number_field = self.get_element('phone_number_field_ID')
        booking_update_checkbox = self.get_element('booking_update_checkbox_ID')

        self.type(name_field, name)
        self.type(email_field, email)
        self.type(phone_number_field, phone_number)
        # first uncheck the default checked booking update checkbox
        self.click(booking_update_checkbox)
        # then check again
        time.sleep(3)
        self.click(booking_update_checkbox)

    def user_click_on_confirm_pay(self):
        log.info('Clicking on Confirm and Pay')
        confirm_pay_button = self.get_element('confirm_pay_XPATH')
        self.scroll_into_view_middle_JS(confirm_pay_button)
        self.click(confirm_pay_button)
        log.info('Confirm Pay button has been clicked successfully')

    def user_click_on_send_query(self):
        log.info('Clicking on Send Query')
        send_query_button = self.get_element('send_query_XPATH')
        self.scroll_into_view_middle_JS(send_query_button)
        self.click(send_query_button)
        log.info('Send Query button has been clicked successfully')

    def user_click_on_confirm_details(self):
        log.info('Clicking on Confirm Details')
        confirm_details_button = self.get_element('webinar_confirm_details_XPATH')
        self.scroll_into_view_middle_JS(confirm_details_button)
        self.click(confirm_details_button)
        log.info('Confirm Details button has been clicked successfully')

    def user_click_on_buy_now(self):
        log.info('Clicking on Buy Now')
        confirm_details_button = self.get_element('package_buy_now_XPATH')
        self.scroll_into_view_middle_JS(confirm_details_button)
        self.click(confirm_details_button)
        log.info('Buy Now button has been clicked successfully')

    def verify_payment_tab_is_open(self, payment_tab_title: str):
        log.info('verifying payment tab is opened')
        iframe = self.wait_for_element_to_be_clickable('payment_tab_frame_CSS', 15)
        self.switch_to_frame(iframe)
        log.info('finding payment tab title')
        title_element = self.wait_for_element_to_be_visible('payment_tab_title_CSS', 15)
        actual_title_text = self.get_text(title_element)
        if actual_title_text == payment_tab_title:
            log.info('Payment tab is opened successfully')
            return True
        return False

    def choose_payment_mode(self, payment_mode: str):
        log.info(f'choosing payment type: {payment_mode}')
        payment_type_locator_value = self.get_locator('payment_type_XPATH').replace('[replace payment_type here]',
                                                                                    payment_mode)
        payment_mode_element = self.wait_for_element_to_be_clickable_with_locator_value(payment_type_locator_value,
                                                                                        'XPATH', 10)
        self.click(payment_mode_element)
        log.info(f'payment type: {payment_mode} has been chosen successfully')

    def choose_payment_bank(self, payment_bank: str):
        log.info(f'choosing payment bank: {payment_bank}')
        payment_bank_locator_value = self.get_locator('payment_bank_XPATH').replace('[replace payment_bank here]',
                                                                                    payment_bank)
        payment_bank_element = self.wait_for_element_to_be_clickable_with_locator_value(payment_bank_locator_value,
                                                                                        'XPATH', 10)
        self.click(payment_bank_element)
        log.info(f'payment bank: {payment_bank} has been chosen successfully')

    def click_on_pay_now(self):
        log.info('clicking on Pay Now')
        pay_now_button = self.get_element('pay_now_ID')
        self.click(pay_now_button)
        log.info('Pay Now button has been clicked successfully')

    def choose_payment_status(self, payment_status):
        log.info(f'choosing payment status: {payment_status}')
        self.switch_to_first_child_window()
        payment_success_locator_value = self.get_locator('payment_status_XPATH').replace(
            '[replace payment_status here]',
            payment_status)
        payment_status_button = self.wait_for_element_to_be_visible_with_locator_value(payment_success_locator_value,
                                                                                       'XPATH', 15)
        self.click(payment_status_button)
        log.info(f'payment_status: {payment_status} has been clicked successfully')
        time.sleep(15)
        self.switch_back_to_parent_window()
