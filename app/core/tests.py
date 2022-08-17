import smtplib
from config import settings


def send_email():
    try:
        mailserver = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        print(mailserver.ehlo())
        mailserver.starttls()
        print(mailserver.ehlo())
        mailserver.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        print('Conectado ...')
    except Exception as e:
        print(e)


send_email()
