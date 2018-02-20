from ..models import Task, User
from ..misc.utils import AESCipher
from ..misc.choices import to_internal, to_external, TaskStatus, TaskPriority


class TaskService():

    def __init__(self):
        self.aes = AESCipher()

    def create_task(self, token, title, description, priority):
        """Return task_id if created or nothing"""
        try:
            encToken = self.aes.encrypt(token)
            user = User.objects.get(current_session=encToken)
        except Exception:
            return
        task = Task(title=title, description=description, user=user,
                    task_priority=to_internal(TaskPriority, priority))
        task.save()
        return task.task_id

    def complete_task(self, token, task_id):
        """Return True if completed or False"""
        try:
            encToken = self.aes.encrypt(token)
            user = User.objects.get(current_session=encToken)
            task = Task.objects.get(task_id=task_id, user=user)
        except Exception:
            return False
        task.task_status = TaskStatus.DONE
        task.save()
        return True

    def delete_task(self, token, task_id):
        """Return True if deleted or False"""
        try:
            encToken = self.aes.encrypt(token)
            user = User.objects.get(current_session=encToken)
            task = Task.objects.get(task_id=task_id, user=user)
        except Exception:
            return False
        task.delete()
        return True

    def set_task_priority(self, token, task_id, priority):
        """Return True if set priority or False"""
        try:
            encToken = self.aes.encrypt(token)
            user = User.objects.get(current_session=encToken)
            task = Task.objects.get(task_id=task_id, user=user)
        except Exception:
            return False
        task.task_priority = to_internal(TaskPriority, priority)
        task.save()
        return True

    def get_tasks(self, token):
        """Return array of tasks"""
        try:
            encToken = self.aes.encrypt(token)
            user = User.objects.get(current_session=encToken)
        except Exception:
            return []
        tasks = Task.objects.filter(user=user).order_by('-created_at')
        resp = []
        for task in tasks:
            temp = {
                'title': task.title,
                'description': task.description,
                'priority': to_external(TaskPriority, task.task_priority),
                'status': to_external(TaskStatus, task.task_status),
                'id': task.task_id
            }
            resp.append(temp)
        return resp
