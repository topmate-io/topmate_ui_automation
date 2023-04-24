import time

from behave import *

from features.pageobjects.PublicProfile_BookingConfirmationPage import PublicProfileBookingConfirmationPage
from features.pageobjects.PublicProfile_BookingFormPage import PublicProfileBookingFormPage
from features.pageobjects.PublicProfile_BookingPage import PublicProfileBookingPage
from features.pageobjects.PublicProfile_EntryPage import PublicProfileEntryPage
from features.pageobjects.PublicProfile_StripePaymentPage import PublicProfileStripePaymentPage
from features.pageobjects.PublicProfile_Webinar_Package_BookingPage import \
    PublicProfileWebinarPackageDocumentBookingPage
from utilities import log_util

log = log_util.get_logs()


@given('user navigates to public profile page of topmate with user "{username}"')
def step_impl(context, username):
    public_profile_url = context.url + username
    log.info(f'Navigating to Entry Page for Public Profile of {public_profile_url}')
    context.public_profile_entry_page = PublicProfileEntryPage(context.driver)
    context.public_profile_entry_page.navigate_to_pubic_profile(public_profile_url)
    context.public_profile_entry_page.maximize_window()


@given('user clicks booking service')
def step_impl(context):
    for row in context.table:
        booking_type = row['booking type']
        duration = row['duration']
        context.public_profile_entry_page.book_service(booking_type, duration)


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
        # context.public_profile_booking_page.choose_time_zone(row['timezone'])

        """Choosing a time slot"""
        if row['time'] == 'random':
            context.public_profile_booking_page.pick_random_time()
        else:
            # TODO: Need to be implemented in future
            pass
        context.public_profile_booking_page.confirm_booking_details()


@when("user clicks on Book Seat")
def step_impl(context):
    booking_type = 'Webinar'
    context.public_profile_webinar_package_document_booking_page = PublicProfileWebinarPackageDocumentBookingPage(
        context.driver,
        booking_type)
    context.public_profile_webinar_package_document_booking_page.book_seat_for_webinar()


@when("user clicks on Buy Package")
def step_impl(context):
    booking_type = 'Package'
    context.public_profile_webinar_package_document_booking_page = PublicProfileWebinarPackageDocumentBookingPage(
        context.driver,
        booking_type)
    context.public_profile_webinar_package_document_booking_page.click_on_buy_package()


@when("user clicks on Purchase")
def step_impl(context):
    booking_type = 'Document Service'
    context.public_profile_webinar_package_document_booking_page = PublicProfileWebinarPackageDocumentBookingPage(
        context.driver,
        booking_type)
    context.public_profile_webinar_package_document_booking_page.click_on_purchase()


@step('user fills up the booking form for "{duration}" minutes video call with user details')
def step_impl(context, duration):
    booking_type = 'video call'
    booking_duration = duration
    context.public_profile_booking_form_page = PublicProfileBookingFormPage(context.driver, booking_type,
                                                                            booking_duration)
    for row in context.table:
        context.public_profile_booking_form_page.user_fills_up_booking_form_data_for_video_call(row['name'],
                                                                                                row['email'],
                                                                                                row[
                                                                                                    'what is the call about'],
                                                                                                row['Phone Number'],
                                                                                                duration)


@step('user fills up the booking form for query service with user details')
def step_impl(context):
    booking_type = 'query'
    booking_duration = None
    context.public_profile_booking_form_page = PublicProfileBookingFormPage(context.driver, booking_type,
                                                                            booking_duration)
    for row in context.table:
        context.public_profile_booking_form_page.user_fills_up_booking_form_data_for_query(row['Your Name'],
                                                                                           row['Email'],
                                                                                           row['Your Question'],
                                                                                           row['Phone Number'])


@step("user fills up the booking form for webinar service with user details")
def step_impl(context):
    booking_type = 'webinar'
    booking_duration = None
    context.public_profile_booking_form_page = PublicProfileBookingFormPage(context.driver, booking_type,
                                                                            booking_duration)
    for row in context.table:
        context.public_profile_booking_form_page.user_fills_up_booking_form_data_for_webinar(row['Your Name'],
                                                                                             row['Email'],
                                                                                             row['Phone Number'])


@step("user fills up the booking form for package service with user details")
def step_impl(context):
    booking_type = 'package'
    booking_duration = None
    context.public_profile_booking_form_page = PublicProfileBookingFormPage(context.driver, booking_type,
                                                                            booking_duration)
    for row in context.table:
        context.public_profile_booking_form_page.user_fills_up_booking_form_data_for_webinar(row['Your Name'],
                                                                                             row['Email'],
                                                                                             row['Phone Number'])


@step("user fills up the booking form for document service service with user details")
def step_impl(context):
    booking_type = 'document dervice'
    booking_duration = None
    context.public_profile_booking_form_page = PublicProfileBookingFormPage(context.driver, booking_type,
                                                                            booking_duration)
    for row in context.table:
        context.public_profile_booking_form_page.user_fills_up_booking_form_data_for_webinar(row['Your Name'],
                                                                                             row['Email'],
                                                                                             row['Phone Number'])


@step("user clicks on '{button_name}'")
def step_impl(context, button_name):
    context.public_profile_booking_form_page.user_click_on_payment_initiate_button(button_text=button_name)


@step("user choose payment type")
def step_impl(context):
    assert context.public_profile_booking_form_page.verify_payment_tab_is_open('Topmate'), "Payment tab is not open"
    for row in context.table:
        context.public_profile_booking_form_page.choose_payment_mode(row['payment mode'])
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
    context.public_profile_booking_confirmation_page = PublicProfileBookingConfirmationPage(context.driver)
    for row in context.table:
        booking_status = context.public_profile_booking_confirmation_page.verify_booking_status_for_all_services(
            row['expected message1'],
            row['expected message2'])
        assert booking_status, f"Booking Status {row['expected message2']}: FAILED!"
        log.info(f"Booking Status {row['expected message2']}: SUCCESS!")


@then("API: user verify payment status")
def step_impl(context):
    for row in context.table:
        booking_type = row['booking type'].lower()
        expected_payment_status = row['payment status']
        booking_id = context.public_profile_booking_confirmation_page.get_bookingID_from_page_title()
        actual_payment_status = context.public_profile_booking_confirmation_page.get_payment_status_API(
            booking_type, booking_id)
        assert expected_payment_status == actual_payment_status, f"Expected Payment Status: {expected_payment_status} | Actual Payment status: {actual_payment_status}: FAILED!"
        log.info(
            f"Expected Payment Status: {expected_payment_status} | Actual Payment status: {actual_payment_status}: SUCCESS!")


@step("user fills up card details for stripe payment")
def step_impl(context):
    context.public_profile_stripe_payment_page = PublicProfileStripePaymentPage(context.driver)
    for row in context.table:
        email_id = row['Email']
        card_number = row['Card Number']
        expiry_date = row['Expiry date']
        cvv = row['CVV']
        name = row['Name on card']
        country_region = row['Country Or Region']
        context.public_profile_stripe_payment_page.user_fills_up_card_details(email_id, card_number, expiry_date, cvv,
                                                                              name, country_region)


@step("user clicks on Pay for stripe payment")
def step_impl(context):
    context.public_profile_stripe_payment_page.click_on_pay()
