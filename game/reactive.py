import requests
from classes import Game, User
from json import loads
from assassins import Assassins
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
    game = get_game(uuid)
    if game == None:
        return False
    game.add_user(user)
    return True

def get_all_games():
    return games

def get_game(id):
    id = UUID(id)
    for gid in games:
        if id == gid:
            return games[gid]
    return None

def start_game(uuid):
    game = get_game(uuid)
    if game == None:
        return False
    game.start_game()
    return True

def create_game(name, id, gamemode):
    id = UUID(id)
    game = Assassins(name, id)
    games[id] = game

def destroy_game(id):
    del games[id]

