#Sending Emails with Python to multiple contact
import os
import smtplib 
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['xxxxxx', 'xxxxxxxxxxxx']
message = EmailMessage()
message['To'] = ', '.join(contacts)
message['From'] = EMAIL_ADDRESS
message['Subject'] = 'Hello, Long time!'
message.set_content('Heres the image you been looking for...')

files = ['me.jpeg', 'me2.jpeg']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    message.add_attachment(file_data, maintype= 'image', subtype= file_type, filename= file_name)

with smtplib.SMTP('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(message)