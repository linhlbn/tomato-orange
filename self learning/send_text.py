from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC508a1c2c9c46ef8639d16c7e7746b65b"
# Your Auth Token from twilio.com/console
auth_token  = "03a8c9e54f2e40d06f3378b86f0ec19d"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+358469518960",
    from_="+16084000419",
    body="This message is generated by developer Linh Pham. Well, 1/ EUROPE, US DOLLAR is COMING. 2/ HAPPY ALL YEAR. 3/ FULL of HEALTHY LIFE")

print(message.sid)
