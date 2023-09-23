from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# Store RSVP responses in a list (in-memory storage for simplicity)
rsvp_responses = []

@app.route('/')
def index():
    return open('birthday.html').read()

@app.route('/log_rsvp', methods=['POST'])
def log_rsvp():
    name = request.form.get('name')
    response = request.form.get('response')

    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log the name, response, and timestamp to the log.txt file
    with open('log.txt', 'a') as log_file:
        log_file.write(f"Name: {name}, Response: {response}, Timestamp: {timestamp}\n")

    rsvp_responses.append({'name': name, 'response': response, 'timestamp': timestamp})

    return 'RSVP logged successfully.'

@app.route('/get_rsvp_responses')
def get_rsvp_responses():
    return {'responses': rsvp_responses}

if __name__ == '__main__':
    app.run(debug=True)
