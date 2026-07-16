from .providers.gemini_provider import GeminiProvider
from .providers.question_bank_provider import QuestionBankProvider


class ProviderManager:

    def __init__(self):

        self.providers = [
            GeminiProvider(),
            QuestionBankProvider(),
        ]

    def generate_questions(self, **kwargs):

        last_error = None

        for provider in self.providers:

            try:
                print(f"Trying {provider.name}")

                return provider.generate_questions(**kwargs)

            except Exception as e:

                print(f"{provider.name} failed:", e)

                last_error = e

        raise last_error
