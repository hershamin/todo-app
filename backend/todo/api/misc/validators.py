from jsonschema import validate, ValidationError


def validateJson(object, schema):
    """Returns true or false for valid json schema"""
    try:
        validate(object, schema)
        return True
    except ValidationError as e:
        #print e.message
        return False


# Schemas
signupSchema = {
    'type': 'object',
    'properties': {
        'first_name': {
            'type': 'string'
        },
        'last_name': {
            'type': 'string'
        },
        'email': {
            'type': 'string',
            'format': 'email',
        },
        'password': {
            'type': 'string'
        },
    },
    'required': [
        'first_name',
        'last_name',
        'email',
        'password',
    ]
}

loginSchema = {
    'type': 'object',
    'properties': {
        'email': {
            'type': 'string',
            'format': 'email',
        },
        'password': {
            'type': 'string'
        },
    },
    'required': [
        'email',
        'password',
    ]
}

createTaskSchema = {
    'type': 'object',
    'properties': {
        'title': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
        'priority': {
            'type': 'string',
            'enum': [
                'Low',
                'Medium',
                'High',
            ]
        },
    },
    'required': [
        'title',
        'description',
        'priority',
    ]
}
