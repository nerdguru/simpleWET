import requests
import os
import json

def listRooms():
    # Set up first call
    url = 'https://api.ciscospark.com/v1/rooms'
    headers = {'Authorization': 'Bearer ' + str(os.getenv('WET_TOKEN'))}
    r = requests.get(url, headers=headers)
    retval = r.json()["items"];

    # Make subsequent calls
    numRoomsLastCall = len(r.json()["items"])
    while numRoomsLastCall == 100:
        r = requests.get(r.links["next"]["url"], headers=headers)
        retval = retval + r.json()["items"];
        numRoomsLastCall = len(r.json()["items"])

    # Return result
    return retval
