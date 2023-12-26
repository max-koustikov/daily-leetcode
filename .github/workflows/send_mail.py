import smtplib
from email.mime.text import MIMEText
import datetime
import os

# Email credentials and content (will be provided as secrets in GitHub Actions)
sender_email = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("EMAIL_PASSWORD")
recipient_email = os.environ.get("RECIPIENT_EMAIL")
subject = "Automated Email from Python"
body = "This is a test email sent at 8:30 PM."

# Check if it's the correct time to send the email
current_time = datetime.datetime.now().time()
if current_time.hour == 20 and current_time.minute == 30:

    # Create the message
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email

    # Establish a secure connection with Gmail's SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message.as_string())

    print("Email sent successfully at 8:30 PM!")
else:
    print("Not the designated time to send the email.")
