from django.contrib import admin
from . models import Question, Choice
from .models import Feedback


# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Feedback)