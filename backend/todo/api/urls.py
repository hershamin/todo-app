from django.conf.urls import url
import views as v


def formatUrl(regex='', apiVersion='v1'):
    return r'^api/{}/{}'.format(apiVersion, regex)


urlpatterns = [
    url(formatUrl('db'), v.dbtype),
]
