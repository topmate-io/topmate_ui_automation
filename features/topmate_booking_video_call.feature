Feature: As an user I want to test booking functionality for video call of topmate.io from public profile

  Background:
    Given user navigates to public profile page of topmate with user "automate_topmate"

  @regression
  Scenario: Validating the booking functionality for 15 minutes video call of topmate.io from public profile
    Given user clicks on video call booking for "15" minutes
    When user books meeting with time and date for "15" minutes video call
      | date   | time   | timezone |
      | random | random | IST      |
    And user fills up the booking form for "15" minutes video call with user details
      | name      | email                       | what is the call about | Phone Number |
      | Test_User | test_user_topmate@gmail.com | For Testing            | 1234567890   |
    And user clicks on Confirm and Pay
    And user choose payment type
      | payment mode | payment bank |
      | Netbanking   | IDBI         |
    And user clicks on Pay Now
    And user choose payment status as "Success"
    Then verify booking is confirmed for the selected time and date
      | expected message1 | expected message2      |
      | Booking confirmed | for 15 mins video call |
    And API: user verify payment status as 'upcoming'

  @regression
  Scenario: Validating the booking functionality for 30 minutes video call of topmate.io from public profile
    Given user clicks on video call booking for "30" minutes
    When user books meeting with time and date for "30" minutes video call
      | date   | time   | timezone |
      | random | random | IST      |
    And user fills up the booking form for "30" minutes video call with user details
      | name      | email                       | what is the call about | Phone Number |
      | Test_User | test_user_topmate@gmail.com | For Testing            | 1234567890   |
    And user clicks on Confirm and Pay
    And user choose payment type
      | payment mode | payment bank |
      | Netbanking   | PNB          |
    And user clicks on Pay Now
    And user choose payment status as "Success"
    Then verify booking is confirmed for the selected time and date
      | expected message1 | expected message2      |
      | Booking confirmed | for 30 mins video call |
    And API: user verify payment status as 'upcoming'

  @regression
  Scenario: Validating the booking functionality for 60 minutes video call of topmate.io from public profile
    Given user clicks on video call booking for "60" minutes
    When user books meeting with time and date for "60" minutes video call
      | date   | time   | timezone |
      | random | random | IST      |
    And user fills up the booking form for "60" minutes video call with user details
      | name      | email                       | what is the call about | Phone Number |
      | Test_User | test_user_topmate@gmail.com | For Testing            | 1234567890   |
    And user clicks on Confirm and Pay
    And user choose payment type
      | payment mode | payment bank |
      | Netbanking   | Kotak        |
    And user clicks on Pay Now
    And user choose payment status as "Success"
    Then verify booking is confirmed for the selected time and date
      | expected message1 | expected message2      |
      | Booking confirmed | for 60 mins video call |
    And API: user verify payment status as 'upcoming'


