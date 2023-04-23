from behave import *
from features.pageobjects.PublicProfile_BookingFormPage import PublicProfileBookingFormPage
from features.pageobjects.PublicProfile_Webinar_Package_BookingPage import PublicProfileWebinarPackageBookingPage
from utilities import log_util

log = log_util.get_logs()


@when("user clicks on Buy Package")
def step_impl(context):
    booking_type = 'Package'
    context.public_profile_webinar_package_booking_page = PublicProfileWebinarPackageBookingPage(context.driver,
                                                                                              booking_type)
    context.public_profile_webinar_package_booking_page.click_on_buy_package()


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


@step("user clicks on Buy Now")
def step_impl(context):
    context.public_profile_booking_form_page.user_click_on_buy_now()