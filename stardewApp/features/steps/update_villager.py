from behave import given, when, then
from django.db import connection
from stardewApp.models import Villager

@given("the user that has added a villager wants to modify it")
def step_given_user_wants_to_modify_villager(context):
    context.villager = Villager.objects.create(name="Jaume", birthday="July 27th")
    context.browser.visit(context.get_url('/villagers/add/'))

@when("they modify any of the fields on the villager page")
def step_when_modify_villager_fields(context):
    # Assuming you have a route for editing a specific villager
    context.browser.fill("name", "Erik")
    context.browser.find_by_xpath('//button[text()="Submit"]').first.click()

@then("the information is modified in the database")
def step_then_information_modified_in_database(context):
    updated_villager = Villager.objects.get(id=context.villager.id)
    assert updated_villager.name == "Erik"