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