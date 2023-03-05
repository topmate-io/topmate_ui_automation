This is a selenium project using Behave[BDD] Framework using PageObject Model Architecture

To run any feature file locally using behave command:
1. general run -> behave /features/login.feature
2. run using tags -> behave /features/login.feature --tags=smoke

How to generate Report after execution?
1. We use allure reporting for that
command -> behave -f allure_behave.formatter:AllureFormatter -o reports/ features

Now we will see the report in allure:
command -> allure serve reports