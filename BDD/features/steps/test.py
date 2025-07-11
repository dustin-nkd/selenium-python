from behave import *


def before_scenario(context):
    print("Inside Before Scenario")


def after_scenario(context):
    print("Inside After Scenario")


def after_step(context, step):
    print()


@given(u'user navigate to Google Search')
def step_impl(context):
    print(u'STEP: Given user navigate to Google Search')


@when(u'Enter Selenium into search field')
def step_impl(context):
    print(u'STEP: When Enter Selenium into search field')


@when(u'Click on the search button')
def step_impl(context):
    print(u'STEP: When Click on the search button')


@then(u'The search result will be displayed')
def step_impl(context):
    print(u'STEP: Then The search result will be displayed')
