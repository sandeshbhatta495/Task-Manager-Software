class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.tasks = []

    def get_username(self):
        return self.username

    def set_password(self, new_password):
        self.password = new_password

    def check_password(self, password):
        return self.password == password

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            return self.tasks.pop(task_id)
        return None

    def __repr__(self):
        return f"User(username={self.username})"