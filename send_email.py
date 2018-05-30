import smtplib

import config

def send_mail(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject : {} \n\n {}'.format(subject,msg)
        server.sendmail(config.EMAIL_ADDRESS, config.RECEIVER_EMAIL, message)
        server.quit()
        print('Success!! Email sent')
    except:
        print('Email failed to send.')

subject = 'Automated Email Subject'  #Put the subject of the email you want to send.

msg = 'This is a test message for a test email.'  # Here put the actual message of the email.

send_mail(subject, msg)
