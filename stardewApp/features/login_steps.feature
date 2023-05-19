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
