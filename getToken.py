import requests
import json
import sys
sys.path.insert(0,'/home/ubuntu/code/uni_cred')
import message

#this is related to telstra sma program, via their dev protal.
#precondition all keys have been set up. 

def sendSMS():
    ###print ("Please enter your Consumer key:")
    #CONSUMER_KEY = input()
    CONSUMER_KEY = pub
    #print ("Please enter your consumer secret:")
    #CONSUMER_SECRET = input()
    CONSUMER_SECRET = pri
    #another_one = "y"

    #while another_one != "n":
    #print ("Enter the recipients number:")
    contact = noB
    #contact = input()
    #print ("Enter your message:")
    #message = "tesing wow"

    # URL = 'https://beta-sapi.telstra.com/v1/oauth/token'
    URL = 'https://sapi.telstra.com/v1/oauth/token'
    data = 'client_id='+CONSUMER_KEY+'&client_secret='+CONSUMER_SECRET+'&grant_type=client_credentials&scope=NSMS'
    print (URL)
    print (data)
    #refernce :   https: // dev.telstra.com / content / messaging - api - getting - started
    response = requests.post(URL,data=data,headers={'Content-Type':'application/x-www-form-urlencoded'})
    print(response)
    print(response.text)
    #above this line prints temporaty token. Can be used to get phone number for the first call



setting = dict()
pub = message.pubkey
pri = message.prikey
noB = message.noB

print (pub)
print (pri)
print (noB)


sendSMS()
