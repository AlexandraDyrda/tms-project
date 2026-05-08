from enum import Enum
from typing import Dict, List, Any


class TaskStatus(Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'


ALLOWED_TRANSITIONS: Dict[TaskStatus, List[TaskStatus]] = {
    TaskStatus.TODO: [TaskStatus.IN_PROGRESS],
    TaskStatus.IN_PROGRESS: [TaskStatus.DONE],
    TaskStatus.DONE: []
}


class Task:
    def __init__(self, id: Any, title: str, status: TaskStatus) -> None:
        self.id = id
        self.title = title
        self.status = status

    def change_status(self, new_status: TaskStatus) -> None:
        if new_status not in ALLOWED_TRANSITIONS[self.status]:
            raise ValueError(f'Cannot transition from {self.status} to {new_status}')
        self.status = new_status
