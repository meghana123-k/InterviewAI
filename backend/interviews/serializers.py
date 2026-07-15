from rest_framework import serializers

from .models import Interview


class InterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interview

        fields = (
            "id",
            "role",
            "experience",
            "difficulty",
            "duration",
            "skills",
            "status",
            "created_at",
        )

        read_only_fields = (
            "id",
            "status",
            "created_at",
        )
