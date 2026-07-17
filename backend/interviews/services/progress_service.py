class ProgressService:

    @staticmethod
    def get_progress(interview):

        total_questions = interview.questions.count()
        answered_questions = interview.answers.count()

        remaining_questions = max(
            total_questions - answered_questions,
            0,
        )

        progress_percentage = (
            round(answered_questions * 100 / total_questions) if total_questions else 0
        )

        current_question = min(
            answered_questions + 1,
            total_questions,
        )

        return {
            "total_questions": total_questions,
            "answered_questions": answered_questions,
            "remaining_questions": remaining_questions,
            "current_question": current_question,
            "progress_percentage": progress_percentage,
            "status": interview.status,
        }
