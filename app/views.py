from django.shortcuts import render
from django.http import HttpResponse , Http404  # import the HttpResponse class from the django.http module.
from .models import Image , Category , Location
import datetime as dt
from peewee import DoesNotExist


# Create your view functios  here.
def home(request):
    # return render ( request , 'welcome.html')
    # gallery=Image.get_all()
    images=Image.objects.filter( ).order_by( 'location' )
    # images=Image.objects.all()
    loct=Location.objects.all( )

    categories=Category.objects.all( )

    date=dt.date.today
    return render( request , 'welcome.html' ,
                   {"date": date , "images": images,"loct":loct,"categories":categories} )


def about(request):
    return render( request , 'about.html' )


def single_image(request , category):
    category=Image.objects.get( category=category )
    return render( request , 'filter.html' , {'image': category} )


def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term=request.GET.get( "category" )
        searched_category=Image.search_by_category( search_term )
        message=f"{search_term}"

        return render( request , 'search.html' , {"message": message , "category": searched_category} )

    else:
        message="You haven't searched for any term"
        return render( request , 'search.html' , {"message": message} )


def location(request , location_id):
    load =Location.objects.get(name=location_id)
    location=Image.objects.filter(location=load.id)
    lock=Location.objects.all()
    loct=Location.objects.all( )
    return render( request , 'location.html' ,
                   {"location": location , "lock": lock,"loct":loct} )


def category(request , category):
    images=Image.filter_by_category( category )
    category=Category.objects.get( pk=category )
    categories=Category.objects.all( )
    loct=Location.objects.all( )

    return render( request , 'location.html' ,
                   {"images": images , "categories": categories , "category": category,"loct":loct} )
