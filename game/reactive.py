import flask
import requests
import classes
import assassins

games_map = {}

def create_game(name, id, gamemode):
    game = Game(name, id, gamemode)
    games_map[id] = game

def destroy_game(id):
    del games_map[id]

def get_game(id):
    return games_map[id]
