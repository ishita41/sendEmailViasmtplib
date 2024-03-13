import smtplib
import getpass
from email.mime.text import MIMEText


def send_email():
    sender_address = 'imishitamahajan@gmail.com'
    password = "leuj jjwt pkqc iuno"
    subject = 'AI MAFIA MACHINE LEARNING'
    msg_body = '''Hello everyone Ishita here,'''

    # Server initialization
    server = smtplib.SMTP('smtp.gmail.com', 587)  # this will enable smtp server
    server.starttls()
    server.login(sender_address, password)

    # Draft message body
    msg = MIMEText(msg_body)
    msg['Subject'] = subject
    msg['From'] = sender_address
    msg['To'] = 'imishitamahajan@gmail.com'
    recipients = ['ishita1726.be21@chitkara.edu.in']

    # Send the email
    server.sendmail(sender_address, recipients, msg.as_string())
    server.quit()


send_email()