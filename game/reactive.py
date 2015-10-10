import requests
from classes import Game, User
from json import loads
import assassins
from uuid import UUID

LB_SERVER = "http://aws1.bitwisehero.com/"

# map from ID to Game
games = {}

def load_user(username):
    url = LB_SERVER + "get_user/%s" % username
    resp = requests.get(url)
    response = loads(resp.text)
    return User(response[0], UUID(response[1]), "none")

def join_game(username, uuid):
    user = load_user(username)
    game = get_game(UUID(uuid))
    if game == None:
        return False
    game.add_user(user)
    return True

def get_all_games():
    return games

def get_game(id):
    for gid in games:
        if id == gid:
            return games[gid]
    return None

def create_game(name, id, gamemode):
    game = Game(name, id, gamemode)
    games[id] = game

def destroy_game(id):
    del games[id]
