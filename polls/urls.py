from django.urls import path

from . import views

# define the app name for namespacing reasons
app_name = 'polls'

# here's where the url patterns for the views will be created 
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]