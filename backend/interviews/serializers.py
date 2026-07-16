from rest_framework import serializers

from .models import Interview


class InterviewSerializer(serializers.ModelSerializer):

    total_questions = serializers.SerializerMethodField()

    answered_questions = serializers.SerializerMethodField()

    class Meta:
        model = Interview

        fields = [
            "id",
            "role",
            "experience",
            "difficulty",
            "duration",
            "status",
            "provider",
            "generation_source",
            "prompt_version",
            "created_at",
            "total_questions",
            "answered_questions",
        ]

    def get_total_questions(self, obj):
        return obj.questions.count()

    def get_answered_questions(self, obj):
        return obj.answers.count()
from .models import InterviewQuestion


class InterviewQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = InterviewQuestion

        fields = [
            "id",
            "question_number",
            "skill",
            "question",
            "difficulty",
        ]


class InterviewAnswerSerializer(serializers.Serializer):

    answer = serializers.CharField(
        trim_whitespace=True,
        allow_blank=False,
        max_length=5000,
    )
