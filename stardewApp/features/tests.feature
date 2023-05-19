
#####ADDING AN INSTANCE
Feature: Testing adding a villager
    Scenario: A villager is added correctly
        Given a user that tries to add a villager
        When they select the add villager option with a name, birthday and a list of liked and loved items
        Then the villager is stored in the database

#####MODIFYING AN INSTANCE
Feature: Testing updating a villager
    Scenario: A villager is updated correctly
        Given the user that has added a villager wants to modify it
        When they modify any of the fields on the villager page
        Then the information is modified in the database

