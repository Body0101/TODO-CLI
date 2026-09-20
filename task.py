class Task:

    def __init__(self, title, date):
        self.title = title
        self.is_done = False
        self.date = date

    def is_complete(self):
        return self.is_done

    def complete(self):
        self.is_done = True

