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
* **findRoom(*string*, *threshold*)** - Calls *listRooms()* and then uses [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)'s `token_sort_ratio()` to find potential matches given the passed in *string*, returning an ordered list for any that score above *threshold*.
* **createRoom(*name*)** - Creates a new room named *name*.
* **createMessage(*roomId*, *message*)** - Writes *message* to the room whose ID is *roomId*.


Using the sample is simple and demonstrated in `usage.py`:
```
```
