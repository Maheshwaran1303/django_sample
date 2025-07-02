from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("Hello, world! This is the home page of my Django app.")
    return render(request, 'myapp/home.html', {'title': 'Home Page'})

def about(request):
    # return HttpResponse("This is the about page of my Django app.")
    return render(request, 'myapp/about.html', {'title': 'About Page'})