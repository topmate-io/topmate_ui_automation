import time

from features.pageobjects.BasePage import BasePage
from utilities import log_util

log = log_util.get_logs()


class PublicProfileBookingFormPage(BasePage):

    def __init__(self, driver, duration):
        super().__init__(driver)
        meeting_details_heading_locator = self.get_locator('meeting_details_heading_XPATH').replace(
            '[replace duration here]', str(duration))
        self.wait_for_element_to_be_visible_with_locator_value(meeting_details_heading_locator, 'XPATH', 10)
        log.info('Successfully navigated to Booking Form Page of Public Profile')

    def user_fills_up_booking_form_data(self, name: str, email: str, about_call: str, phone_number: str, duration):
        log.info('User filling up booking form data')
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

    def user_click_on_confirm_pay(self):
        log.info('Clicking on Confirm and Pay')
        confirm_pay_button = self.get_element('confirm_pay_XPATH')
        self.scroll_to_bottom_of_page_using_JS()
        self.click(confirm_pay_button)

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

    def verify_booking_status(self, expected_message1, expected_message2):
        log.info('verifying booking status')
        booking_status_element = self.wait_for_element_to_be_visible('booking_status_CSS', 10)
        booking_status_message = self.get_text(booking_status_element)
        log.info(f'expected status message: {expected_message1}')
        log.info(f'actual status message: {booking_status_message}')

        service_title_element = self.get_element('service_title_CSS')
        service_title_text = self.get_text(service_title_element)
        log.info(f'expected service_title_text: {expected_message2}')
        log.info(f'actual service_title_text: {service_title_text}')
        if booking_status_message == expected_message1 and service_title_text == expected_message2:
            return True
