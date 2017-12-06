#!/usr/bin/python
# coding=utf-8
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC373af3a0589b578f38c6471d93e32c46"
# Your Auth Token from twilio.com/console
auth_token = "a1158797b1e988414539a980b67d8954"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309",
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)
