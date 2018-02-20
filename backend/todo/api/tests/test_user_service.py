from django.test import TestCase
from ..models import User
from ..services import UserService


class UserServiceTestCase(TestCase):

    def setUp(self):
        self.existingUser = User(email='info@example.com', first_name='first', last_name='last')
        self.existingUser.set_password('password')
        self.existingUser.save()
        self.userService = UserService()

    def test_create_user(self):
        signupInfo = self.userService.create_user('first', 'last', 'info@info.com', 'password')
        user = User.objects.get(email='info@info.com')
        self.assertEqual(user.email, 'info@info.com')
        self.assertEqual(signupInfo.get('first_name'), 'first')
        self.assertEqual(signupInfo.get('last_name'), 'last')
        self.assertEqual(signupInfo.get('email'), user.email)
        self.assertTrue(len(signupInfo.get('login_token')) > 0)

    def test_create_user_existing(self):
        signupInfo = self.userService.create_user('first', 'last', self.existingUser.email, 'password')
        self.assertEqual(signupInfo, None)

    def test_login_user(self):
        loginInfo = self.userService.login_user(self.existingUser.email, 'password')
        self.assertEqual(loginInfo.get('first_name'), self.existingUser.first_name)
        self.assertEqual(loginInfo.get('last_name'), self.existingUser.last_name)
        self.assertEqual(loginInfo.get('email'), self.existingUser.email)
        self.assertTrue(len(loginInfo.get('login_token')) > 0)

    def test_login_user_false_information(self):
        loginInfo = self.userService.login_user('info@example', 'pass')
        self.assertEqual(loginInfo, None)

    def test_logout_user(self):
        loginInfo = self.userService.login_user(self.existingUser.email, 'password')
        status = self.userService.logout_user(loginInfo.get('login_token'))
        self.assertTrue(status)

    def test_logout_user_false_information(self):
        loginInfo = self.userService.login_user(self.existingUser.email, 'password')
        status = self.userService.logout_user('fake token')
        self.assertFalse(status)
