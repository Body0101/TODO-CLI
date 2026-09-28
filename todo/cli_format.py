# take maange >> self.tasks
# ! Don't forget cli.py about list (show_tasks)
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

# Improved: mapping each group key to (label, color) used for the centered rule title
SECTION_STYLE = {
    "O": ("⚠ OVERDUE TASKS", "red"),
    "U": ("🕒 UPCOMING TASKS", "yellow"),
    "C": ("✅ COMPLETED TASKS", "green"),
}


def _build_section_table(tasks, prefix, row_style=None):
    # Improved: each section is now its own small table (with its own header)
    table = Table(
        box=box.SIMPLE_HEAVY, show_header=True, header_style="bold", expand=False
    )
    table.add_column("ID", justify="center", style="bold")
    table.add_column("Task", min_width=20)
    table.add_column("Due Date", justify="center")
    for num, task in enumerate(tasks, 1):
        table.add_row(
            f"{prefix}{num}",
            task.title,
            task.date.strftime("%d %b %Y %I:%M %p"),
            style=row_style,
        )
    return table


def formater(groups):
    if not any(groups.values()):
        console.print("[dim]No tasks found.[/dim]")
        return

    # Improved: order + per-section row style (dim for overdue, none for upcoming, dim strike for completed)
    order = [
        ("O", "dim"),
        ("U", None),
        ("C", "dim strike"),
    ]

    for key, row_style in order:
        if not groups[key]:
            continue
        label, color = SECTION_STYLE[key]
        # Improved: console.rule prints the label centered on its own full-width line
        console.rule(f"[bold {color}]{label}[/bold {color}]", style=color)
        table = _build_section_table(groups[key], key, row_style=row_style)
        console.print(table)


def task_added():
    console.print("[green]Added[/green]")


def task_completed():
    console.print("[green]Completed[/green]")


def task_deleted():
    console.print("[green]Deleted[/green]")

def task_errors(wrng):
    console.print(f"[red]{', '.join(wrng)} not found[/red]")
