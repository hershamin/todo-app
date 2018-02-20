# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
import django

from django.db import models
from ..misc.choices import TaskPriority, TaskStatus


class Task(models.Model):
    """This class represents the task model"""
    task_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', related_name='users', blank=True,
                             null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, default='Untitled')
    description = models.TextField(default='', blank=True, null=True)

    task_priority = models.CharField(max_length=2, choices=TaskPriority.CHOICES, default=TaskPriority.LOW)
    task_status = models.CharField(max_length=2, choices=TaskStatus.CHOICES, default=TaskStatus.OPEN)
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(editable=False, default=django.utils.timezone.now)
    updated_at = models.DateTimeField(editable=False, default=django.utils.timezone.now)

    def __str__(self):
        return 'Task ID: {0}, title: {1}, user: {2}'.format(self.task_id, self.title, self.user)

    def save(self, *args, **kwargs):
        """Update timestamps on save"""
        if not self.task_id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Task, self).save(*args, **kwargs)
