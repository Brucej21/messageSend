import requests
import json
import sys
sys.path.insert(0,'/home/ubuntu/code/uni_cred')
import message

#this is related to telstra sms program, via their dev protal.

def sendSMS():
    ###print ("Please enter your Consumer key:")
    #CONSUMER_KEY = input()
    CONSUMER_KEY = pub
    #print ("Please enter your consumer secret:")
    #CONSUMER_SECRET = input()
    CONSUMER_SECRET = pri
    #another_one = "y"

    # URL = 'https://beta-sapi.telstra.com/v1/oauth/token'
    URL = 'https://sapi.telstra.com/v1/oauth/token'
    data = 'client_id='+CONSUMER_KEY+'&client_secret='+CONSUMER_SECRET+'&grant_type=client_credentials&scope=NSMS'
    print (data)
    print (URL)
    print (data)
    response = requests.post(URL,data=data,headers={'Content-Type':'application/x-www-form-urlencoded'})
    print(response)
    print(response.text)
    authResp = json.loads(response.text)
    #above this line works

    #'Authorization': 'Bearer '+authResp["access_token"]

    headers = {
        'Authorization': 'Bearer '+authResp["access_token"],
        'Content-Type': 'application/json',
    }

    contact = noB
    message = "to eat smelly food is to taste something smelly (excluding cheese) Confucius 122AD"

    sms2 = {"to": contact, "body": message}
    print (sms2)




    #data = '"to": noB, "body": "Sibling reminder app: says ... dont forget to pick up ur wonderful sister at 4pm'
    #print (data)

    #sent = requests.post('https://tapi.telstra.com/v2/messages/sms', headers=headers, data=data)
    sent = requests.post('https://tapi.telstra.com/v2/messages/sms', headers=headers, data=json.dumps(sms2).encode('utf-8'))

    #print(sent)


setting = dict()
pub = message.pubkey
pri = message.prikey
noB = message.noB


sendSMS()
