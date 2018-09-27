from django.shortcuts import render
from django.http import HttpResponse  # import the HttpResponse class from the django.http module.


# Create your view functios  here.
def welcome(request):
    return render ( request , 'welcome.html')
def about(request):
    return render(request, 'about.html')
