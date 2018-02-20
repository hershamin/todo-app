from django.conf.urls import url

import views.misc as m
import views.user as u
import views.task as t


def formatUrl(regex='', apiVersion='v1'):
    return r'^api/{}/{}'.format(apiVersion, regex)


urlpatterns = [
    # Misc
    url(formatUrl('db$'), m.dbtype),

    # User
    url(formatUrl('user/signup$'), u.signup),
    url(formatUrl('user/login$'), u.login),
    url(formatUrl('user/logout$'), u.logout),

    # Task
    url(formatUrl('task$'), t.get_tasks),
    url(formatUrl('task/create$'), t.create_task),
    url(formatUrl('task/delete/(?P<task_id>.+)$'), t.delete_task),
    url(formatUrl('task/complete/(?P<task_id>.+)$'), t.complete_task),
    url(formatUrl('task/priority/(?P<task_id>.+)/(?P<priority>.+)$'), t.set_task_priority),
]
