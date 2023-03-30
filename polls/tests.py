import datetime
from django.test import TestCase
from django.utils import timezone

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