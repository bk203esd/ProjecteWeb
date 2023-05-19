from behave import given, when, then
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

@given('a registered user that wants to login')
def step_given_registered_user_wants_to_login(context):
    context.user = User.objects.create_user(username='testuser', password='testpassword')

@when('they introduce a stored user and password combination')
def step_when_introduce_stored_user_password(context):
    context.username = 'testuser'
    context.password = 'testpassword'

@then('the login is successful')
def step_then_login_successful(context):
    user = authenticate(username=context.username, password=context.password)
    assert user is not None

@when('they introduce a non-stored user and password combination')
def step_when_introduce_non_stored_user_password(context):
    context.username = 'nonexistentuser'
    context.password = 'invalidpassword'

@then('the login is unsuccessful')
def step_then_login_unsuccessful(context):
    user = authenticate(username=context.username, password=context.password)
    assert user is None