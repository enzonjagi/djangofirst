from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    """The index view for the polls app
    
    Attributes:
        - request: not used yet
    """

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    #we could do this
    # return HttpResponse(template.render(context, request))
    # or use render() as a shortcut
    return render(request, 'polls/index.html', context)

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