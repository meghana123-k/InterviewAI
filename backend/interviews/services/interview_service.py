from interviews.ai.question_generator import QuestionGenerator
from resumes.models import Resume

from interviews.models import Interview, InterviewQuestion


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
        generator = QuestionGenerator()

        questions = generator.generate_questions(
            role=interview.role,
            experience=interview.experience,
            difficulty=interview.difficulty,
            skills=interview.skills,
            question_count=max(5, interview.duration // 2),
        )
        for q in questions:
            InterviewQuestion.objects.create(
                interview=interview,
                question_number=q["question_number"],
                skill=q["skill"],
                question=q["question"],
                difficulty=q["difficulty"],
            )
        return interview
