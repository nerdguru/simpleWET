import requests
import os

def createRoom(title):
    # Set up call
    url = 'https://api.ciscospark.com/v1/rooms'
    headers = {'Authorization': 'Bearer ' + str(os.getenv('WET_TOKEN'))}
    data = {'title':title}
    r = requests.post(url, data=data, headers=headers)
    return r.json();
