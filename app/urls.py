from django.conf.urls import url  # import the url function from the from the django.conf.urls
from . import views  # import the app's views module.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url ( r'^$' , views.home , name='welcome' ) ,
    url ( r'^about/' , views.about , name='about' ) ,
    url( r'^search/' , views.search_results , name='search_results' ) ,
    url( r'^image/(\d+)' , views.single_image , name='filter' ),
    url ( r'^location/(\w+)' , views.location , name='location' ) ,
]
if settings.DEBUG:
    urlpatterns+=static ( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )
