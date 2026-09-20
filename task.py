from datetime import datetime


class Task:

    def __init__(self):
        self.title = ""
        self.check = False
        self.date = datetime.now()

    def enter_title(self, title):
        self.title = title.title()

    def is_complete(self):
        return self.check

    def completed(self):
        if not self.check:
            self.check = True

    def enter_datetime(self, year, month, day=0, hour=0, minute=0):

        self.date = datetime(
            year=year,
            month=month,
            day=day,
            hour=hour,
            minute=minute,
        )
