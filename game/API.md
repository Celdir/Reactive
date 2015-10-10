# Proposed API #

## General Game Methods ##

### create_game/`gamemode`/`name` ###

Success: `gamemode` is valid.
Modifications: creates game of type `gamemode` with name `name`.
Returns: same as `get_game/uuid` of the newly created game.

Failure: `gamemode` is invalid.
Modifications: none.
Returns: empty list.

### end_game/`uuid` ###

Success: `uuid` is a valid game.
Modifications: ends game.
Returns: empty list. *TODO FIX THIS*

Failure: `uuid` is not a valid game.
Modifications: none.
Returns: empty list.

### get_all_games ###

Success: always.
Modifications: none.
Returns: list of all games, where each game is a JSON string in the same format
as `get_game/uuid`.

### get_game/`uuid` ###

Success: `uuid` refers to a valid game.
Modifications: none.
Returns: returns game as a JSON string.

Failure: `uuid` does not refer to a valid game.
Modifications: none.
Returns: empty list.

### join_game/`username`/`uuid` ###

Success: `username` is valid and `uuid` refers to a valid game.
Modifications: adds user to selected game.
Returns: same as `get_game/uuid`.

Failure: `username` is invalid.
Modifications: none.
Returns: empty list.

Failure: `uuid` is invalid.
Modifications: none.
Returns: empty list.

### leave_game/`username`/`uuid` ###

Success: `username` is valid, `uuid` refers to a valid game, and user is in game.
Modifications: removes user from game.
Returns: same as `get_game/uuid`.

Failure: `username` is invalid.
Modifications: none.
Returns: empty list.

Failure: `uuid` is invalid.
Modifications: none.
Returns: empty list.

Failure: user is not in game.
Modifications: none.
Returns: empty list.

## Assassins Specific Methods ##

### assassins/target/`uuid`/`name` ###

Success: `uuid` is a valid game and `name` is a user in that game.
Modification: none.
Returns: Name of target for `name` in game `uuid`.

Failure: `uuid` is not a game.
Modifications: none.
Returns: nothing.

Failure: `name` is not in `uuid`.
Modifications: none.
Returns: nothing.

