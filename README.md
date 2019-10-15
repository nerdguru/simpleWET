# simpleWET

simpleWET is an extremely simple client interface for WebEx Teams intended to
be used by automations that want to post notifications to a room but not deal
with the intricacies of the REST API directly.

## Usage
Before using this client, visit the [WebEx Teams API Getting Started](https://developer.webex.com/docs/api/getting-started)
page, login, and obtain a Bearer token.  Then set it as an environment variable
`WET_TOKEN` using something like the following:

```
export WET_TOKEN=<your bearer token>
```

simpleWET contains four methods:

* **listRooms()** - Returns a JSON list of rooms, including the pagination potentially required of multiple REST API calls.
* **findRoom(*string*)** - Calls *listRooms()* and then uses [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) to find potential matches given the passed in *string*.  It takes the best match and sets its room ID to the environment variable `WET_CURRENT_ROOM_ID`.
* **createRoom(*name*)** - Creates a new room named *name* and sets its room ID to the environment variable `WET_CURRENT_ROOM_ID`.
* **createMessage(*message*)** - Writes *message* to the room whose ID is currently in the environment variable `WET_CURRENT_ROOM_ID`.


Using the sample is simple and demonstrated in `usage.py`:
```
```
