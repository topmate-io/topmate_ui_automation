Feature: As an user I want to test booking functionality for Package of topmate.io from public profile

  Background:
    Given user navigates to public profile page of topmate with user "automate_topmate"

  @regression @abroad
  Scenario: Validating the booking functionality for Package of topmate.io from public profile outside india
    Given user clicks booking service
      | booking type | duration |
      | Package      | None     |
    When user clicks on Buy Package
    And user fills up the booking form for package service with user details
      | Your Name | Email                       | Phone Number |
      | Test_User | test_user_topmate@gmail.com | 1234567890   |
    And user clicks on Buy Now
    And user fills up card details for stripe payment
      | Email             | Card Number         | Expiry date | CVV | Name on card | Country Or Region |
      | test543@gmail.com | 4242 4242 4242 4242 | 12/34       | 123 | Test User    | Default           |
    And user clicks on Pay for stripe payment
    Then verify booking is confirmed for the selected time and date
      | expected message1 | expected message2     |
      | Package           | with Automate Topmate |
    And API: user verify payment status
      | booking type | payment status |
      | package      | ongoing        |


  @regression @india
  Scenario: Validating the booking functionality for Package of of topmate.io from public profile in india
    Given user clicks booking service
      | booking type | duration |
      | Package      | None     |
    When user clicks on Buy Package
    And user fills up the booking form for package service with user details
      | Your Name | Email                       | Phone Number |
      | Test_User | test_user_topmate@gmail.com | 1234567890   |
    And user clicks on Buy Now
    And user choose payment type
      | payment mode | payment bank |
      | Netbanking   | IDBI         |
    And user clicks on Pay Now
    And user choose payment status as "Success"
    Then verify booking is confirmed for the selected time and date
      | expected message1 | expected message2     |
      | Package           | with Automate Topmate |
    And API: user verify payment status
      | booking type | payment status |
      | package      | ongoing        |