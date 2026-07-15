from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from .serializers import InterviewSerializer
from .services.interview_service import InterviewService


class InterviewCreateView(generics.CreateAPIView):

    serializer_class = InterviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        interview = InterviewService.create_interview(
            request.user,
            serializer.validated_data,
        )

        output = InterviewSerializer(interview)

        return Response(
            output.data,
            status=status.HTTP_201_CREATED,
        )
