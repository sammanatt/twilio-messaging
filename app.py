from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

# Load environment file, assign variables
from dotenv import load_dotenv
load_dotenv()

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]
my_cell = os.environ["my_cell"]

app = Flask(__name__)

# Create a route to handle incoming SMS messages
# This is where the magic happens!
@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    print(f'Incoming message from {request.values.get("From")}: ${request.values.get("Body")}')

    # Here, we're generating TwiML using the Python helper library
    resp = MessagingResponse()
    resp.message("TwilioQuest rules")

    return str(resp)

if __name__ == "__main__":
    app.run(port=8767)
