from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'

fromNumber = '+2673824521'
toNumber = '+973790997'

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Come check out my website!",
                     from_=fromNumber,
                     to=toNumber
                 )

print(message.sid)
