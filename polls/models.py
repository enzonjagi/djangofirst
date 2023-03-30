import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
"""We'll be defining models in this file.

The Models are represented by the classes below.
"""


class Question(models.Model):
    """A question: represents qustions in the poll app
    
    Attributes:
        - question_text: the question itself
        - pub_date: the publishing date for the question
    Methods:
        - __str__ : adding a clean representation of the class
        - was_published_recently: Should check and show if the
                                    question was published recently
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """Should return the question_text when called."""

        return self.question_text
    
    def was_published_recently(self):
        """Should check and show if the question was published recently."""

        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """A choice: represents the options for user to answer questions

    Attributes:
        - question: refers to the question that was asked(a foreign key)
        - choice_text: the text for each individual choice given for the question
        - votes: the number of votes allocated to the above choice
    Methods:
        - __str__ : adding a clean representation of the class
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Should return the choice_text when called."""
        
        return self.choice_text