import json

from django.conf import settings
from google import genai

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def parse_resume(text: str):
    prompt = f"""
Extract the following resume into JSON.

Return ONLY valid JSON.

Structure:

{{
  "name": "",
  "email": "",
  "phone": "",
  "skills": [],
  "education": [],
  "experience": [],
  "projects": [],
  "certifications": []
}}

Resume:

{text}
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    response_text = response.text.strip()

    # Remove Markdown code fences if present
    if response_text.startswith("```"):
        response_text = response_text.split("\n", 1)[1]
        response_text = response_text.rsplit("```", 1)[0].strip()

    return json.loads(response_text)
