from django.test import TestCase
from ..services import TaskService, UserService


class TaskServiceTestCase(TestCase):

    def setUp(self):
        self.taskService = TaskService()
        self.userService = UserService()
        self.user = self.userService.create_user('first', 'last', 'info@email.com', 'password')
        self.token = self.userService.login_user(self.user.get('email'), 'password').get('login_token')

    def test_create_task(self):
        taskId = self.taskService.create_task(self.token, 'title', 'desc', 'Low')
        self.assertIsNotNone(taskId)
        tasks = self.taskService.get_tasks(self.token)
        self.assertEqual(len(tasks), 1)
        task = tasks.__getitem__(0)
        self.assertEqual(task.get('title'), 'title')
        self.assertEqual(task.get('description'), 'desc')
        self.assertEqual(task.get('priority'), 'Low')
        self.assertEqual(task.get('status'), 'Open')
        self.assertIsNotNone(task.get('id'))

    def test_create_task_unknown_user(self):
        taskId = self.taskService.create_task('fake token', 'title', 'desc', 'Low')
        self.assertIsNone(taskId)
        tasks = self.taskService.get_tasks(self.token)
        self.assertEqual(len(tasks), 0)

    def test_complete_task(self):
        taskId = self.taskService.create_task(self.token, 'title', 'desc', 'Low')
        status = self.taskService.complete_task(self.token, taskId)
        self.assertTrue(status)
        tasks = self.taskService.get_tasks(self.token)
        self.assertEqual(len(tasks), 1)
        task = tasks.__getitem__(0)
        self.assertEqual(task.get('id'), taskId)
        self.assertEqual(task.get('status'), 'Done')

    def test_complete_task_unknown_user(self):
        taskId = self.taskService.create_task(self.token, 'title', 'desc', 'Medium')
        status = self.taskService.complete_task('fake token', taskId)
        self.assertFalse(status)
        tasks = self.taskService.get_tasks(self.token)
        self.assertEqual(len(tasks), 1)
        task = tasks.__getitem__(0)
        self.assertEqual(task.get('id'), taskId)
        self.assertEqual(task.get('status'), 'Open')

    def test_complete_task_wrong_id(self):
        taskId = self.taskService.create_task(self.token, 'title', 'desc', 'High')
        status = self.taskService.complete_task(self.token, taskId + 2)
        self.assertFalse(status)
        tasks = self.taskService.get_tasks(self.token)
        self.assertEqual(len(tasks), 1)
        task = tasks.__getitem__(0)
        self.assertEqual(task.get('id'), taskId)
        self.assertEqual(task.get('status'), 'Open')

    def test_delete_task(self):
        taskId = self.taskService.create_task(self.token, 'title', 'desc', 'High')
        status = self.taskService.delete_task(self.token, taskId)
        self.assertTrue(status)
        tasks = self.taskService.get_tasks(self.token)
        self.assertEqual(len(tasks), 0)

    def test_delete_task_unknown_user(self):
        taskId = self.taskService.create_task(self.token, 'title', 'desc', 'High')
        status = self.taskService.delete_task('fake token', taskId)
        self.assertFalse(status)
        tasks = self.taskService.get_tasks(self.token)
        self.assertEqual(len(tasks), 1)
        task = tasks.__getitem__(0)
        self.assertEqual(task.get('id'), taskId)

    def test_delete_task_wrong_id(self):
        taskId = self.taskService.create_task(self.token, 'title', 'desc', 'High')
        status = self.taskService.delete_task(self.token, taskId + 2)
        self.assertFalse(status)
        tasks = self.taskService.get_tasks(self.token)
        self.assertEqual(len(tasks), 1)
        task = tasks.__getitem__(0)
        self.assertEqual(task.get('id'), taskId)

    def test_set_priority(self):
        taskId = self.taskService.create_task(self.token, 'title', 'desc', 'High')
        status = self.taskService.set_task_priority(self.token, taskId, 'Medium')
        self.assertTrue(status)
        tasks = self.taskService.get_tasks(self.token)
        self.assertEqual(len(tasks), 1)
        task = tasks.__getitem__(0)
        self.assertEqual(task.get('id'), taskId)
        self.assertEqual(task.get('priority'), 'Medium')

    def test_set_priority_unknown_user(self):
        taskId = self.taskService.create_task(self.token, 'title', 'desc', 'High')
        status = self.taskService.set_task_priority('fake token', taskId, 'Medium')
        self.assertFalse(status)
        tasks = self.taskService.get_tasks(self.token)
        self.assertEqual(len(tasks), 1)
        task = tasks.__getitem__(0)
        self.assertEqual(task.get('id'), taskId)
        self.assertEqual(task.get('priority'), 'High')

    def test_set_priority_wrong_id(self):
        taskId = self.taskService.create_task(self.token, 'title', 'desc', 'High')
        status = self.taskService.set_task_priority(self.token, taskId + 2, 'Medium')
        self.assertFalse(status)
        tasks = self.taskService.get_tasks(self.token)
        self.assertEqual(len(tasks), 1)
        task = tasks.__getitem__(0)
        self.assertEqual(task.get('id'), taskId)
        self.assertEqual(task.get('priority'), 'High')
