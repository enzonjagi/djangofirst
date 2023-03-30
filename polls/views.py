from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question, Choice

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

    # we could use HttpResponse as show below:
    # return HttpResponse(template.render(context, request))
    # or use render() as a shortcut, as shown below:
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """Dispays a question in detail
    
    Parameters:
        - request
        - question_id: the id of the question
    """

    # There are two options for this
    # the try - except option below
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """
    # or the get_object_or_404() function as implemented below
    question = get_object_or_404(Question, pk=question_id)

    # return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', { 'question': question})

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

    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        # Redisplay the question for voting
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': "Please pick one of the choices",
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return a redirect after posting data to avoid posting it twice
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )

    # return HttpResponse("You're voting on question %s." % question_id)