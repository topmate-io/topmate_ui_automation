Feature: As an user I want to test login functionality of topmate.io

  Background:
    Given user navigates to topmate.io

  @smoke
  Scenario Outline: Validating the login functionality with correct username and correct password
    Given user clicks on login
    When user enters "<username>" and "<password>"
    And user clicks on Sign-in
    Then verify user is navigated to homepage
    Examples:
      | username         | password |
      | automate_topmate | 123456   |


  @sanity
  Scenario Outline: Validating the login functionality with wrong username and correct password
    Given user clicks on login
    When user enters "<username>" and "<password>"
    And user clicks on Sign-in
    Then verify login error message is displayed
    Examples:
      | username                    | password |
      | automationtopmate@gmail.com | 123456   |


  @sanity
  Scenario Outline: Validating the login functionality with correct username and wrong password
    Given user clicks on login
    When user enters "<username>" and "<password>"
    And user clicks on Sign-in
    Then verify login error message is displayed
    Examples:
      | username         | password |
      | automate_topmate | 12345678 |