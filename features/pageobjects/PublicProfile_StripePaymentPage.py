import time

from api.api_utils import api_requests
from api.endpoints import endpoints
from features.pageobjects.BasePage import BasePage
from utilities import log_util

log = log_util.get_logs()


class PublicProfileStripePaymentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_element_to_be_visible('pay_with_card_header_XPATH', 15)
        log.info('Successfully navigated to Public Profile Stripe Payment Page')

    def user_fills_up_card_details(self, email: str, card_number: str, expiry_date: str, cvv: str, name: str,
                                   country_region: str):
        log.info('User filling up card details')
        email_field = self.wait_for_element_to_be_clickable('stripe_email_field_ID', 5)
        card_number_field = self.get_element('stripe_card_number_ID')
        expiry_date_field = self.get_element('stripe_expiry_date_ID')
        cvv_field = self.get_element('stripe_cvv_ID')
        name_field = self.get_element('stripe_name_ID')
        country_region_dropdown_field = self.get_element('stripe_country_dropdown_ID')
        secure_checkbox_field = self.get_element('secure_checkbox_ID')

        self.type(email_field, email)
        self.type(card_number_field, card_number)
        self.type(expiry_date_field, expiry_date)
        self.type(cvv_field, cvv)
        self.type(name_field, name)
        if country_region.lower() != 'default':
            self.select_from_dropdown(country_region, country_region_dropdown_field)

        # as seen in the report, secure checkbox is by-default checked, hence unchecking it
        self.click(secure_checkbox_field)
        self.wait(2)


    def click_on_pay(self):
        log.info('clicking on Pay')
        pay_button = self.wait_for_element_to_be_clickable('stripe_pay_button_CSS')
        self.click(pay_button)
        log.info('Pay button has been clicked successfully')
        self.wait(8)
