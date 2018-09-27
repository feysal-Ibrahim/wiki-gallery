from django.conf.urls import url  # import the url function from the from the django.conf.urls
from . import views #import the app's views module.

urlpatterns=[
    url ( r'^$', views.welcome , name='welcome' ),
    url(r'^about/', views.about , name='about'),
]