import smtplib
import json
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender():
    def __init__(self, port:int, sender:str, password:str, recipients:list, email_host:str = None) -> None:
        self.port = port
        self.sender = sender
        self.password = password
        self.recipients = recipients
        self.host_mapper = self._get_host_mapper()
        self.email_host = self._get_email_host(email_host)

    def _get_host_mapper(self):
        with open('./config/smtp_domain_mapper.json', 'r') as f:
            host_mapper = json.load(f)
            return host_mapper

    def _get_email_host(self, host):
        if host is None:
            sender_domain = self.sender.split('@')[-1].split('.')[0]
            logging.info(f"Host is not specified. Extract domain from the sender's email\nThe domain is {sender_domain}")
            smtp_host = self.host_mapper.get(sender_domain)
            if smtp_host is None:
                raise ValueError('Domain not found, if it is a newly added domain, please update the smtp_domain_mapper.json')
            return smtp_host
        else:
            return host

    def send_email(self, subject:str, body:str):
        for recipient in self.recipients:
            # * create a message object
            message = MIMEMultipart()
            message['From'] = self.sender
            message['To'] = recipient
            message['Subject'] = subject

            # * add the body to the message
            message.attach(MIMEText(body, 'plain'))

            # * create a secure SSL context
            smtp = smtplib.SMTP(self.email_host, port=self.port)
            smtp.starttls()
            smtp.login(self.sender, self.password)
            smtp.send_message(message)
            print(f'Email was successfully sent to {recipient}')
            smtp.quit()