# Library imports.
from flask import Flask
from json import loads
from re import escape

# Because we need an app.
app = Flask(__name__)

# All routes are defined here.

# User Routes

@app.route("/add_user/<username>")
def add_user(username):
    # escape username
    username = escape(username)
    result = database.add_user(username)
    if result == []:
        return "[]"
    return dumps((result.name, str(result.id), result.score))

@app.route("/get_all_users/")
def get_all_users():
    results = database.get_all_users()
    processed = []
    for result in results:
        n = (result.name, str(result.id), result.score)
        processed.append(n)
    return dumps(processed)

@app.route("/get_user/<username>")
def get_user(username):
    # escape username
    username = escape(username)
    result = database.get_user(username)
    if result == []:
        return "[]"
    return dumps((result.name, str(result.id), result.score))

# Clan Routes

@app.route("/add_clan/<clanname>")
def add_clan(clanname):
    # escape clanname
    clanname = escape(clanname)
    result = database.add_clan(clanname)
    if result == []:
        return "[]"
    return dumps((result.name, str(result.id), result.score))

@app.route("/get_all_clans/")
def get_all_clans():
    results = database.get_all_clans()
    processed = []
    for result in results:
        n = (result.name, str(result.id), result.score)
        processed.append(n)
    return dumps(processed)

@app.route("/get_clan/<clanname>")
def get_clan(clanname):
    # escape clanname
    clanname = escape(clanname)
    result = database.get_clan(clanname)
    if result == []:
        return "[]"
    return dumps((result.name, str(result.id), result.score))

# Award Routes

@app.route("/award_user_points/<username>/<int:points>/")
def award_user_points(username, points):
    # escape username
    username = escape(username)
    result = database.award_user_points(username, points)
    if result == []:
        return "[]"
    return dumps((result.name, str(result.id), result.score))

@app.route("/award_clan_points/<clanname>/<int:points>/")
def award_clan_points(clanname, points):
    # escape clanname
    clanname = escape(clanname)
    result = database.award_clan_points(clanname, points)
    if result == []:
        return "[]"
    return dumps((result.name, str(result.id), result.score))

# Utility Routes

@app.route("/clear_all_records/")
def clear_all_records():
    results = database.clear_all_records()
    return "[]"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

