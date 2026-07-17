from interviews.models import InterviewQuestion


class ProgressService:

    @staticmethod
    def get_progress(interview):
        total_questions = InterviewQuestion.objects.filter(interview=interview).count()

        answered_questions = InterviewQuestion.objects.filter(
            interview=interview,
            is_answered=True,
        ).count()

        remaining_questions = total_questions - answered_questions

        progress_percentage = (
            round((answered_questions / total_questions) * 100)
            if total_questions > 0
            else 0
        )

        return {
            "total_questions": total_questions,
            "answered_questions": answered_questions,
            "remaining_questions": remaining_questions,
            "current_question": (
                answered_questions + 1
                if answered_questions < total_questions
                else total_questions
            ),
            "progress_percentage": progress_percentage,
            "status": interview.status,
        }
