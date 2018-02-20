from ..models import User
from ..misc.utils import AESCipher


class UserService():

    def __init__(self):
        self.aes = AESCipher()

    def create_user(self, first_name, last_name, email, password):
        """Return user information object or nothing"""
        return

    def login_user(self, email, password):
        """Return user information object or nothing"""
        return

    def logout_user(self, token):
        """Return True if success or False"""
        return False
