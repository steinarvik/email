import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def send_birthday_wish(receiver_email, sender_email, sender_password, birthday):
    current_date = datetime.date.today()
    birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()

    if current_date != birthday_date:
        print("Today is not the birthday.")
        return

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Happy Birthday!"

    # Create the body of the message
    body = "Wishing you a wonderful day! Happy Birthday!"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a secure session with Gmail's outgoing SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to the server
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(msg)

        print("Successfully sent birthday wish email to %s" % receiver_email)

    except Exception as e:
        print("Failed to send email: %s" % str(e))

    finally:
        server.quit()

# Usage example
receiver_email = 'receiver@example.com'
sender_email = 'your-email@gmail.com'
sender_password = 'your-password'
birthday = '2024-4-1'  # Set the birthday date in YYYY-MM-DD format

send_birthday_wish(receiver_email, sender_email, sender_password, birthday)