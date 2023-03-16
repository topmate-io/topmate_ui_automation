import smtplib
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from datetime import datetime
from typing import List
from zoneinfo import ZoneInfo

from .report_util import ReportUtil
from .util_helper import UtilHelper


def generate_mailer_body(browser, sender_email_id, receiver__email_id_list: List[str]) -> str:
    """This Method returns Email message Subject, mail Body of the mail"""
    current_time = datetime.now(tz=ZoneInfo('Asia/Kolkata')).strftime('%d/%m/%y %I:%M %p')
    subject = f"Automation Status | Browser: {browser} | {current_time}"
    allure_report_path = ReportUtil.upload_report_to_S3()
    print(allure_report_path)
    body = f"""
    <h3>Automation Run is completed.</h3>
    Please find the REPORT <a href="{allure_report_path}">HERE.</a><br>
    <p style="font-size:15px">Thanks & Regards,<br>
    Automation Team</p>
    """

    em = EmailMessage()
    html_body = MIMEText(body, 'html')
    em['From'] = sender_email_id
    em['To'] = ", ".join(receiver__email_id_list)
    em['Subject'] = subject
    em.set_content(html_body)
    return em.as_string()


def send_mail(browser: str, sender_email_id: str, sender_email_password: str, receiver__email_id_list: List[str]):
    """This Method sends mail"""
    try:
        print('sending mail')
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender_email_id, sender_email_password)
            email_subject = generate_mailer_body(browser.upper(), sender_email_id, receiver__email_id_list)
            smtp.sendmail(sender_email_id, receiver__email_id_list, email_subject)
        print(f"Mail successfully sent to : {receiver__email_id_list}")
    except Exception as e:
        print(f"Exception occurred while sending mail: {e}")


def send_final_report_to_mail():
    filepath = 'test_data/creds.json'
    json_data = UtilHelper.read_JSON(filepath)
    sender_email_id = json_data.get('gmail').get('sender').get('email_id')
    sender_password = json_data.get('gmail').get('sender').get('password')
    receiver_email_id_list = json_data.get('gmail').get('receiver')
    browser = UtilHelper.get_specific_env_var('BROWSER').upper()

    send_mail(browser, sender_email_id, sender_password, receiver_email_id_list)


send_final_report_to_mail()
