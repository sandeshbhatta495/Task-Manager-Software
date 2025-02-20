class TaskManagerUI:
    def __init__(self, auth_manager):
        self.auth_manager = auth_manager
        self.tasks = {}

    def display_menu(self):
        while True:
            if not self.auth_manager.current_user:
                self.show_auth_menu()
            else:
                self.show_task_menu()

    def show_auth_menu(self):
        print("\n=== Task Manager ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.login()
        elif choice == "2":
            self.register()
        elif choice == "3":
            exit()

    def show_task_menu(self):
        print(f"\n=== Welcome {self.auth_manager.current_user} ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.add_task()
        elif choice == "2":
            self.view_tasks()
        elif choice == "3":
            self.complete_task()
        elif choice == "4":
            self.auth_manager.current_user = None

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        if self.auth_manager.login(username, password):
            print("Login successful!")
        else:
            print("Invalid credentials!")

    def register(self):
        username = input("Choose username: ")
        password = input("Choose password: ")
        if self.auth_manager.register(username, password):
            print("Registration successful!")
        else:
            print("Username already exists!")

    def add_task(self):
        title = input("Task title: ")
        description = input("Task description: ")
        user = self.auth_manager.current_user
        if user not in self.tasks:
            self.tasks[user] = []
        self.tasks[user].append({"title": title, "description": description, "completed": False})
        print("Task added successfully!")

    def view_tasks(self):
        user = self.auth_manager.current_user
        if user not in self.tasks or not self.tasks[user]:
            print("No tasks found!")
            return
        
        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks[user]):
            status = "✓" if task["completed"] else " "
            print(f"{i+1}. [{status}] {task['title']}: {task['description']}")

    def complete_task(self):
        self.view_tasks()
        try:
            task_id = int(input("Enter task number to complete: ")) - 1
            user = self.auth_manager.current_user
            if 0 <= task_id < len(self.tasks[user]):
                self.tasks[user][task_id]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")