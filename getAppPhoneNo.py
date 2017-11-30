# this is a once off action per app.

import requests

#precondition a call has been made to get the token see gettoken.py

headers = {
    'authorization': 'insertTokenHere',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
}

data = '{\n  "activeDays":30,\n  "notifyURL":"http://example.com/callback",\n  "callbackData":\n  {\n    "anything":"some data"\n  }\n}'

response = requests.post('https://tapi.telstra.com/v2/messages/provisioning/subscriptions', headers=headers, data=data)

print(response.text)
