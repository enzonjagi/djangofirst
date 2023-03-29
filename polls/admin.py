from django.contrib import admin
from .models import Question

"""
    Makes the poll app modifiable in the admin site
"""

# Register your models here.
admin.site.register(Question)
