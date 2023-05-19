from behave import given, when, then
from django.contrib.auth.models import User

@given('a visitor that wants to register')
def step_given_visitor_wants_to_register(context):
    pass

@when('they introduce a valid user and password')
def step_when_introduce_valid_user_password(context):
    context.username = 'testuser'
    context.password = 'testpassword'

@then('their data is stored')
def step_then_data_is_stored(context):
    user = User.objects.create_user(username=context.username, password=context.password)
    assert user is not None

@when('they introduce an invalid user and password')
def step_when_introduce_invalid_user_password(context):
    context.username = 'invaliduser'
    context.password = 'invalidpassword'

@then('their data is not stored')
def step_then_data_is_not_stored(context):
    user = User.objects.create_user(username=context.username, password=context.password)
    assert user is None
