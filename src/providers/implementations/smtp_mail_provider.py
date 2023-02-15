from providers.mail_provider import IMailProvider
from providers.mail_provider import IMessage

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
from dotenv import load_dotenv

load_dotenv()

class SMTPMailProvider(IMailProvider):

  def __init__(self):
    self._smtp_port = os.getenv('MAIL_PORT')
    self._smtp_host = os.getenv('MAIL_HOST')
    self._smtp_password = os.getenv('MAIL_PASSWORD')
  
  def send_mail(self, message: IMessage) -> None:
    server = smtplib.SMTP(self._smtp_host, self._smtp_port)
    server.starttls()

    server.login(message.by.email, self._smtp_password)

    mail_message = MIMEMultipart()
    
    mail_message['From'] = message.by.email
    mail_message['Subject'] = message.subject

    mail_message['To'] = message.to.email
    mail_message.attach(MIMEText(message.body, 'html'))

    server.sendmail(message.by.email, message.to.email, mail_message.as_string())

    server.quit()
    