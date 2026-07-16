from django.conf import settings
from django.db import models


class Interview(models.Model):

    DIFFICULTY_CHOICES = [
        ("EASY", "Easy"),
        ("MEDIUM", "Medium"),
        ("HARD", "Hard"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
    ]

    GENERATION_SOURCE_CHOICES = [
        ("AI", "AI"),
        ("QUESTION_BANK", "Question Bank"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="interviews",
    )

    resume = models.ForeignKey(
        "resumes.Resume",
        on_delete=models.CASCADE,
        related_name="interviews",
    )

    role = models.CharField(max_length=100)

    experience = models.CharField(max_length=50)

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
    )

    duration = models.PositiveIntegerField()

    skills = models.JSONField(default=list)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    # AI Metadata
    provider = models.CharField(
        max_length=50,
        blank=True,
    )

    generation_source = models.CharField(
        max_length=30,
        choices=GENERATION_SOURCE_CHOICES,
        default="AI",
    )

    prompt_version = models.CharField(
        max_length=20,
        default="v1",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class InterviewQuestion(models.Model):

    interview = models.ForeignKey(
        Interview,
        on_delete=models.CASCADE,
        related_name="questions",
    )

    question_number = models.PositiveIntegerField()

    skill = models.CharField(max_length=100)

    question = models.TextField()

    difficulty = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["question_number"]

    def __str__(self):
        return f"Q{self.question_number} - {self.skill}"


class QuestionBank(models.Model):

    DIFFICULTY_CHOICES = [
        ("EASY", "Easy"),
        ("MEDIUM", "Medium"),
        ("HARD", "Hard"),
    ]

    skill = models.CharField(max_length=100)

    role = models.CharField(
        max_length=100,
        blank=True,
    )

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
    )

    question = models.TextField()

    expected_answer = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = [
            "skill",
            "difficulty",
        ]

    def __str__(self):
        return f"{self.skill} - {self.question[:50]}"


class InterviewAnswer(models.Model):

    interview = models.ForeignKey(
        Interview,
        on_delete=models.CASCADE,
        related_name="answers",
    )

    question = models.OneToOneField(
        InterviewQuestion,
        on_delete=models.CASCADE,
        related_name="answer",
    )

    answer = models.TextField()

    score = models.FloatField(
        default=0,
    )

    feedback = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.interview.id} - Q{self.question.question_number}"
