QUESTION_GENERATION_PROMPT = """
You are an experienced technical interviewer.

Generate {question_count} interview questions.

Role:
{role}

Experience:
{experience}

Difficulty:
{difficulty}

Skills:
{skills}

Rules:

1. Questions must be technical.
2. Cover all selected skills.
3. Mix conceptual and practical questions.
4. Return ONLY JSON.

Format:

[
    {{
        "question_number": 1,
        "skill": "Python",
        "question": "...",
        "difficulty": "MEDIUM"
    }}
]
"""
