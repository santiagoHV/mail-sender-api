from flask import Flask, request
from flask_cors import CORS
import mailer

app = Flask(__name__)
CORS(app)

@app.route('/send-mail', methods=['POST'])
def send_mail():
    mail = {
        'message': request.json['message'],
        'subject': request.json['subject'],
        'sender': request.json['sender'],
    }
    mailer.send_mail(mail)

    return 'Mail sent'
    

@app.route('/')
def index():
    return 'Hello, mailer with flask, by Santiago Herrera'


if __name__ == '__main__':
    app.run(port=5000, debug=True)