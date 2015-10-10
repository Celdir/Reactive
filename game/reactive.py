import requests
from classes import Game
import assassins

# map from ID to Game
games = {}

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
