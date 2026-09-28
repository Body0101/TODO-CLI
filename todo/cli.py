import argparse
from .taskmanager import TaskManager
import datetime
from .cli_format import formater, task_added, task_completed, task_deleted, task_errors

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
    add_parser = subparsers.add_parser(
        "add", help="Add a new task with a title, date, and optional time."
    )
    add_parser.add_argument("title", help="Task title")

    add_parser.add_argument(
        "--date", required=True, type=valid_date, help="Task date (YYYY-MM-DD)"
    )

    add_parser.add_argument(
        "--time",
        default=datetime.time(0, 0),
        type=valid_time,
        help='Task time "HH:MM AM/PM"',
    )
    # list command
    list_parser = subparsers.add_parser("list", help="Show all tasks")
    # complete command
    complete_parser = subparsers.add_parser("complete", help="Complete a task")
    complete_parser.add_argument(
        "id",
        type=str,
        nargs="+",
        metavar="ID",
        help="Task IDs to complete (e.g. O1 U2 C3)",
    )
    # delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument(
        "id",
        type=str,
        nargs="+",
        metavar="ID",
        help="Task IDs to delete (e.g. O1 U2 C3)",
    )
    args = parser.parse_args()
    if args.command == "add":
        add_command(args)
    #  Here Print >
    elif args.command == "complete":
        complete_command(args)
    elif args.command == "list":
        list_command()
    elif args.command == "delete":
        delete_command(args)


def add_command(args):
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
    task_added()


def complete_command(args):
    manage.load_tasks()
    # Here Print >
    # now I note the wrong indeces
    wrng = []
    for id in args.id:
        if not manage.complete_task(id):
            wrng.append(id)
    manage.save_tasks()
    if wrng:
        task_errors(wrng)
    if len(wrng) < len(args.id):
        task_completed()


def list_command():
    manage.load_tasks()
    groups = manage.get_task_groups()
    formater(groups)


def delete_command(args):
    manage.load_tasks()
    wrng = []
    args.id.sort(key=lambda id: int(id[1:]) if id[1:].isdigit() else 0, reverse=True)
    for id in args.id:
        if not manage.delete_task(id):
            wrng.append(id)
    if wrng:
        task_errors(wrng)
    manage.save_tasks()
    if len(wrng) < len(args.id):
        task_deleted()
