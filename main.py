from datetime import datetime


class Habit():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.streak = 0
        self.dates_completed = []

    def mark_complete(self, date):
        if date not in self.dates_completed:
            self.dates_completed.append(date)
            print(f"{self.name} completed on: {date}")
            streak += 1
        else:
            print("You've already completed this habit today!")

    def reset_streak(self):
        ex_streak = self.streak
        self.streak = 0
        print(
            f"Your streak for '{self.name}' has been reset from {ex_streak} to 0")

    def get_streak(self):
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
        pass
