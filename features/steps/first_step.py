
from behave import *


@given('print given')
def step_impl(context):
    print('print given')


@when('print when')
def step_impl(context):
    print('print when')


@then('print then')
def step_impl(context):
    print('print then')