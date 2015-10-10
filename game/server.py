# Library imports.
from flask import Flask
from json import dumps, loads
from re import escape
from uuid import uuid4

# Reactive imports
import reactive
from classes import Game

# Because we need an app.
app = Flask(__name__)

# All routes are defined here.

@app.route("/create_game/<gamemode>/<name>/")
def create_game(gamemode, name):
    reactive.create_game(name, uuid4(), gamemode)
    return "lol"

@app.route("/end_game/<uuid>/")
def end_game(uuid):
    pass

@app.route("/get_all_games/")
def get_all_games():
    games = reactive.get_all_games()
    info = []
    for (id, g) in games:
        info.append({
            "uuid" : g.id,
            "gamemode" : g.gamemode,
            "name" : g.name,
            "users" : g.users,
            "teams" : g.teams,
        })
    return dumps(info)

@app.route("/get_game/<uuid>")
def get_game(uuid):
    g = reactive.get_game(uuid)
    if g == None:
        return "[]"
    info = {
        "uuid" : g.id,
        "gamemode" : g.gamemode,
        "name" : g.name,
        "users" : g.users,
        "teams" : g.teams,
    }
    return dumps(info)

@app.route("/join_game/<username>/<uuid>/")
def join_game(username, uuid):
    pass

@app.route("/leave_game/<username>/<uuid>/")
def leave_game(username, uuid):
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

