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
##
