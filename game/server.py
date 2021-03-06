# Library imports.
from flask import Flask
from json import dumps, loads
from re import escape
from uuid import uuid4, UUID

# Reactive imports
import reactive
from classes import Game
from assassins import Assassins

# Because we need an app.
app = Flask(__name__)

# Game States
PREGAME = 0
PLAYING = 1
ENDGAME = 2

# All routes are defined here.

@app.route("/create_game/<gamemode>/<name>/")
def create_game(gamemode, name):
    uuid = str(uuid4())
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
            users.append((u.name, str(u.id), u.current_score, u.alive))
        info.append({
            "uuid" : str(g.id),
            "gamemode" : g.gamemode,
            "name" : g.name,
            "users" : users,
            "teams" : g.teams,
            "active" : g.state == PLAYING
        })
    return dumps(info)

@app.route("/get_game/<uuid>")
def get_game(uuid):
    g = reactive.get_game(uuid)
    if g == None:
        return "[]"
    users = []
    for u in g.users:
        users.append((u.name, str(u.id), u.current_score, u.alive))
    info = {
        "uuid" : str(g.id),
        "gamemode" : g.gamemode,
        "name" : g.name,
        "users" : users,
        "teams" : g.teams,
        "active" : g.state == PLAYING
    }
    return dumps(info)

@app.route("/get_game_players/<uuid>")
def get_game_players(uuid):
    g = reactive.get_game(uuid)
    if g == None:
        return "[]"
    users = []
    for u in g.users:
        users.append((u.name, str(u.id), u.current_score, u.alive))
    return dumps(users)

@app.route("/join_game/<username>/<uuid>/")
def join_game(username, uuid):
    if reactive.join_game(username, uuid):
        return get_game(uuid)
    return ""

@app.route("/leave_game/<username>/<uuid>/")
def leave_game(username, uuid):
    pass

# Assassins Specifc Routes

@app.route("/assassins/kill/<uuid>/<killer>/<target>")
def assassins_kill(uuid, killer, target):
    g = reactive.get_game(uuid)
    if g == None or g.gamemode != "assassins" or g.state != PLAYING:
        return "NOPE"
    found_killer = False
    found_target = False
    for user in g.living:
        if user.name == killer:
            found_killer = True
            killer_ref = user
        if user.name == target:
            found_target = True
            target_ref = user
    if found_killer and found_target and killer_ref.target == target_ref:
        g.win(killer_ref.id)
        g.kill(target_ref.id)
        return "Success"
    else:
        return "Failure"

    

@app.route("/assassins/target/<uuid>/<name>")
def assassins_target(uuid, name):
    g = reactive.get_game(uuid)
    if g == None or g.gamemode != "assassins" or g.state != PLAYING:
        return "NOPE"
    for user in g.living:
        if user.name == name:
            return "\"%s\"" % user.target.name
    return "NAH"

@app.route("/start_game/<uuid>")
def start_game(uuid):
    if reactive.start_game(uuid):
        return get_game(uuid)
    return ""

# Hard Coded Sample Game
def sample():
    reactive.create_game("Bob", '7d59d944-b051-4b9c-bf9f-a3fd4c1c541a', "assassins")
    for user in reactive.load_all_users():
        reactive.join_game(user.name, '7d59d944-b051-4b9c-bf9f-a3fd4c1c541a')

if __name__ == "__main__":
    sample()
    app.run(host="0.0.0.0", port=80, debug=True)

