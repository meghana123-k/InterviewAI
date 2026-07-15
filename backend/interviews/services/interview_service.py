from resumes.models import Resume

from interviews.models import Interview


class InterviewService:

    @staticmethod
    def create_interview(user, validated_data):

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

        return interview
