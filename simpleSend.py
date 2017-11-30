#this is a simple send example
#precondition is that a token has been created
'''
AccessToken="Access Token"
Dest="Destination number"
curl -X post -H "Authorization: Bearer $AccessToken" \
  -H "Content-Type: application/json" \
  -d '{ "to":"$Dest", "body":"Test Message" }' \
  https://tapi.telstra.com/v2/messages/sms
'''

import requests


headers = {
    'Authorization': 'Bearer insertTokenHere',
    'Content-Type': 'application/json',
}

data = '{ "to":"+614phonenumber", "body":"hello world" }'

sent = requests.post('https://tapi.telstra.com/v2/messages/sms', headers=headers, data=data)


print (sent)
