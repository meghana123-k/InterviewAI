import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import Card from "../../components/ui/Card";
import Button from "../../components/ui/Button";

import { getLatestResume } from "../../services/resumeService";
import { createInterview } from "../../services/interviewService";

const InterviewConfig = () => {
  const navigate = useNavigate();

  const [resume, setResume] = useState(null);

  const [formData, setFormData] = useState({
    role: "Software Engineer",
    experience: "Fresher",
    difficulty: "MEDIUM",
    duration: 20,
    skills: [],
  });

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadResume();
  }, []);

  const loadResume = async () => {
    try {
      const data = await getLatestResume();

      setResume(data);

      setFormData((prev) => ({
        ...prev,
        skills: data.extracted_skills || [],
      }));
    } catch (error) {
      console.error(error);
    }
  };

  const toggleSkill = (skill) => {
    setFormData((prev) => ({
      ...prev,
      skills: prev.skills.includes(skill)
        ? prev.skills.filter((s) => s !== skill)
        : [...prev.skills, skill],
    }));
  };

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      setLoading(true);

      const interview = await createInterview(formData);

      navigate(`/interview/${interview.id}`);
    } catch (error) {
      console.error(error);
      alert("Failed to create interview.");
    } finally {
      setLoading(false);
    }
  };

  if (!resume) {
    return <div className="text-center mt-20">No finalized resume found.</div>;
  }

  return (
    <div className="max-w-4xl mx-auto mt-10">
      <Card>
        <h1 className="text-3xl font-bold mb-8">Configure Interview</h1>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="font-medium">Role</label>

            <input
              className="w-full border rounded-lg p-3 mt-2"
              name="role"
              value={formData.role}
              onChange={handleChange}
            />
          </div>

          <div className="grid grid-cols-2 gap-6">
            <div>
              <label className="font-medium">Experience</label>

              <select
                className="w-full border rounded-lg p-3 mt-2"
                name="experience"
                value={formData.experience}
                onChange={handleChange}
              >
                <option>Fresher</option>
                <option>1-2 Years</option>
                <option>3-5 Years</option>
              </select>
            </div>

            <div>
              <label className="font-medium">Difficulty</label>

              <select
                className="w-full border rounded-lg p-3 mt-2"
                name="difficulty"
                value={formData.difficulty}
                onChange={handleChange}
              >
                <option value="EASY">Easy</option>
                <option value="MEDIUM">Medium</option>
                <option value="HARD">Hard</option>
              </select>
            </div>
          </div>

          <div>
            <label className="font-medium">Duration</label>

            <select
              className="w-full border rounded-lg p-3 mt-2"
              name="duration"
              value={formData.duration}
              onChange={handleChange}
            >
              <option value={10}>10 Minutes</option>
              <option value={20}>20 Minutes</option>
              <option value={30}>30 Minutes</option>
            </select>
          </div>

          <div>
            <h2 className="font-semibold mb-4">Skills</h2>

            <div className="flex flex-wrap gap-3">
              {resume.extracted_skills.map((skill) => (
                <button
                  type="button"
                  key={skill}
                  onClick={() => toggleSkill(skill)}
                  className={`px-4 py-2 rounded-full border ${
                    formData.skills.includes(skill)
                      ? "bg-violet-600 text-white"
                      : "bg-white"
                  }`}
                >
                  {skill}
                </button>
              ))}
            </div>
          </div>

          <Button type="submit" disabled={loading} className="w-full">
            {loading ? "Creating Interview..." : "Start Interview"}
          </Button>
        </form>
      </Card>
    </div>
  );
};

export default InterviewConfig;
