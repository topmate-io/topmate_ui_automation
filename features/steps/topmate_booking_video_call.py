import time

from behave import *

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


@when("user picks a random date")
def step_impl(context):
    context.public_profile_booking_page = PublicProfileBookingPage(context.driver)
    context.public_profile_booking_page.pick_random_date()



@step('user choose timezone "{timezone}"')
def step_impl(context, timezone):
    context.public_profile_booking_page.choose_time_zone(timezone)


@step("user picks a random time")
def step_impl(context):
    context.public_profile_booking_page.pick_random_time()



@step("user confirms booking details")
def step_impl(context):
    context.public_profile_booking_page.confirm_booking_details()
    time.sleep(10)


@step("user fills up the booking form with user deatils")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user fills up the form with user deatils')


@step("user clicks on Confirm and Pay")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user clicks on Confirm and Pay')


@step("user choose payment type")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user choose payment type')


@step("user clicks on Pay Now")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user clicks on Pay Now')


@step('user choose payment status as "{status}"')
def step_impl(context, status):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user choose payment status as "Success"')


@then('verify payment status as "{status}"')
def step_impl(context, status):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then verify payment status as "Success"')


@step("verify booking is confirmed for the selected time and date")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And verify booking is confirmed for the selected time and date')
