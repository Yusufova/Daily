import time


class Routine:
    def init(self, morning_time, lunch_time, evening_time, night_time):
        self.wake_time = morning_time
        self.lunch_time = lunch_time
        self.evening_time = evening_time
        self.night_time = night_time

    def morning(self):
        print(f"now at {self.wake_time} a.m. Good Morning! Do some exercises")
        time.sleep(0.2)
        self.lunch()

    def lunch(self):
        print(f" {self.lunch_time} a.m and lunch time! ")
        self.evening()

    def evening(self):
        print(f"now {self.evening_time} p.m . Good evening! You should do your homeworks!")
        self.night()

    def night(self):
        print(f"now {self.night_time} p.m. Bed time and Good Night!")

obj = Routine("5.00", "12.30", "18.00", "21.35")
obj.morning()