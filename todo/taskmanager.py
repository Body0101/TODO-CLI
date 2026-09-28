from datetime import datetime
from .task import Task
import json
from .cli_format import formater
from .storage import DATA_DIR, DATA_FILE


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, year, month, day, hour=0, minute=0):  # * main function
        task = Task(
            title=title,
            date=datetime(year, month, day, hour, minute),
        )

        self.tasks.append(task)

    # ^==============================================================

    def complete_task(self, task_id):  # * main function
        task = self.get_task(task_id)
        if task:
            task.complete()
            return True
        return False

    # ^==============================================================

    # * main function

    # ^==============================================================

    def delete_task(self, task_id):  # * main function
        task = self.get_task(task_id)
        if task in self.tasks:
            self.tasks.remove(task)
            return True
        return False

    # ^==============================================================

    def to_dict(self):
        return [
            {
                "title": task.title,
                "date": task.date.isoformat(),
                "is_done": task.is_done,
            }
            for task in self.tasks
        ]

    # ^==============================================================

    def save_tasks(self):
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        with open(DATA_FILE, "w") as file:
            json.dump(self.to_dict(), file, indent=4)

    # ^==============================================================

    def load_tasks(self):
        self.tasks = []
        if not DATA_FILE.exists():
            return
        with open(DATA_FILE, "r") as file:
            lst_dict = json.load(file)
        for task in lst_dict:
            new_task = Task(
                title=task["title"], date=datetime.fromisoformat(task["date"])
            )
            new_task.is_done = task["is_done"]
            self.tasks.append(new_task)

    # ^==============================================================

    def get_task_groups(self):
        overdue = []
        upcoming = []
        completed = []
        for task in self.tasks:
            if task.is_done:
                completed.append(task)
            elif task.date < datetime.now():
                overdue.append(task)
            else:
                upcoming.append(task)
        overdue.sort(key=lambda task: task.date)
        upcoming.sort(key=lambda task: task.date)
        return {"O": overdue, "U": upcoming, "C": completed}

    # ^================================================================

    def get_task(self, task_id):
        if not self.is_valid_task_id(task_id):
            return False
        id = int(task_id[1:])
        return self.get_task_groups()[task_id[0]][id - 1]

    def is_valid_task_id(self, task_id):
        if not task_id:
            return False
        if task_id[0] not in ("C", "O", "U"):
            return False
        try:
            id = int(task_id[1:])
        except ValueError:
            return False
        return 1 <= id <= len(self.get_task_groups()[task_id[0]])
