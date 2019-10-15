from .listRooms import listRooms
from fuzzywuzzy import fuzz

def sortScore(item):
    return item['score']*-1

def findRoom(string, threshold):
    rooms = listRooms()
    retval = []
    for room in rooms:
        score = fuzz.partial_ratio(string, room["title"])
        if score >= threshold:
            hit = {}
            hit['score'] = score
            hit['room'] = room
            retval.append(hit)

    retval.sort(key=sortScore)
    return retval
