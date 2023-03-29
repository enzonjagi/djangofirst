from django.db import models

# Create your models here.
"""We'll be defining models in this file.

The Models are represented by the classes below.
"""


class Question(models.Model):
    """A question: represents qustions in the poll app
    
    Attributes:
        - question_text: the question itself
        - pub_date: the publishing date for the question
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    """A choice: represents the options for user to answer questions

    Attributes:
        - question: refers to the question that was asked(a foreign key)
        - choice_text: the text for each individual choice given for the question
        - votes: the number of votes allocated to the above choice
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)