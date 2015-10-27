from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signal/(?P<signal>[a-zA-Z0-9])$', views.signal, name='signal'),
    url(r'^reset$', views.reset, name='reset'),
]

