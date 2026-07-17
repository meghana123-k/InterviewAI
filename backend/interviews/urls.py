from django.urls import path
from .views import (
    InterviewCreateView,
    InterviewDetailView,
    CurrentQuestionView,
    InterviewProgressView,
    SubmitAnswerView,
)

urlpatterns = [
    path(
        "configure/",
        InterviewCreateView.as_view(),
    ),
    path(
        "<int:id>/",
        InterviewDetailView.as_view(),
    ),
    path(
        "<int:id>/question/",
        CurrentQuestionView.as_view(),
    ),
    path(
        "question/<int:question_id>/answer/",
        SubmitAnswerView.as_view(),
    ),
    path(
        "<int:interview_id>/progress/",
        InterviewProgressView.as_view(),
        name="interview-progress",
    ),
]
