# TODO-CLI

A simple and lightweight command-line TODO manager built with Python.

TODO-CLI lets you manage your tasks directly from the terminal with a clean and readable interface.

## Features

* Add tasks with a due date and optional time.
* List tasks grouped by status.
* Automatically organize tasks into:

  * Overdue tasks
  * Upcoming tasks
  * Completed tasks
* Complete multiple tasks at once.
* Delete multiple tasks at once.
* Persistent task storage using JSON.
* Cross-platform data storage.
* Clean terminal output using Rich.
* Helpful command-line errors using argparse.

## Requirements

* Python 3.10 or newer

## Installation

### From GitHub

Clone the repository:

```bash
git clone [https://github.com/YOUR_USERNAME/todo-cli.git](https://github.com/Body0101/TODO-CLI)
cd todo-cli
```

Install the project:

```bash
pip install .
```

After installation, the `todo` command will be available:

```bash
todo --help
```

### Install directly from GitHub

You can also install TODO-CLI directly without cloning the repository:

```bash
pip install git+[https://github.com/YOUR_USERNAME/todo-cli.git](https://github.com/Body0101/TODO-CLI)
```

Then:

```bash
todo --help
```

## Usage

### Show help

```bash
todo --help
```

### Add a task

```bash
todo add "Study Python" --date 2026-10-01
```

You can specify a time:

```bash
todo add "Study Python" --date 2026-10-01 --time "08:30 PM"
```

### List tasks

```bash
todo list
```

Tasks are divided into three groups:

| Prefix | Meaning   |
| ------ | --------- |
| `O`    | Overdue   |
| `U`    | Upcoming  |
| `C`    | Completed |

Example task IDs:

```text
O1
U1
U2
C1
```

### Complete tasks

Complete one task:

```bash
todo complete U1
```

Complete multiple tasks:

```bash
todo complete U1 U2 O1
```

### Delete tasks

Delete one task:

```bash
todo delete U1
```

Delete multiple tasks:

```bash
todo delete U1 U2 C1
```

## Task Display

Tasks are displayed according to their status:

```text
Overdue
   ↓
Upcoming
   ↓
Completed
```

Overdue and completed tasks are visually dimmed, while completed tasks are also shown with a strike-through style.

Tasks within the overdue and upcoming sections are sorted by their due date.

## Data Storage

TODO-CLI stores tasks as JSON.

The data file is stored in the operating system's appropriate application-data directory rather than inside the project or Python package.

This allows TODO-CLI to work across different operating systems without relying on machine-specific paths.

The application uses `platformdirs` to determine the appropriate location automatically.

## Tech Stack

* **Python** — Main programming language
* **argparse** — Command-line interface
* **datetime** — Date and time handling
* **json** — Task persistence
* **Rich** — Terminal formatting and tables
* **platformdirs** — Cross-platform application data directories
* **pytest** — Testing

## Project Structure

```text
todo-cli/
├── todo/
│   ├── __init__.py
│   ├── cli.py
│   ├── cli_format.py
│   ├── storage.py
│   ├── task.py
│   └── taskmanager.py
├── tests/
├── pyproject.toml
├── README.md
└── .gitignore
```

## Development

Clone the repository:

```bash
git clone https://github.com/Body0101/TODO-CLI.git
cd todo-cli
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install the project in editable mode:

```bash
pip install -e .
```

Run the CLI:

```bash
todo --help
```

Run the tests:

```bash
pytest
```

## License

This project is open source. See the `LICENSE` file for details.
