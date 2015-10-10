import flask

class User:
    def __init__(self, name, id, clan):
        self.name = name
        self.id = id
        self.clan = clan
        self.clan.add_user(self)
        self.total_score = 0
        self.current_score = 0
    
    def set_total_score(self, score):
        self.total_score = score
   
    def set_current_score(self, score):
        self.current_score = score

    def add_score(self, score):
        self.current_score += score

    def subtract_score(self, score):
        self.current_score -= score
    
    def join_clan(self, clan):
        self.leave_clan()
        self.clan = clan
        self.clan.add_user(self)

    def leave_clan(self):
        self.clan.remove_user(self)

    def join_team(self, team):
        self.team = team
        self.team.add_user(self)

    def leave_team(self):
        self.team.remove_user(self)
        self.team = None

    def join_game(self, game):
        self.game = game
        self.game.add_user(self)
    
    # add current score to total score, set current score to 0, and leave the user's current game
    def leave_game(self):
        self.total_score += self.current_score
        self.clan.add_score(self.current_score)
        self.current_score = 0
        self.game.remove_user(self)
        self.game = None

class Clan:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.users = []
        self.gamemodes = []
        self.score = 0

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def add_gamemode(self, gamemode):
        self.gamemodes.append(gamemode)

    def set_score(self, score):
        self.score = score

    def add_score(self, score):
        self.score += score
    
    def subtract_score(self, score):
        self.score -= score
 
class Team:
    def __init__(self, name, id, game):
        self.name = name
        self.id = id
        self.users = []
        self.game = game
        self.score = 0

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def join_game(self, game):
        self.game = game
        for user in self.users:
            user.join_game(self.game)
        self.game.add_team(self)

    def leave_game(self):
        for user in self.users:
            user.leave_game()
            self.remove_user(user)
        self.game.remove_team(self)
        self.game = None

    def set_score(self, score):
        self.score = 0

    def add_score(self, score):
        self.score += score

    def subtract_score(self, score):
        self.score -= score

class Game:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.users = []
        self.teams = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def add_team(self, team):
        self.teams.append(team)

    def remove_team(self, team):
        self.teams.remove(team)

    def game_over(self):
        for team in self.teams:
            team.leave_game()
        for user in self.users:
            user.leave_game()

