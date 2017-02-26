from django.conf.urls import url

from . import views

app_name = 'members'
urlpatterns = [
    url(r'^apply/$', views.new_member_application, name='apply'),
]
