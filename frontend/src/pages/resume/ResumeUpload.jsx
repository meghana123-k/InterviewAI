// path: frontend/src/pages/resume/ResumeUpload.jsx
import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { UploadCloud, FileText, Sparkles, CheckCircle2 } from "lucide-react";

import Card from "../../components/ui/Card";
import Button from "../../components/ui/Button";

import { uploadResume } from "../../services/resumeService";

function ResumeUpload() {
  const navigate = useNavigate();

  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const [message, setMessage] = useState("");
  const [success, setSuccess] = useState(false);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files?.[0];

    if (!selectedFile) return;

    if (selectedFile.type !== "application/pdf") {
      setMessage("Only PDF files are allowed.");
      setSuccess(false);
      return;
    }

    setFile(selectedFile);
    setMessage("");
  };

  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file) {
      setMessage("Please select a PDF file.");
      setSuccess(false);
      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    try {
      setLoading(true);

      await uploadResume(formData);

      setSuccess(true);

      setMessage("Resume uploaded successfully. Redirecting...");

      setTimeout(() => {
        navigate("/resume/review");
      }, 1200);
    } catch (error) {
      console.error(error);

      setSuccess(false);

      setMessage("Resume upload failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="
        min-h-screen
        bg-gradient-to-br
        from-slate-100
        via-violet-50
        to-cyan-50
        px-5
        py-10
        dark:from-slate-950
        dark:via-slate-900
        dark:to-indigo-950
      "
    >
      <div className="mx-auto max-w-4xl">
        {/* Header */}

        <div className="mb-8">
          <h1
            className="
              text-5xl
              font-black
              text-slate-800
              dark:text-white
            "
          >
            Upload Resume
          </h1>

          <p className="mt-3 text-slate-500 dark:text-slate-400">
            Upload your resume and let AI analyze your skills and experience.
          </p>
        </div>

        {/* AI Banner */}

        <div
          className="
            mb-8
            rounded-3xl
            bg-gradient-to-r
            from-violet-600
            via-indigo-600
            to-cyan-600
            p-8
            text-white
            shadow-2xl
          "
        >
          <div className="flex items-center gap-3">
            <Sparkles size={34} />

            <h2 className="text-2xl font-bold">AI Resume Scanner</h2>
          </div>

          <p className="mt-4 max-w-2xl text-white/80">
            Our AI extracts skills, technologies, experience, and strengths to
            personalize your interview preparation.
          </p>
        </div>

        {/* Upload Card */}

        <Card>
          <form onSubmit={handleUpload} className="space-y-6">
            <label
              className="
                flex
                cursor-pointer
                flex-col
                items-center
                justify-center
                rounded-3xl
                border-2
                border-dashed
                border-violet-300
                bg-violet-50/50
                p-12
                transition
                hover:border-violet-500
                hover:bg-violet-100/40
                dark:border-violet-800
                dark:bg-slate-900/40
              "
            >
              <UploadCloud size={60} className="text-violet-500" />

              <h3 className="mt-4 text-xl font-bold">Choose Resume PDF</h3>

              <p className="mt-2 text-sm text-slate-500">
                Click to browse and upload your resume
              </p>

              <input
                type="file"
                accept=".pdf"
                onChange={handleFileChange}
                className="hidden"
              />
            </label>

            {file && (
              <div
                className="
                  flex
                  items-center
                  gap-4
                  rounded-2xl
                  bg-slate-100
                  p-4
                  dark:bg-slate-800
                "
              >
                <FileText size={30} className="text-red-500" />

                <div>
                  <p className="font-semibold">{file.name}</p>

                  <p className="text-sm text-slate-500">
                    {(file.size / 1024).toFixed(1)} KB
                  </p>
                </div>
              </div>
            )}

            {message && (
              <div
                className={`
                  rounded-2xl
                  p-4
                  text-center
                  font-medium
                  ${
                    success
                      ? "bg-green-100 text-green-700"
                      : "bg-red-100 text-red-700"
                  }
                `}
              >
                <div className="flex items-center justify-center gap-2">
                  {success && <CheckCircle2 size={18} />}

                  {message}
                </div>
              </div>
            )}

            <Button type="submit" disabled={loading}>
              {loading ? "Analyzing Resume..." : "Upload & Analyze"}
            </Button>
          </form>
        </Card>

        {/* Features */}

        <div className="mt-8 grid gap-6 md:grid-cols-3">
          <Card>
            <h3 className="font-bold">Skill Extraction</h3>

            <p className="mt-3 text-sm text-slate-500">
              AI automatically identifies technical and professional skills.
            </p>
          </Card>

          <Card>
            <h3 className="font-bold">ATS Optimization</h3>

            <p className="mt-3 text-sm text-slate-500">
              Improve resume quality for recruiter screening systems.
            </p>
          </Card>

          <Card>
            <h3 className="font-bold">Interview Readiness</h3>

            <p className="mt-3 text-sm text-slate-500">
              Personalized interview recommendations based on your resume.
            </p>
          </Card>
        </div>
      </div>
    </div>
  );
}

export default ResumeUpload;