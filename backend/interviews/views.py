from django.db import transaction

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from interviews.services.progress_service import ProgressService

from .models import Interview, InterviewQuestion, InterviewAnswer
from .serializers import (
    InterviewSerializer,
    InterviewQuestionSerializer,
    InterviewAnswerSerializer,
)
from .services.interview_service import InterviewService


class InterviewCreateView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = InterviewSerializer

    def create(self, request, *args, **kwargs):

        try:
            interview = InterviewService.create_interview(
                request.user,
                request.data,
            )

        except ValueError as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(interview)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class InterviewDetailView(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = InterviewSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Interview.objects.filter(user=self.request.user)


class SubmitAnswerView(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = InterviewAnswerSerializer

    @transaction.atomic
    def post(self, request, question_id):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        question = generics.get_object_or_404(
            InterviewQuestion,
            id=question_id,
            interview__user=request.user,
        )

        interview = question.interview

        if interview.status == "COMPLETED":
            return Response(
                {"detail": ("Interview has already been completed.")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if InterviewAnswer.objects.filter(question=question).exists():
            return Response(
                {"detail": ("This question has already been answered.")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        answer = InterviewAnswer.objects.create(
            interview=interview,
            question=question,
            answer=serializer.validated_data["answer"],
        )

        if interview.status == "PENDING":
            interview.status = "IN_PROGRESS"
            interview.save(update_fields=["status"])

        return Response(
            {
                "message": ("Answer submitted successfully."),
                "answer_id": answer.id,
                "question_number": (question.question_number),
            },
            status=status.HTTP_201_CREATED,
        )


class CurrentQuestionView(generics.GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = InterviewQuestionSerializer

    def get(self, request, id):

        interview = generics.get_object_or_404(
            Interview,
            id=id,
            user=request.user,
        )

        answered_ids = interview.answers.values_list(
            "question_id",
            flat=True,
        )

        question = (
            interview.questions.exclude(id__in=answered_ids)
            .order_by("question_number")
            .first()
        )

        if question is None:

            if interview.status != "COMPLETED":
                interview.status = "COMPLETED"
                interview.save(update_fields=["status"])

            return Response(
                {
                    "completed": True,
                    "interview_id": interview.id,
                    "status": interview.status,
                    "total_questions": (interview.questions.count()),
                    "answered_questions": (interview.answers.count()),
                    "message": ("Interview completed successfully."),
                }
            )

        serializer = self.get_serializer(question)

        return Response(serializer.data)


class InterviewProgressView(APIView):

    permission_classes = [IsAuthenticated]

    def get(
        self,
        request,
        interview_id,
    ):

        interview = generics.get_object_or_404(
            Interview,
            id=interview_id,
            user=request.user,
        )

        progress = ProgressService.get_progress(interview)

        return Response(progress)
