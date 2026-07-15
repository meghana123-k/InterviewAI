import { useState } from "react";

import Card from "../../components/ui/Card";
import Button from "../../components/ui/Button";

import { uploadResume } from "../../services/resumeService";

const ResumeUpload = () => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file) {
      setMessage("Please select a PDF file.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setMessage("");

      await uploadResume(formData);

      setMessage("Resume uploaded successfully.");
      setFile(null);

      e.target.reset();
    } catch (error) {
      console.error(error);
      setMessage("Upload failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto mt-10">
      <Card>
        <h2 className="text-2xl font-bold mb-6">Upload Resume</h2>

        <form onSubmit={handleUpload} className="space-y-5">
          <input
            type="file"
            accept=".pdf"
            onChange={(e) => setFile(e.target.files[0])}
            className="w-full"
          />

          <Button type="submit" disabled={loading} className="w-full">
            {loading ? "Uploading..." : "Upload Resume"}
          </Button>
        </form>

        {message && <p className="mt-5 text-center">{message}</p>}
      </Card>
    </div>
  );
};

export default ResumeUpload;
