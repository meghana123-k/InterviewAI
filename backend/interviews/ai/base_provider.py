from abc import ABC, abstractmethod


class BaseProvider(ABC):

    name = "base"

    @abstractmethod
    def generate_questions(
        self,
        role,
        experience,
        difficulty,
        skills,
        question_count,
    ):
        pass
