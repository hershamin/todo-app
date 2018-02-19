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
