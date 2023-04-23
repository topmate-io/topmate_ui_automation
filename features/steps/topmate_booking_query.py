import time

from behave import *

from features.pageobjects.PublicProfile_BookingConfirmationPage import PublicProfileBookingConfirmationPage
from features.pageobjects.PublicProfile_BookingFormPage import PublicProfileBookingFormPage
from features.pageobjects.PublicProfile_BookingPage import PublicProfileBookingPage
from features.pageobjects.PublicProfile_EntryPage import PublicProfileEntryPage
from features.pageobjects.PublicProfile_StripePaymentPage import PublicProfileStripePaymentPage
from utilities import log_util

log = log_util.get_logs()


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


@step("user clicks on Send Query")
def step_impl(context):
    context.public_profile_booking_form_page.user_click_on_send_query()
