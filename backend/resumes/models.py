from django.conf import settings
from django.db import models


class Resume(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("READY", "Ready"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="resumes",
    )

    file = models.FileField(upload_to="resumes/")

    extracted_text = models.TextField(blank=True)

    extracted_skills = models.JSONField(
        default=list,
        blank=True,
    )

    resume_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]
