# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
import django

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from ..misc.utils import AESCipher, get_rand_key


class User(AbstractBaseUser):
    """This class represents the user model"""
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=False, unique=True, db_index=True)
    current_session = models.CharField(max_length=128, blank=True, default='', db_index=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=128)

    created_at = models.DateTimeField(editable=False, default=django.utils.timezone.now)
    updated_at = models.DateTimeField(editable=False, default=django.utils.timezone.now)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return 'Email: {0}, Last Login: {1}'.format(self.email, self.last_login)

    def save(self, *args, **kwargs):
        """On save update timestamps"""
        if not self.user_id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(User, self).save(*args, **kwargs)

    def get_session_key(self):
        """Sets and returns session token"""
        genKey = get_rand_key()
        aes = AESCipher()
        self.current_session = aes.encrypt(genKey)
        self.last_login = timezone.now()
        self.save()
        return genKey

    def clear_session_key(self):
        """Clear session key"""
        self.current_session = ''
        self.save()
