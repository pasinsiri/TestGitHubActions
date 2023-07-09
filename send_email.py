import argparse
from functions.email_sender import EmailSender

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

es = EmailSender(
    port=PORT,
    sender=SENDER,
    password=password,
    recipients=RECIPIENTS,
)

es.send_email(
    subject=SUBJECT,
    body=BODY
)