# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cjson as json

from django.views.decorators.csrf import csrf_exempt
from ..misc.utils import json_response, bad_request, get_headers_token
from ..misc.decorators import content_type, method
from ..misc.validators import validateJson, createTaskSchema
from ..services import TaskService


# Get tasks
@csrf_exempt
@method('GET')
def get_tasks(request):
    # Validate
    token = get_headers_token(request)
    if not token:
        return bad_request('Missing information')
    # Action
    taskService = TaskService()
    tasks = taskService.get_tasks(token)
    # Response
    return json_response(tasks)


# Create task
@csrf_exempt
@method('POST')
@content_type('application/json')
def create_task(request):
    # Validate
    reqBody = json.decode(request.body)
    valid = validateJson(reqBody, createTaskSchema)
    token = get_headers_token(request)
    if not valid or not token:
        return bad_request('Missing information')
    # Action
    taskService = TaskService()
    taskId = taskService.create_task(token, reqBody.get('title'),
                                     reqBody.get('description'),
                                     reqBody.get('priority'))
    # Response
    if not taskId:
        return bad_request('Unable to comply')
    else:
        return json_response({})


# Delete task
@csrf_exempt
@method('DELETE')
def delete_task(request, task_id):
    # Validate
    token = get_headers_token(request)
    if not token:
        return bad_request('Missing information')
    # Action
    taskService = TaskService()
    status = taskService.delete_task(token, task_id)
    # Response
    if not status:
        return bad_request('Unable to comply')
    else:
        return json_response({})


# Complete task
@csrf_exempt
@method('PUT')
def complete_task(request, task_id):
    # Validate
    token = get_headers_token(request)
    if not token:
        return bad_request('Missing information')
    # Action
    taskService = TaskService()
    status = taskService.complete_task(token, task_id)
    # Response
    if not status:
        return bad_request('Unable to comply')
    else:
        return json_response({})


# Set task priority
@csrf_exempt
@method('PUT')
def set_task_priority(request, task_id, priority):
    # Validate
    token = get_headers_token(request)
    priorityValues = ['Low', 'Medium', 'High']
    if not token or priority not in priorityValues:
        return bad_request('Missing information')
    # Action
    taskService = TaskService()
    status = taskService.set_task_priority(token, task_id, priority)
    # Response
    if not status:
        return bad_request('Unable to comply')
    else:
        return json_response({})
