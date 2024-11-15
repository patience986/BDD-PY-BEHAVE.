Feature: User Login
  As a user, I want to log into the application so I can access my account

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid credentials
    Then the user is redirected to the dashboard

  Scenario: Failed login with invalid credentials
    Given the user is on the login page
    When the user enters invalid credentials
    Then an error message is displayed
