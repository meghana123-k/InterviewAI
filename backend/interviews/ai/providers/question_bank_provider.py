import random

from interviews.models import QuestionBank

from ..base_provider import BaseProvider


class QuestionBankProvider(BaseProvider):

    name = "Question Bank"

    def generate_questions(
        self,
        role,
        experience,
        difficulty,
        skills,
        question_count,
    ):

        questions = []

        for skill in skills:

            queryset = QuestionBank.objects.filter(
                skill__iexact=skill,
                difficulty=difficulty,
                is_active=True,
            )

            questions.extend(list(queryset))

        if len(questions) < question_count:
            raise ValueError("Not enough questions in Question Bank.")

        selected = random.sample(
            questions,
            question_count,
        )

        result = []

        for index, question in enumerate(selected, start=1):

            result.append(
                {
                    "question_number": index,
                    "skill": question.skill,
                    "question": question.question,
                    "difficulty": question.difficulty,
                }
            )

        return result
