import requests
import os

def createMessage(roomId, text):
    # Set up call
    url = 'https://api.ciscospark.com/v1/messages'
    headers = {'Authorization': 'Bearer ' + str(os.getenv('WET_TOKEN'))}
    data = {'roomId':roomId,
            'text':text}
    r = requests.post(url, data=data, headers=headers)
    return r.json();
