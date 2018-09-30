from django.shortcuts import render
from django.http import HttpResponse , Http404  # import the HttpResponse class from the django.http module.
from .models import Image , Category , Location
import datetime as dt
from peewee import DoesNotExist


# Create your view functios  here.
def home(request):
    # return render ( request , 'welcome.html')
    # gallery=Image.get_all( )
    images=Image.objects.filter( ).order_by( 'location' )
    date=dt.date.today
    return render( request , 'welcome.html' ,
                   {"date": date , "images": images} )


def about(request):
    return render( request , 'about.html' )


def single_image(request , image_id):
    image=Image.objects.get( id=image_id )
    return render( request , 'filter.html' , {'image': image} )


def search_results(request):
    if 'location' in request.GET and request.GET["location"]:
        search_term=request.GET.get( "location" )
        searched_location=Image.search_by_location( search_term )
        message=f"{search_term}"

        return render( request , 'search.html' , {"message": message , "location": searched_location} )

    else:
        message="You haven't searched for any term"
        return render( request , 'search.html' , {"message": message} )
