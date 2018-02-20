# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import cjson as json

from django.views.decorators.csrf import csrf_exempt
from ..misc.utils import json_response, bad_request, get_headers_token
from ..misc.decorators import content_type, method
from ..misc.validators import validateJson, loginSchema, signupSchema
from ..services import UserService


# Sign up
@csrf_exempt
@method('POST')
@content_type('application/json')
def signup(request):
    # Validate
    reqBody = json.decode(request.body)
    valid = validateJson(reqBody, signupSchema)
    if not valid:
        return bad_request('Missing information')
    # Action
    userService = UserService()
    resp = userService.create_user(reqBody.get('first_name'),
                                   reqBody.get('last_name'),
                                   reqBody.get('email'),
                                   reqBody.get('password'))
    # Response
    if not resp:
        return bad_request('Unable to comply')
    else:
        return json_response(resp)


# Log in
@csrf_exempt
@method('POST')
@content_type('application/json')
def login(request):
    # Validate
    reqBody = json.decode(request.body)
    valid = validateJson(reqBody, loginSchema)
    if not valid:
        return bad_request('Missing information')
    # Action
    userService = UserService()
    resp = userService.login_user(reqBody.get('email'),
                                  reqBody.get('password'))
    # Response
    if not resp:
        return bad_request('Unable to comply')
    else:
        return json_response(resp)


# Logout
@csrf_exempt
@method('POST')
def logout(request):
    # Validate
    token = get_headers_token(request)
    if not token:
        return bad_request('Missing information')
    # Action
    userService = UserService()
    status = userService.logout_user(token)
    # Response
    if not status:
        return bad_request('Unable to comply')
    else:
        return json_response({})
