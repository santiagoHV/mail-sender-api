import smtplib
from decouple import config

MAIL = config('MAIL')
MAIL_PWD = config('MAIL_PWD')

def send_mail(mail):

    message = 'Subject: {}\n\n{}\n\n{}'.format(mail['subject'], mail['message'], mail['sender'])

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(MAIL, MAIL_PWD)

    server.sendmail('sherrerav@correo.udistrital.edu.co','santiherreravelas@gmail.com', message)

    server.quit()

    print('enviado')

