import argparse
from .taskmanager import TaskManager
import datetime

manage = TaskManager()

def valid_date(value):
    try:
        return datetime.datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError("date must be in YYYY-MM-DD format")


def valid_time(value):
    try:
        return datetime.datetime.strptime(value, "%I:%M %p").time()
    except ValueError:
        raise argparse.ArgumentTypeError("time must be in HH:MM AM/PM format")

def main():
    parser = argparse.ArgumentParser(
        prog="todo",
        description="A simple command-line TODO manager, Designed by Eng-Body",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    # add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")

    add_parser.add_argument(
        "--date", required=True, type=valid_date, help="Task date (YYYY-MM-DD)"
    )

    add_parser.add_argument(
        "--time",
        default=datetime.time(0, 0),
        type=valid_time,
        help="Task time (HH:MM AM/PM)",
    )
    # list command
    list_parser = subparsers.add_parser("list", help="Show all tasks")
    # complete command
    complete_parser = subparsers.add_parser("complete", help="Complete a task")
    complete_parser.add_argument(
        "num",
        type=int,
        help="Add numbers of tasks to complete it",
        nargs="+",
        metavar="number of task",
    )
    # delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument(
            "num",
            type=int,
            help="Add numbers of tasks to delete it",
            nargs="+",
            metavar="number of task",
        )
    args = parser.parse_args()
    if args.command == "add":
        manage.load_tasks()
        manage.add_task(
            title=args.title,
            year=args.date.year,
            month=args.date.month,
            day=args.date.day,
            hour=args.time.hour,
            minute=args.time.minute,
        )
        manage.save_tasks()
    elif args.command == "complete":
        manage.load_tasks()
        for num in args.num:
            if not manage.complete_task(num):
                print(f"{num} is not found")
        manage.save_tasks()
    elif args.command == "list":
        manage.load_tasks()
        manage.show_tasks()
    elif args.command == "delete":
        manage.load_tasks()
        args.num.sort(reverse=True)
        for num in args.num:
            if not manage.delete_task(num):
                print(f"{num} is not found")
        manage.save_tasks()
