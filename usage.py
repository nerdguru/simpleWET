import simpleWET
import os
import json

print('My token: ' + os.environ['WET_TOKEN'])
# rooms = simpleWET.listRooms()
# print(json.dumps(rooms, indent=4))
# print('Number: ' + str(len(rooms)))
results = simpleWET.findRoom('GPO DevNet', 70)
print(json.dumps(results, indent=4))
