echo ""
echo "Browser Type: " $BROWSER
echo "Yeppee!!!....... UI Automation Started Started in $BROWSER......."

behave features -D browser=chrome -D headless=true -f allure_behave.formatter:AllureFormatter -o reports/
#allure serve reports
