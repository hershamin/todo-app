# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cjson as json

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from misc.utils import json_response, bad_request
from misc.decorators import content_type, method


# DB Name
@csrf_exempt
@method('GET')
def dbtype(request):
    # Return database type
    dbPath = settings.DATABASES['default']['NAME']
    dbFile = dbPath.split('/')[-1]
    if 'test' in dbFile:
        return json_response({'name': 'test'})
    else:
        return json_response({'name': 'prod'})


# Sign up
@csrf_exempt
@method('POST')
@content_type('application/json')
def signup(request):
    return bad_request('signup')


# Log in
@csrf_exempt
@method('POST')
@content_type('application/json')
def login(request):
    return bad_request('login')


# Logout
@csrf_exempt
@method('POST')
def logout(request):
    return bad_request('logout')


# Create task
@csrf_exempt
@method('GET')
def get_tasks(request):
    return bad_request('get tasks')


# Delete task
@csrf_exempt
@method('DELETE')
def delete_task(request):
    return bad_request('delete task')
