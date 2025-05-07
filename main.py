import json
from datetime import datetime, date


class Habit():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.streak = 0
        self.dates_completed = []

    def mark_complete(self):
        if date.today() not in self.dates_completed:
            self.dates_completed.append(date.today())
            print(f"{self.name} completed on: {date.today()}")
        else:
            print("You've already completed this habit today!")

    def reset_streak(self):
        confirm = input(
            f"Are you sure you want to reset your {self.streak} day streak? [y/n]")
        if confirm.lower() == 'y':
            ex_streak = self.streak
            self.dates_completed = []
            print(
                f"Your streak for '{self.name}' has been reset from {ex_streak} to 0")
        elif confirm.lower() == 'n':
            print("Okay, streak will not be reset")
        else:
            print('Please enter either y or n')

    def get_streak(self):
        self.streak = 0
        self.dates_completed = sorted(self.dates_completed)
        for date in self.dates_completed:
            self.streak += 1
        print(f"\nYour current streak for '{self.name}' is: {self.streak}")

    def get_completion_rate(self):
        if not self.dates_completed:
            print("\nNo completions yet")
            return
        start_date = min(self.dates_completed)
        today = date.today()
        total_days = (today - start_date).days + 1
        completed_days = len(self.dates_completed)
        return f"\nYou have completed {completed_days} out of {total_days}"


class User():
    def __init__(self, username):
        self.__username = username
        self.__habits = []

    def find_habit(self, name):
        for habit in self.__habits:
            if habit.name == name:
                return habit
        print("Habit not found")

    def add_habit(self):
        habit = input("Please enter a name for your habit: ")
        description = input("Please enter a description: ")
        habit = Habit(habit, description)
        self.__habits.append(habit)

    def remove_habit(self, name):
        habit = self.find_habit(name)
        self.__habits.remove(habit)

    def view_summary(self):
        for habit in self.__habits:
            if habit.dates_completed:
                last_completed = sorted(habit.dates_completed)[-1]
                print(f"\n{habit.name} last completed on {last_completed}")
            else:
                print(f"\n{habit.name} has not yet been completed")

    def get_username(self):
        username = self.__username
        return username


class HabitTrackerApp():
    def __init__(self):
        self.users = []

    def load_data(self):
        try:
            with open("habit_data.json", "r") as file:
                data = json.load(file)

            for user_data in data:
                user = User(user_data["username"])
                for habit_info in user_data["habits"]:
                    habit = Habit(habit_info["name"],
                                  habit_info["description"])
                    habit.dates_completed = [
                        datetime.strptime(d, "%Y-%m-%d").date()
                        for d in habit_info["dates_completed"]
                    ]
                    user._User__habits.append(habit)
                self.users.append(user)

        except FileNotFoundError:
            print("\nNo saved data found. Starting fresh.")

    def save_data(self):
        data = []
        for user in self.users:
            user_data = {
                "username": user.get_username(),
                "habits": []
            }
            for habit in user._User__habits:
                habit_data = {
                    "name": habit.name,
                    "description": habit.description,
                    "dates_completed": [d.isoformat() for d in habit.dates_completed]
                }
                user_data["habits"].append(habit_data)
            data.append(user_data)

        with open("habit_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def run(self):
        self.load_data()
        print("-----------------------------------\nWELCOME TO EVIE'S HABIT TRACKER APP\n-----------------------------------")
        choice = 0
        while choice not in [1, 2, 3]:
            self.display_menu()
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.register()
                choice = 0

            elif choice == 2:
                self.login()

            elif choice == 3:
                print("\nProgram terminating...")

            else:
                print("\nPlease enter a valid choice\n")

    def login(self):
        userName = input("Please enter your username: ")
        for user in self.users:
            if user.get_username() == userName:
                current_user = user
                choice = 0
                while choice not in [1, 2, 3, 4, 5, 6, 7]:
                    self.display_loggedin_menu()
                    choice = int(input("Please enter your choice: "))
                    if choice == 1:
                        current_user.view_summary()
                        choice = 0

                    elif choice == 2:
                        current_user.add_habit()
                        choice = 0

                    elif choice == 3:
                        habit_name = input("\nWhich habit did you complete? ")
                        habit = current_user.find_habit(habit_name)
                        if habit:
                            habit.mark_complete()
                        choice = 0

                    elif choice == 4:
                        habit_name = input(
                            "\nWhich habit streak do you want to view? ")
                        habit = current_user.find_habit(habit_name)
                        if habit:
                            habit.get_streak()
                        else:
                            print("Habit not found")
                        choice = 0

                    elif choice == 5:
                        habit_name = input(
                            "\nWhich habit do you want to remove? ")
                        current_user.remove_habit(habit_name)
                        choice = 0

                    elif choice == 6:
                        habit_name = input(
                            "\nWhich habit do you want the completion rate for? ")
                        habit = current_user.find_habit(habit_name)
                        if habit:
                            print('\n', habit.get_completion_rate())

                        choice = 0

                    elif choice == 7:
                        self.save_data()
                        print("Progress saved. Logging out.")
                        return

                    else:
                        print("Please enter a valid number")

                print("Username not found")

    def display_loggedin_menu(self):
        print(
            "\n-----------------------------\nPlease select one of the \nfollowing options:\n-----------------------------")
        print(
            "1. View habits\n2. Add new habit\n3. Mark habit complete\n4. View streak\n5. Delete habit\n6. View completion rate\n7. Save and Logout\n-----------------------------")

    def register(self):
        userName = input("Please enter a username: ")
        userName = User(userName)
        self.users.append(userName)

    def display_menu(self):
        print(
            "Please select one of the \nfollowing options:\n-----------------------------")
        print("1. Register new user\n2. Log in\n3. Quit\n-----------------------------")


# # MAIN LOOP
habitTracker = HabitTrackerApp()
habitTracker.run()
