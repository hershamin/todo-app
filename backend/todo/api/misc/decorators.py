import cjson as json
from django.http import HttpResponse


# Allowed Http Methods
def method(methodInput):
    def decorator(func):
        def func_wrapper(request, **kwargs):
            if request.method != methodInput:
                error = json.encode({
                    'error' : 'Wrong Method'
                })
                return HttpResponse(error, status=404, content_type='application/json')
            return func(request, **kwargs)
        return func_wrapper
    return decorator


# Allowed content type
def content_type(contentType):
    def decorator(func):
        def func_wrapper(request, **kwargs):
            if request.content_type != contentType:
                error = json.encode({
                    'error' : 'Wrong Content Type'
                })
                return HttpResponse(error, status=404, content_type='application/json')
            return func(request, **kwargs)
        return func_wrapper
    return decorator