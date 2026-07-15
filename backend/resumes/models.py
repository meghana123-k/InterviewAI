from django.contrib.auth.models import User
from django.db import models


class Resume(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="resume",
    )

    file = models.FileField(upload_to="resumes/")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    extracted_text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} Resume"
