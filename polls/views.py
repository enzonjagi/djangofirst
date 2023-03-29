from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """The index view for the polls app
    
    Attributes:
        - request: not used yet
    """
    return HttpResponse("Salaam peeps. Welcome to the Polls index page")

def detail(request, question_id):
    """Dispays a question in detail
    
    Parameters:
        - request
        - question_id: the id of the question
    """

    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    """Displays the results of a question in detail
    
    Parameters:
        - request
        - question_id: the id of the question
    """

    response = "You're looking at the results of question %s."
    
    return HttpResponse(response % question_id)


def vote(request, question_id):
    """Allows you to vote for a question
    
    Parameters:
        - request
        - question_id: the id of the question
    """

    return HttpResponse("You're voting on question %s." % question_id)