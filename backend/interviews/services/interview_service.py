from django.db import transaction

from interviews.ai.question_generator import QuestionGenerator
from interviews.models import Interview, InterviewQuestion


class InterviewService:

    @staticmethod
    @transaction.atomic
    def create_interview(user, validated_data):
        active_interview = user.interviews.filter(
            status__in=[
                "PENDING",
                "IN_PROGRESS",
            ]
        ).first()

        if active_interview:
            raise ValueError(
                "Finish your current interview before creating a new one."
            )
        resume = user.resumes.filter(resume_status="READY").first()

        if resume is None:
            raise ValueError("No finalized resume found.")

        interview = Interview.objects.create(
            user=user,
            resume=resume,
            role=validated_data["role"],
            experience=validated_data["experience"],
            difficulty=validated_data["difficulty"],
            duration=validated_data["duration"],
            skills=validated_data["skills"],
        )

        generator = QuestionGenerator()

        questions = generator.generate_questions(
            role=interview.role,
            experience=interview.experience,
            difficulty=interview.difficulty,
            skills=interview.skills,
            question_count=max(
                5,
                interview.duration // 2,
            ),
        )

        for question in questions:

            InterviewQuestion.objects.create(
                interview=interview,
                question_number=question["question_number"],
                skill=question["skill"],
                question=question["question"],
                difficulty=question["difficulty"],
            )

        interview.provider = "Gemini"

        interview.generation_source = "AI"

        interview.prompt_version = "v1"

        interview.save(
            update_fields=[
                "provider",
                "generation_source",
                "prompt_version",
            ]
        )

        return interview
