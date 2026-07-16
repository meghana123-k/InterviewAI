from .manager import ProviderManager


class QuestionGenerator:

    def __init__(self):

        self.manager = ProviderManager()

    def generate_questions(self, **kwargs):

        return self.manager.generate_questions(**kwargs)
