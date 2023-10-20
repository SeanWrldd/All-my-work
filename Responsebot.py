import requests
import random
import time
from ResponseBotResources import links
messenger = "https://discord.com/api/v9/channels/868327278734606377/messages"


a = "1"
b = "2"
c = "3"
header = { 
    'authorization': "your auth code"
} 

url = links["get"]

response = requests.get(url, headers=header)

if response.status_code == 200:
    messages = response.json()
    if messages:
        last_message_timestamp = response.headers.get('Date')
    
else:
    print("Failed")




"""""
person_message = "https://cdn.discordapp.com/avatars/633399581190651934/7ca42c0c747104508dfd5d67f4ee0e3f.webp?size=48"
response = requests.get(person_message)

if response.status_code == 200:
    ranmsg = random.randrange(0,3)
    payload = {'content': ""} 
    payload['content'] = a if ranmsg == 1 else b if ranmsg == 2 else c 
    requests.post(messenger, data=payload, headers = header)




if links["get"] == True:
    ranmsg = random.randrange(0,3)
    payload = {'content': ""} 
    payload['content'] = a if ranmsg == 1 else b if ranmsg == 2 else c 
    requests.post(messenger, data=payload, headers = header)
"""
