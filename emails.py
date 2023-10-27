# Python script to send personalized emails to a list of recipients
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_personalized_email(sender_email, sender_password, recipients, subject, body):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    for recipient_email in recipients:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message.attach(MIMEText(body, 'plain'))
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
