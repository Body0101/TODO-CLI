from datetime import datetime
from .task import Task
import json


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
    def save_tasks(self):
        with open("/run/media/abdelrahman/52C09CE0C09CCB9B/python/todo_project/todo/data.json", "w") as file:
            json.dump(self.to_dict(),file, indent=4)
    def load_tasks(self):
        self.tasks = []
        with open("/run/media/abdelrahman/52C09CE0C09CCB9B/python/todo_project/todo/data.json", "r") as file:
            lst_dict = json.load(file) 
        for task in lst_dict:
            new_task = Task(title=task["title"], date=datetime.fromisoformat(task["date"]))
            new_task.is_done = task["is_done"]
            self.tasks.append(new_task)

