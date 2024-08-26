import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load the Excel file
df = pd.read_excel('your_file.xlsx')

# Email details
sender_email = "your_email@gmail.com"
sender_password = "your_password"
subject = "Change of Party Date"
message_body = "Hello all!\nThe party will take place this Saturday instead of Sunday.\nSee you there!"

# Set up the SMTP server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)

# Send an email to each address in the 'Email' column
for index, row in df.iterrows():
    receiver_email = row['Email']
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the text message
    msg.attach(MIMEText(message_body, 'plain'))

    server.send_message(msg)
    print(f"Email sent to {receiver_email}")

server.quit()
print("All emails sent successfully.")