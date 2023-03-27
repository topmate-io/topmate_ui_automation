import time

from features.pageobjects.BasePage import BasePage
from utilities import log_util
from utilities.util_helper import UtilHelper

log = log_util.get_logs()


class PublicProfileBookingPage(BasePage):

    def __init__(self, driver, duration):
        super().__init__(driver)
        video_call_description_heading_locator = self.get_locator('video_call_description_XPATH').replace(
            '[replace duration here]', str(duration))
        self.wait_for_element_to_be_visible_with_locator_value(video_call_description_heading_locator, 'XPATH', 10)
        log.info('Successfully navigated to Booking Page of Public Profile')

    def pick_random_date(self):
        """for now we are selecting the second date just beside the default pre-selected date"""
        date_element = self.wait_for_element_to_be_clickable('second_date_CSS', 10)
        self.click(date_element)
        # date_slot_box_element = self.wait_for_element_to_be_visible('date_slot_box_CSS', 10)
        # self.hover_on_element(date_slot_box_element)
        # date_slot_list = self.wait_for_all_elements_to_be_visible('date_slot_list_CSS', 5)
        # random_date_slot = date_slot_list[UtilHelper.get_random_number(0, len(date_slot_list)-1)]
        # self.scroll_to_element(random_date_slot)
        # self.click(random_date_slot)
        # log.info(f'time slot: {self.get_text(random_date_slot)} has been set successfully')


    def choose_time_zone(self, zone):
        log.info(f'Choosing {zone} time zone')
        timezone_dropdown = self.get_element('timezone_dropdown_CSS')
        self.click(timezone_dropdown)
        timezone_dropdown_box = self.wait_for_element_to_be_visible('time_zone_dropdown_box_ID', 5)
        self.hover_on_element(timezone_dropdown_box)
        timezone = self.wait_for_element_to_be_clickable(f'{zone}_timezone_XPATH', 10)
        self.scroll_to_element(timezone)
        self.click(timezone)
        log.info(f'timezone: {zone} has been set successfully')

    def pick_random_time(self):
        log.info('picking random time')
        time_slot_box_element = self.get_element('time_slot_box_CSS')
        self.hover_on_element(time_slot_box_element)
        time_slot_list = self.wait_for_all_elements_to_be_visible('time_slot_list_CSS', 10)
        random_time_slot = time_slot_list[UtilHelper.get_random_number(0, len(time_slot_list)-1)]
        self.scroll_to_element(random_time_slot)
        self.click(random_time_slot)
        log.info(f'time slot: {self.get_text(random_time_slot)} has been set successfully')

    def confirm_booking_details(self):
        log.info('confirming booking details')
        confirm_button = self.get_element('confirm_button_CSS')
        self.click(confirm_button)
        log.info('booking details has been confirmed successfully')



