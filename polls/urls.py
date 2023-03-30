from django.urls import path

from . import views

# define the app name for namespacing reasons
app_name = 'polls'

# here's where the url patterns for the views will be created 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]