

from distutils.command.clean import clean
import os

from flask import (
    Flask,
    flash,
    render_template,
    redirect,
    request,
    url_for
)
from twilio.rest import Client

app = Flask(__name__)
app.secret_key = "This is a very secret key"
client = Client('ACb380be3508589452a1da517faebbc427','3b97cea052dce38f55d8f76d3b38b289')

def get_sent_messages():
    messages = client.messages.list()
    return messages

def send_message(to, body):
    pass

@app.route('/', methods=['GET'])
def index():
    messages = get_sent_messages()
    return render_template('index.html', messages = messages)

@app.route('/add-compliment', methods=['POST'])
def add_compliment():
    sender = request.values.get('sender', "Someone")
    receiver = request.values.get('receiver', 'Someone')
    compliment = request.values.get('compliment', 'wonderful')
    to = request.values.get('to')
    body = f'{sender} says: {receiver} is {compliment}. see more compliments at {request.url_root}'
    send_message(to, body)
    flash('Your message was sent successfully.')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()