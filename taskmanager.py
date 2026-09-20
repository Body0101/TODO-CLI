from datetime import datetime
from task import Task
# import json


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, year, month, day, hour=0, minute=0):
        task = Task(
            title=title.title(),
            date=datetime(year, month, day, hour, minute),
        )

        self.tasks.append(task)
    def complete_task(self, id):
        if self.is_index_valid(id):
            self.tasks[id - 1].complete()
            return True
        return False
    def show_tasks(self):
        for id, task in enumerate(self.tasks, 1):
            print(f"{id} | {task.title} | {task.date} | {task.is_done}")
    def delete_task(self, id):
        if self.is_index_valid(id):
            self.tasks.pop(id-1)
            return True
        return False
    def is_index_valid(self, id):
        return 1 <= id <= len(self.tasks)
    def to_dict(self):
        return [{
                "title":task.title,
                "date": task.date.isoformat(),
                "is_done": task.is_done
            } for task in self.tasks]
