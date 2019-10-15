import simpleWET
import os
import json

# Call listRooms, print them out, and print out a count
rooms = simpleWET.listRooms()
print(json.dumps(rooms, indent=4))
print('Number: ' + str(len(rooms)))

# Call findRooms, print out the results
results = simpleWET.findRoom('containers', 70)
print(json.dumps(results, indent=4))

# Create a room
room = simpleWET.createRoom('Test simpleWET room')
print(json.dumps(room, indent=4))

# Write a message to the new room
message = simpleWET.createMessage(room["id"], 'The quick brown fox jumped over the lazy dog')
print(json.dumps(message, indent=4))
