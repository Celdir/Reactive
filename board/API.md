# Proposed API #

### General Notes ###

A username is always store case-sensitively, but always matched lowercase.

## General User Methods ##

### add_user/`username` ###

Success: user does not exist.
Modifications: creates user in database with username, random UUID, and a score of 0.
Returns: same as `get_user/username`.

Failure: user already exists.
Modifications: none.
Returns: empty list.

### get_all_users ###

Success: hopefully always.
Modifications: none.
Returns: a list of all user rows. List of lists, where the container lists are
in the format of [name, id, score].

### get_user/`username` ###

Success: user exists.
Modifications: none.
Returns: the row of the associated user as a JSON list of [name, id, score].

Failure: user does not exists.
Modifications: none.
Returns: empty list.

## General Clan Methods ##

### add_clan/`clanname` ###

Success: clan does not exist.
Modifications: creates clan in database with clanname, random UUID, and a score of 0.
Returns: same as `get_clan/clanname`.

Failure: clan already exists.
Modifications: none.
Returns: empty list.

### get_all_clans ###

Success: hopefully always.
Modifications: none.
Returns: a list of all clan rows. List of lists, where the container lists are
in the format of [name, id, score].

### get_clan/`clanname` ###

Success: clan exists.
Modifications: none.
Returns: the row of the associated clan as a JSON list of [name, id, score].

Failure: clan does not exist.
Modifications: none.
Returns: empty list.

## Scoring ##

### award_user_points/`username`/`points` ###

Success: clan exists.
Modifications: adds `points` to the current score of `clanname`.
Returns: same as `get_clan/clanname`.

Failure: clan does not exist.
Modifications: none.
Returns: empty list.

### award_user_points/`username`/`points` ###

Success: user exists.
Modifications: adds `points` to the current score of `username`.
Returns: same as `get_user/username`.

Failure: user does not exist.
Modifications: none.
Returns: empty list.

## Utility Methods ##

### clear_all_records ##

Success: always.
Modifications: clears everything, yo.
Returns: empty list.
