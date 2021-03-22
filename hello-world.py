import os
from twilio.rest import Client

# Load environment file, assign variables
from dotenv import load_dotenv
load_dotenv()

account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]

# Your Account Sid and Auth Token from twilio.com/console
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+14022679449',
    body='hello world',
    to='+12108486578'
)

print(message.sid)
