from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    """
    The index view for the polls app

    Methods:
        - get_queryset(): returns the latest 5 published questions
    """

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions
        """

        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    """Dispays a question in detail
    """

    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    """Dispays a question's results in detail
    """

    model = Question
    template_name = 'polls/results.html'


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