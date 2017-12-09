#!/usr/bin/python
# coding=utf-8
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC373af3a0589b578f38c6471d93e32c46"
# Your Auth Token from twilio.com/console
auth_token = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+6592777992",
    from_="+16172945098",
    body="Hello from Python!")

print(message.sid)
