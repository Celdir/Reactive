from flask import Flask
import requests
from classes import User, Team, Game
from random import shuffle
from json import loads

app = Flask(__name__)

class Assassins(Game):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.users = []
        self.teams = []

    def add_user(self, user):
        user.alive = True
        self.users.append(user)

    def start_game(self):
        shuffle(self.users)
        for counter, user in enumerate(self.users):
            if counter == len(self.users)-1:
                self.users[counter].target = self.users[0]
            else:
                self.users[counter].target = self.users[counter+1]

    def win(self, id):
        for user in self.users:
            if user.id == id:
                user.add_score(1)
                return

    def kill(self, id):
        for counter, user in enumerate(self.users):
            if user.id == id:
                user.alive = False
                if counter == len(self.users)-1:
                    self.users[counter-1].target = self.users[0]
                else: 
                    self.users[counter-1].target = self.users[counter+1]
                user.leave_game()

        if len(self.users) == 1:
            self.game_over()
