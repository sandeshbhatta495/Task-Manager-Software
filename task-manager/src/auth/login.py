import json
import os

class AuthManager:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.load_users()

    def load_users(self):
        try:
            with open('../data/users.json', 'r') as f:
                self.users = json.load(f)
        except FileNotFoundError:
            self.users = {}

    def save_users(self):
        with open('../data/users.json', 'w') as f:
            json.dump(self.users, f)

    def register(self, username, password):
        if username not in self.users:
            self.users[username] = password
            self.save_users()
            return True
        return False

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            self.current_user = username
            return True
        return False