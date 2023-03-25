from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """The index view for the polls app"""
    return HttpResponse("Salaam peeps. Welcome to the Polls index page")
