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
        print(f"Your current streak for '{self.name}' is: {self.streak}")

    def get_completion_rate(self):
        pass


habit1 = Habit('Run', 'Go for a run')
habit1.mark_complete(datetime.now().date())


class User():
    def __init__(self, username):
        self.username = username
        self.habits = []

    def add_habit():
        pass

    def remove_habit():
        pass

    def get_habit(name):
        pass

    def view_summary():
        pass


class HabitTrackerApp():
    def __init__(self, users):
        self.users = users

    def load_data():
        pass

    def save_data():
        pass

    def run():
        pass

    def login():
        pass

    def register():
        pass

    def display_menu():
        print("----------\nWelcome to the Habit Tracker\n---------")


habitTracker = HabitTrackerApp("guest")
habitTracker.display_menu()
