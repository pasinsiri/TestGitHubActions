import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import argparse

# * configure email and port
PORT = 587
SENDER = 's.mcfarlane14@outlook.com'
RECIPIENTS = ['pasinplp0206@gmail.com', 'pasin.sirirat@gmail.com']
SUBJECT = "Test Sending Email from GitHub Actions"
BODY = """\
Hi!

This is a test email that will be sent via GitHub Actions.
If you receive this email, the automated workflow is run as expected.

Best regards,
An email sender
"""

# * retrieve password
parser = argparse.ArgumentParser(
    prog='EmailSender',
    description='Get a password for an email login',
    epilog='The password is required for the SSL connector'
)
parser.add_argument('-pw', '--password')
args = parser.parse_args()
password = args.password

for recipient in RECIPIENTS:
    # * create a message object
    message = MIMEMultipart()
    message['From'] = SENDER
    message['To'] = recipient
    message['Subject'] = SUBJECT

    # * add the body to the message
    message.attach(MIMEText(BODY, 'plain'))

    # * create a secure SSL context
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(SENDER, password)
    smtp.send_message(message)
    print(f'Email was successfully sent to {recipient}')
    smtp.quit()