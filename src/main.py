from auth.login import AuthManager
from ui.menu import TaskManagerUI

def main():
    print("Welcome to the Task Manager!")
    auth_manager = AuthManager()
    ui = TaskManagerUI(auth_manager)
    ui.display_menu()

if __name__ == "__main__":
    main()