from django.contrib import admin

from .models import (
    Interview,
    InterviewAnswer,
    InterviewQuestion,
    QuestionBank,
)

admin.site.register(Interview)
admin.site.register(InterviewQuestion)
admin.site.register(QuestionBank)
admin.site.register(InterviewAnswer)
