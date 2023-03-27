echo ""
#export BROWSER=chrome
echo "Browser: " $BROWSER
echo "URL: " $URL
echo "Yeppee!!!....... UI Automation Started Started in $BROWSER......."
#source venv/bin/activate
behave features -D url=$URL -D browser=$BROWSER -D headless=true -f allure_behave.formatter:AllureFormatter -o reports/json_reports/
allure generate reports/json_reports -o reports/allure_reports --clean
python3 -m utilities.mail_util


