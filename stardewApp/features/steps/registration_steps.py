from behave import given, when, then
from django.contrib.auth.models import User
from django.db import connection


@given('a visitor that wants to register')
def step_given_visitor_wants_to_register(context):
    context.browser.visit(context.get_url('account/signup/'))

@when('they introduce a valid user and password')
def step_when_introduce_valid_user_password(context):
    context.browser.fill("username", "CarlesM")
    context.browser.fill("password1", "contrasenya1")
    context.browser.fill("password2", "contrasenya1")
    context.browser.find_by_xpath('//button[text()="Signup"]').first.click()

@then('their data is stored')
def step_then_data_is_stored(context):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM auth_user WHERE username = 'CarlesM' AND password = 'contrasenya1'")
        count = cursor.fetchone()[0]
        assert count > 0

@when('they introduce an invalid user and password')
def step_when_introduce_invalid_user_password(context):
    context.browser.fill("username", "Roberto")
    context.browser.fill("password1", "contrasenya1")
    context.browser.fill("password2", "contrasenya2")
    context.browser.find_by_xpath('//button[text()="Signup"]').first.click()

@then('their data is not stored')
def step_then_data_is_not_stored(context):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM auth_user WHERE username = 'Roberto' AND password = 'contrasenya1'")
        count = cursor.fetchone()[0]
        assert count == 0
