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
    uuid = uuid4()
    reactive.create_game(name, uuid, gamemode)
    return get_game(uuid)

@app.route("/end_game/<uuid>/")
def end_game(uuid):
    pass

@app.route("/get_all_games/")
def get_all_games():
    games = reactive.get_all_games()
    info = []
    for key in games:
        g = games[key]
        users = []
        for u in g.users:
            users.append((u.name, str(u.id), u.current_score))
        info.append({
            "uuid" : str(g.id),
            "gamemode" : g.gamemode,
            "name" : g.name,
            "users" : users,
            "teams" : g.teams,
        })
    return dumps(info)

@app.route("/get_game/<uuid>")
def get_game(uuid):
    g = reactive.get_game(uuid)
    if g == None:
        return "[]"
    users = []
    for u in g.users:
        users.append((u.name, str(u.id), u.current_score))
    info = {
        "uuid" : str(g.id),
        "gamemode" : g.gamemode,
        "name" : g.name,
        "users" : users,
        "teams" : g.teams,
    }
    return dumps(info)

@app.route("/get_sample_game/<uuid>/")
def get_sample_game(uuid):
    info = {
        "uuid" : uuid,
        "gamemode" : "assassins",
        "name" : "Just A Game",
        "users" : ["frank", "steve", "yas"],
        "teams" : []
    }
    return dumps(info)

@app.route("/get_all_samples/")
def get_all_samples():
    info = []
    for i in [1,2,3,4,5]:
        info.append({
            "uuid" : "x",
            "gamemode" : "assassins",
            "name" : "Just A Game",
            "users" : ["frank", "steve", "yas"],
            "teams" : []
        })
    return dumps(info)

@app.route("/join_game/<username>/<uuid>/")
def join_game(username, uuid):
    if reactive.join_game(username, uuid):
        return get_game(uuid)
    return ""
    

@app.route("/leave_game/<username>/<uuid>/")
def leave_game(username, uuid):
    pass

# Assassins Specifc Routes

@app.route("/assassins/target/<uuid>/<name>")
def assassins_target(uuid, name):
    g = reactive.get_game(uuid)
    if g == None or g.gamemode != "assassins" or g.state != PLAYING:
        return ""
    for user in g.users:
        if user == name:
            return user.target.name
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

@app.route("/start_game/<uuid>")
def start_game(uuid):
    if reactive.start_game(uuid):
        return get_game(uuid)
    return ""
