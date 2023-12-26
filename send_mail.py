import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Email Credentials and Content (will be provided as secrets in GitHub Actions)
sender_email = "zachhefferman@gmail.com"  # Replace with your email address
password = "kmhv iwkx wbod pimy"  # Replace with your app password
recipient_email = "max.koustikov@gmail.com"  # Replace with recipient email
subject = "Automated Email from Python"
body = "This is a test email sent at 8:30 PM."

# Get current time and calculate target time
now = datetime.now()
target_time = now.replace(hour=20, minute=30)

# Check if it's the designated time to send the email
if target_time - now <= timedelta(seconds=60):

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
    print("Not the designated time to send the email. Current time:", now)
