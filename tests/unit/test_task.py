import pytest
from src.models.task import Task, TaskStatus
from src.validators.task_validator import TaskValidator
from src.services.task_service import TaskService

# 1. Тестуємо модель задачі (task.py)
def test_task_creation():
    task = Task(id=1, title="Test", status=TaskStatus.TODO)
    assert task.status == TaskStatus.TODO

def test_change_status_valid():
    task = Task(id=1, title="Test", status=TaskStatus.TODO)
    task.change_status(TaskStatus.IN_PROGRESS)
    assert task.status == TaskStatus.IN_PROGRESS

def test_change_status_invalid():
    task = Task(id=1, title="Test", status=TaskStatus.TODO)
    with pytest.raises(ValueError):
        task.change_status(TaskStatus.DONE) # З TODO не можна відразу в DONE

# 2. Тестуємо валідатор (task_validator.py)
def test_task_validator():
    validator = TaskValidator()
    assert validator.is_title_valid("") == False
    assert validator.is_title_valid("   ") == False
    assert validator.is_title_valid("Good Title") == True

# 3. Тестуємо сервіс (task_service.py)
def test_task_service():
    service = TaskService()
    assert service is not None