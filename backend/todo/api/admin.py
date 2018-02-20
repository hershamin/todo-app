# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User, Task
from django.contrib import admin
from misc.utils import ReadonlyTabularInline


# Custom models
class TaskInline(ReadonlyTabularInline):
    model = Task
class UserAdmin(admin.ModelAdmin):
    inlines = (TaskInline,)


# Register your models here
admin.site.register(User, UserAdmin)
admin.site.register(Task)
