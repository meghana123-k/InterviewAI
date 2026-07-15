from rest_framework import generics, permissions

from .models import Resume
from .serializers import ResumeSerializer
from .skill_extractor import SkillExtractor
from .utils import extract_text_from_pdf


class ResumeUploadView(generics.CreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        resume = serializer.save(user=self.request.user)

        extracted_text = extract_text_from_pdf(resume.file.path)

        extractor = SkillExtractor(
            enable_fuzzy=True,
            enable_ner=False,
        )

        skills = extractor.extract_skills(extracted_text)

        resume.extracted_text = extracted_text
        resume.extracted_skills = skills

        resume.save(
            update_fields=[
                "extracted_text",
                "extracted_skills",
            ]
        )


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Resume
from .serializers import ResumeSerializer


class LatestResumeView(generics.RetrieveUpdateAPIView):

    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.resumes.first()

    def perform_update(self, serializer):
        serializer.save(resume_status="READY")
