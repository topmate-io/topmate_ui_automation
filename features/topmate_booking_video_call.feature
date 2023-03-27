Feature: As an user I want to test booking functionality for video call of topmate.io from public profile

  Background:
    Given user navigates to public profile page of topmate with user "automate_topmate"

  @regression
  Scenario: Validating the booking functionality for 15 minutes video call of topmate.io from public profile
    Given user clicks on video call booking for "30" minutes
    When user books meeting with time and date for "30" minutes video call
      | date   | time   | timezone |
      | random | random | IST      |
    And user fills up the booking form for "30" minutes video call with user details
      | name      | email                | what is the call about | Phone Number |
      | Test_User | dipanjan56@gmail.com | For Testing            | 1234567890   |
    And user clicks on Confirm and Pay
    And user choose payment type
      | payment mode | payment bank |
      | Netbanking   | Axis         |
    And user clicks on Pay Now
    And user choose payment status as "Success"
    Then verify booking is confirmed for the selected time and date
      | expected message1 | expected message2      |
      | Booking confirmed | for 30 mins video call |
