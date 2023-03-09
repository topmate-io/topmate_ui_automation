echo ""
echo "Browser Type: " $BROWSER
export headless_mode=true
echo "Yeppee!!!....... UI Automation Started Started in $BROWSER......."

behave features/login.feature -D browser=$BROWSER

