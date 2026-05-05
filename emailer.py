import smtplib
from email.message import EmailMessage

def send_email(to, subject, content):
    msg = EmailMessage()
    msg.set_content(content)
    msg['subject'] = subject
    msg['to'] = to
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('ah13.projects@gmail.com', 'wfdi bmvt jpss svyi')
    server.sendmail("ah13.projects@gmail.com", to, msg.as_string())
    server.quit()

send_email("lopamudra.boston@gmail.com", "Testa", "VIRAT KOHLI")
