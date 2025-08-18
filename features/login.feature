Feature: Login functionality
  Scenario: Login successfully with valid credentials
    Given user is on the login page
    When user enter valid username and password
    And click on login button
    Then user should redirected to the dashboard page
