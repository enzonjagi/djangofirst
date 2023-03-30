import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question, Choice

# Create your tests here.
class QuestionModelTests(TestCase):
    """Test cases for the Question model
    """

    def test_was_published_recently_with_future_question(self):
        """
        Tests that was_published_recently() returns false for questions
        whose pub_date is in the future
        """

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        #the test
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        Tests that was_published_recently() returns False for questions
        whose pub_date is older than 1 day
        """

        time = timezone.now() - datetime.timedelta(
            days=1,
            seconds=1
        )
        old_question = Question(pub_date=time)

        # run the test
        self.assertIs(
            old_question.was_published_recently(),
            False
        )

    def test_was_published_recently_with_recent_question(self):
        """
        Tests that was_published_recently() returns True for questions
        whose pub_date is within the last day
        """

        time = timezone.now() - datetime.timedelta(
            hours=23,
            minutes=59,
            seconds=59
        )
        recent_question = Question(pub_date=time)

        # run the test
        self.assertIs(
            recent_question.was_published_recently(),
            True
        )

def create_question(question_text, days):
    """A function to create a question

    Description:
        - create a question with 'question_text' and days since 
        publishing(-ve for past, +ve for future published questions)

    Returns:
        - A created question with the parameters as the required info
    """

    time = timezone.now() + datetime.timedelta(days=days)

    return Question.objects.create(
        question_text=question_text,
        pub_date=time
    )

class QuestionIndexViewTests(TestCase):
    """Test cases for the IndexView
    """

    def test_no_questions(self):
        """Checks if an appropiate message appears where not questions
        were created
        """

        response = self.client.get(
            reverse('polls:index')
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            []
        )

    def test_past_question(self):
        """
            Checks if a question published in the past(pub_date),
            is displayed on the index page
        """

        question = create_question(
            question_text="Past Question",
            days=-30
        )
        response = self.client.get(
            reverse('polls:index')
        )

        self.assertQuerysetEqual(
            response.context['latest_query_list'],
            [question],
        )
    
    def test_future_question(self):
        """
            Checks if a question published in the future(pub_date),
            is displayed on the index page
        """

        create_question(
            question_text="Past Question",
            days=30
        )
        response = self.client.get(
            reverse('polls:index')
        )

        self.assertContains(
            response,
            'No polls are available'
        )
        self.assertQuerysetEqual(
            response.context['latest_query_list'],
            [],
        )
    
    def test_future_question_past_question(self):
        """
            Checks if a question published in the past & future
            (pub_date), are displayed on the index page
        """

        question = create_question(
            question_text="Past Question",
            days=-30
        )
        create_question(
            question_text="Past Question",
            days=30
        )
        response = self.client.get(
            reverse('polls:index')
        )

        self.assertQuerysetEqual(
            response.context['latest_query_list'],
            [question],
        )


    def test_two_past_questions(self):
        """
            Checks if two questions published in the past(pub_date),
            is displayed on the index page
        """

        question1 = create_question(
            question_text="Past Question",
            days=-30
        )
        question2 = create_question(
            question_text="Past Question",
            days=-5
        )
        response = self.client.get(
            reverse('polls:index')
        )

        self.assertQuerysetEqual(
            response.context['latest_query_list'],
            [question2, question1],
        )

class QuestionDetailViewTests(TestCase):
    """Test cases for the DetailView
    """


    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(
            question_text='Future question.', 
            days=5
        )
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)