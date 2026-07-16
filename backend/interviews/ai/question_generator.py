import json

from .prompts import QUESTION_GENERATION_PROMPT
from .providers import GeminiProvider


class QuestionGenerator:

    def __init__(self):
        self.provider = GeminiProvider()

    def generate_questions(
        self,
        role,
        experience,
        difficulty,
        skills,
        question_count,
    ):

        prompt = QUESTION_GENERATION_PROMPT.format(
            role=role,
            experience=experience,
            difficulty=difficulty,
            skills=", ".join(skills),
            question_count=question_count,
        )

        response = self.provider.generate(prompt)

        if response.startswith("```"):
            response = response.split("\n", 1)[1]
            response = response.rsplit("```", 1)[0]

        return json.loads(response)
