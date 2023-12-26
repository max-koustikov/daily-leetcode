import smtplib
from email.mime.text import MIMEText

# Email credentials and content
sender_email = "zachhefferman@gmail.com"  # Replace with your email address
password = "kmhv iwkx wbod pimy"  # Replace with your email password
recipient_email = "max.koustikov@gmail.com"  # Replace with recipient email
subject = "Automated Email from Python"
body = "This is a test email sent using Python."

# Create the message
message = MIMEText(body)
message['Subject'] = subject
message['From'] = sender_email
message['To'] = recipient_email

# Establish a secure connection with Gmail's SMTP server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient_email, message.as_string())

print("Email sent successfully!")
