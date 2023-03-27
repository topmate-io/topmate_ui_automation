import time

from behave import *
from features.pageobjects.PublicProfile_BookingFormPage import PublicProfileBookingFormPage
from features.pageobjects.PublicProfile_BookingPage import PublicProfileBookingPage
from features.pageobjects.PublicProfile_EntryPage import PublicProfileEntryPage
from utilities import log_util

log = log_util.get_logs()


@given('user navigates to public profile page of topmate with user "{username}"')
def step_impl(context, username):
    public_profile_url = context.url + username
    log.info(f'Navigating to Entry Page for Public Profile of {public_profile_url}')
    context.public_profile_entry_page = PublicProfileEntryPage(context.driver)
    context.public_profile_entry_page.navigate_to_pubic_profile(public_profile_url)
    context.public_profile_entry_page.maximize_window()


@given('user clicks on video call booking for "{duration}" minutes')
def step_impl(context, duration):
    context.public_profile_entry_page.book_video_call(int(duration))


@when('user books meeting with time and date for "{duration}" minutes video call')
def step_impl(context, duration):
    context.public_profile_booking_page = PublicProfileBookingPage(context.driver, duration)
    for row in context.table:
        """Choosing a date"""
        if row['date'] == 'random':
            context.public_profile_booking_page.pick_random_date()
        else:
            # TODO: Need to be implemented in future
            pass

        """Choosing a timezone"""
        context.public_profile_booking_page.choose_time_zone(row['timezone'])

        """Choosing a time slot"""
        if row['time'] == 'random':
            context.public_profile_booking_page.pick_random_time()
        else:
            # TODO: Need to be implemented in future
            pass
        context.public_profile_booking_page.confirm_booking_details()


@step('user fills up the booking form for "{duration}" minutes video call with user details')
def step_impl(context, duration):
    context.public_profile_booking_form_page = PublicProfileBookingFormPage(context.driver, duration)
    for row in context.table:
        context.public_profile_booking_form_page.user_fills_up_booking_form_data(row['name'], row['email'],
                                                                                 row['what is the call about'],
                                                                                 row['Phone Number'], duration)


@step("user clicks on Confirm and Pay")
def step_impl(context):
    context.public_profile_booking_form_page.user_click_on_confirm_pay()


@step("user choose payment type")
def step_impl(context):
    assert context.public_profile_booking_form_page.verify_payment_tab_is_open('Topmate'), "Payment tab is not open"
    for row in context.table:
        context.public_profile_booking_form_page.choose_payment_type(row['payment mode'])
        context.public_profile_booking_form_page.choose_payment_bank(row['payment bank'])
        time.sleep(10)


@step("user clicks on Pay Now")
def step_impl(context):
    context.public_profile_booking_form_page.click_on_pay_now()


@step('user choose payment status as "{payment_status}"')
def step_impl(context, payment_status):
    context.public_profile_booking_form_page.choose_payment_status(payment_status)


@step('verify booking is confirmed for the selected time and date')
def step_impl(context):
    for row in context.table:
        booking_status = context.public_profile_booking_form_page.verify_booking_status(row['expected message1'],
                                                                                        row['expected message2'])
        assert booking_status, "Booking Status is Failed!"
