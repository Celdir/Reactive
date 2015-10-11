from flask import Flask
import requests
from classes import Game
from random import shuffle
from json import loads

app = Flask(__name__)

# Game States
PREGAME = 0
PLAYING = 1
ENDGAME = 2

class Assassins(Game):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.state = PREGAME
        self.gamemode = "assassins"
        self.users = []
        self.living = []
        self.teams = []

    def add_user(self, user):
        u = user.join_game(self)
        self.users.append(u)
        self.living.append(u)
        self.living[-1].alive = True

    def start_game(self):
        self.state = PLAYING
        shuffle(self.living)
        for counter, user in enumerate(self.living):
            if counter == len(self.living)-1:
                self.living[counter].target = self.living[0]
            else:
                self.living[counter].target = self.living[counter+1]

    def win(self, id):
        for user in self.living:
            if user.id == id:
                user.add_score(1)
                return True
        return False

    def kill(self, id):
        for counter, user in enumerate(self.living):
            if user.id == id:
                user.alive = False
                if counter == len(self.living)-1:
                    self.living[counter-1].target = self.living[0]
                else: 
                    self.living[counter-1].target = self.living[counter+1]
                self.remove_user(user)

        if len(self.living) == 1:
            self.game_over()

