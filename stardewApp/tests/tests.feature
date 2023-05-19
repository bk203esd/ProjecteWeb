#####REGISTERING
Feature: Testing the registration
    Scenario: Correct registering
        Given a visitor that wants to register
        When they introduce a valid user and password
        Then their data is stored

    Scenario: Incorrect registering
        Given a visitor that wants to register
        When they introduce an invalid user and password
        Then their data is not stored

#####LOGGING IN
Feature: Testing the login
    Scenario: Registered correct login
        Given a registered user that wants to login
        When they introduce a stored user and password combination
        Then the login is successful

    Scenario: Registered incorrect login
        Given a user that wants to login
        When they introduce a non-stored user and password combination
        Then the login is unsuccessful

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

