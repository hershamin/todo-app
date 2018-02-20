from ..models import Task
from ..misc.utils import AESCipher


class TaskService():

    def __init__(self):
        self.aes = AESCipher()

    def create_task(self, token, title, description, priority):
        """Return task_id if created or nothing"""
        return

    def complete_task(self, token, task_id):
        """Return True if completed or False"""
        return False

    def delete_task(self, token, task_id):
        """Return True if deleted or False"""
        return False

    def get_tasks(self, token):
        """Return array of tasks"""
        return []

    def set_task_priority(self, token, task_id, priority):
        """Return True if set priority or False"""
        return False
