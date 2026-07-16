import json
import time

from django.conf import settings
from google import genai

from google.genai.errors import (
    ClientError,
    ServerError,
)

from ..base_provider import BaseProvider
from interviews.ai.prompts import QUESTION_GENERATION_PROMPT


class GeminiProvider(BaseProvider):

    name = "Gemini"

    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

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

        for attempt in range(3):

            try:

                response = self.client.models.generate_content(
                    model=settings.GEMINI_MODEL,
                    contents=prompt,
                )

                text = response.text.strip()

                if text.startswith("```"):
                    text = text.split("\n", 1)[1]
                    text = text.rsplit("```", 1)[0].strip()

                return json.loads(text)

            except ServerError:

                print(f"Gemini unavailable. Retry {attempt + 1}/3")

                if attempt == 2:
                    raise

                time.sleep(2**attempt)

            except ClientError:
                raise
