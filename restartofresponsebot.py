import requests
import random
import time
from ResponseBotResources import links

a = "1"
b = "2"
c = "3"
date = []

messenger = "https://discord.com/api/v9/channels/1132654960903991358/messages"

header = { 
    'authorization': "NTk3MTY4OTUxNTYyMDc2MTY2.Gq4CkY.zKmIOsFlSW_cKMgI2_HGApHw5PtZXZSNZD4TjE"
}

message_sending = requests.post("https://discord.com/api/v9/channels/1132654960903991358/messages")
message_recieving = requests.get("https://cdn.discordapp.com/avatars/597168951562076166/43ed96acce0581609f4c7b1609ce4c57.webp?size=48")

if message_recieving.status_code() == 200 and message_sending.status_code() != 200:
    payload = {"content",''}

    message_sending
