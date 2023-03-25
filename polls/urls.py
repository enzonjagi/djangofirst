from django.urls import path

from . import views

# here's where the url patterns for the views will be created 
urlpatterns = [
    path('', views.index, name='index')
]