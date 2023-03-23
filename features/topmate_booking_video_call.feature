Feature: As an user I want to test booking functionality for video call of topmate.io from public profile

  Background:
    Given user navigates to public profile page of topmate with user "automate_topmate"

  @smoke
  Scenario: Validating the booking functionality for 15 minutes video call of topmate.io from public profile
    Given user clicks on video call booking for "15" minutes
    When user picks a random date
    And user choose timezone "IST"
    And user picks a random time
    And user confirms booking details
    And user fills up the booking form with user deatils
      | name      | email                | what is the call about | Phone Number | Receive Booking Details |
      | Test_User | dipanjan56@gmail.com | For Testing            | 0123456789   | yes                     |
    And user clicks on Confirm and Pay
    And user choose payment type
      | payment mode | bank |
      | NetBanking   | PNB  |
    And user clicks on Pay Now
    And user choose payment status as "Success"
    Then verify payment status as "Success"
    And verify booking is confirmed for the selected time and date
