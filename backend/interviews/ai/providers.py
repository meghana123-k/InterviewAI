from django.conf import settings
from google import genai


class GeminiProvider:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    def generate(self, prompt):
        response = self.client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt,
        )

        return response.text
