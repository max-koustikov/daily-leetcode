import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Email credentials and content (will be provided as secrets in GitHub Actions)
sender_email = "your_email@gmail.com"
password = "your_app_password"
recipient_email = "recipient_email@example.com"
subject = "Automated Email from Python"
body = "This is a test email sent every minute."

# Check if it's a new minute
current_minute = datetime.now().minute
if current_minute % 1 == 0:  # Every minute

    # Create the message
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email

    # Establish a secure connection with Gmail's SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message.as_string())

    print("Email sent successfully at", datetime.now())
