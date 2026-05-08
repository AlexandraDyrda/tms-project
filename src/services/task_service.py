class TaskService:
    def __init__(self, task_repo, notifier):
        self.task_repo = task_repo
        self.notifier = notifier

    def assign_task(self, task_id, assignee_id):
        self.notifier.send(recipient_id=assignee_id, message="assigned")

    def get_task(self, task_id):
        return self.task_repo.find_by_id(task_id)

    def create_task(self, title, priority):
        self.task_repo.save()