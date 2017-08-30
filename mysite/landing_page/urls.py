from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'send_information$', views.send_information, name='send_information'),
    ]

