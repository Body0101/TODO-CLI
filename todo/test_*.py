import pytest
from .taskmanager import TaskManager
from datetime import datetime


@pytest.fixture
def manage():
    return TaskManager()


@pytest.mark.parametrize("title, year, month, day", [("Klam in hob", 2007, 12, 6)])
def test_add_task(title, year, month, day, manage):
    manage.add_task(title, year, month, day)
    y = len(manage.tasks)
    assert y == 1


@pytest.mark.parametrize("title, year, month, day", [("Klam in hob", 2007, 12, 6)])
def test_add_task_title(title, year, month, day, manage):
    manage.add_task(title, year, month, day)

    assert manage.tasks[0].title == "Klam In Hob"


# Test and simulate input date as the same stored result
@pytest.mark.parametrize("title, year, month, day", [("Klam in hob", 2007, 12, 6)])
def test_add_task_date(title, year, month, day, manage):
    manage.add_task(title, year, month, day)
    y = manage.tasks
    assert y[0].date == datetime(
        2007,
        12,
        6,
    )

# Test status task
@pytest.mark.parametrize("title, year, month, day", [("Klam in hob", 2007, 12, 6)])
def test_add_task_done1(title, year, month, day, manage):
    manage.add_task(title, year, month, day)
    assert not manage.tasks[0].is_done

# Test indexing as inputs
@pytest.mark.parametrize(
    "id, expected",
    [
        (-1, False),
        (0, False),
        (1, True),
        (2, False),
        (3, False),
    ],
)
def test_add_task_complete(id, expected, manage):
    manage.add_task("Klam in hob", 2007, 12, 6)
    assert manage.complete_task(id) == expected


@pytest.mark.parametrize("title, year, month, day", [("Klam in hob", 2007, 12, 6)])
def test_add_task_done2(title, year, month, day, manage):
    manage.add_task(title, year, month, day)
    manage.complete_task(1)
    assert manage.tasks[0].is_done


@pytest.mark.parametrize(
    "id, expected",
    [
        (-1, False),
        (0, False),
        (1, True),
        (2, False),
        (100, False),
    ],
)
def test_delete_task_return(id, expected, manage):
    manage.add_task("Task", 2026, 9, 24)

    assert manage.delete_task(id) == expected

# ======================= Delete testing ========================

def test_delete_task_removes_task(manage):
    manage.add_task("Task", 2026, 9, 24)

    assert len(manage.tasks) == 1

    manage.delete_task(1)

    assert len(manage.tasks) == 0


def test_delete_specific_task(manage):
    manage.add_task("Task One", 2026, 9, 24)
    manage.add_task("Task Two", 2026, 9, 25)
    manage.add_task("Task Three", 2026, 9, 26)

    manage.delete_task(2)

    assert len(manage.tasks) == 2
    assert manage.tasks[0].title == "Task One"
    assert manage.tasks[1].title == "Task Three"

# ==================== to_dict testing ====================

def test_to_dict(manage):
    manage.add_task("Klam in hob", 2026, 9, 24)

    result = manage.to_dict()

    assert result == [
        {
            "title": "Klam In Hob",
            "date": datetime(2026, 9, 24).isoformat(),
            "is_done": False,
        }
    ]


def test_to_dict_after_complete(manage):
    manage.add_task("Task", 2026, 9, 24)

    manage.complete_task(1)

    result = manage.to_dict()

    assert result[0]["is_done"] is True
