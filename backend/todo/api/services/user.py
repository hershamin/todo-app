from ..models import User
from ..misc.utils import AESCipher


class UserService():

    def __init__(self):
        self.aes = AESCipher()

    def user_response(self, email, firstName, lastName, session):
        return {
            'email': email,
            'first_name': firstName,
            'last_name': lastName,
            'login_token': session
        }

    def create_user(self, first_name, last_name, email, password):
        """Return user information object or nothing"""
        try:
            user = User(email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            session = user.get_session_key()
            user.save()
        except Exception:
            return
        return self.user_response(email, first_name, last_name, session)

    def login_user(self, email, password):
        """Return user information object or nothing"""
        try:
            user = User.objects.get(email=email)
        except Exception:
            return
        status = user.check_password(password)
        if not status:
            return
        else:
            session = user.get_session_key()
            return self.user_response(email, user.first_name, user.last_name, session)

    def logout_user(self, token):
        """Return True if success or False"""
        try:
            encToken = self.aes.encrypt(token)
            user = User.objects.get(current_session=encToken)
        except Exception:
            return False
        user.clear_session_key()
        return True
