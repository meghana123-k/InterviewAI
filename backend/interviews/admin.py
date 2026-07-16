from django.contrib import admin

from .models import (
    Interview,
    InterviewQuestion,
    QuestionBank,
)

admin.site.register(Interview)
admin.site.register(InterviewQuestion)
admin.site.register(QuestionBank)
