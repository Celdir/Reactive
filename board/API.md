# Proposed API #

## add_user/<username> ##

Success: user does not exist.
Modifications: creates user in database with username, random UUID, and a score of 0.
Returns: same as `get_user/<username>`.

Failure: user already exists.
Modifications: none.
Returns: empty list.

## get_user/<username> ##

Success: user exists.
Modifications: none.
Returns: the row of the associated user as a JSON list of [name, id, score].

Failure: user does not exists.
Modifications: none.
Returns: empty list.

## get_all_users ##

Success: hopefully always.
Modifications: none.
Returns: a list of all user rows. List of lists, where the container lists are
in the format of [name, id, score].

Failure: hopefully never.
Modifications: none.
Returns: complete and utter sadness.
