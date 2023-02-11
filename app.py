from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
from pathlib import Path
import ssl
import smtplib
import os
from dotenv import load_dotenv
load_dotenv('.env')

""" Define sender email and app password in Google apps"""
sender_email = 'rambdrpun@gmail.com'
app_password = os.getenv('APP_PASSWORD')

""" Temporary email generated from this link https://temp-mail.org/en/ """
receiver_email = 'pelipig134@aosod.com'

subject = "Testing Python Email Sender"


""" Plain text body """
# body = """
# We are testing python script to send email.
# """

# Load HTML email template using Path module
template = Template(Path("template.html").read_text())
body = template.substitute({'name':'John'})

""" Create an instance of EmailMessage """
em = MIMEMultipart()
em['from'] = sender_email
em['to'] = receiver_email
em['subject'] = subject

# Plain text email body
# em.set_content(body)

# HTML email body
em.attach(MIMEText(body,'html'))

# Connect to GMAIL SMTP server and send email
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender_email, app_password)
    smtp.sendmail(sender_email, receiver_email, em.as_string())
