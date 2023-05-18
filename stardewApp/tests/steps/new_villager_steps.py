from behave import given, when, then
from django.db import connection
from stardewApp.models import Villager

@given("a user that tries to add a villager")
def step_given_user_adds_villager(context):
    context.browser.visit(context.get_url('villagers/add/'))

@when("they select the add villager option with a name, birthday and a list of liked and loved items")
def step_when_select_add_villager_option(context):
    context.browser.fill("name", "Jaume")
    context.browser.fill("birthday", "Summer 27th")
    context.browser.fill("liked items", "Daffodil")
    context.browser.fill("loved items", "Coconut")
    context.browser.find_by_xpath('//button[text()="Add Villager"]').first.click()

@then("the villager is stored in the database")
def step_then_villager_stored_in_database(context):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM Villager WHERE name = 'Erik' AND birthday = 'Summer 27th'")
        count = cursor.fetchone()[0]
        assert count > 0