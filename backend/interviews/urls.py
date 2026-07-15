from django.urls import path

from .views import InterviewCreateView

urlpatterns = [
    path(
        "configure/",
        InterviewCreateView.as_view(),
        name="configure-interview",
    ),
]
