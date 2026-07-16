
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  Brain,
  Sparkles,
  Clock3,
  Target,
} from "lucide-react";

import Card from "../../components/ui/Card";
import Button from "../../components/ui/Button";
import Input from "../../components/ui/Input";
import Loader from "../../components/ui/Loader";

import { getLatestResume } from "../../services/resumeService";
import { createInterview } from "../../services/interviewService";

const DEFAULT_CONFIG = {
  role: "Software Engineer",
  experience: "Fresher",
  difficulty: "MEDIUM",
  duration: 20,
  skills: [],
};

function InterviewConfig() {
  const navigate = useNavigate();

  const [resume, setResume] = useState(null);

  const [formData, setFormData] = useState(DEFAULT_CONFIG);

  const [resumeLoading, setResumeLoading] = useState(true);

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
    } finally {
      setResumeLoading(false);
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
    const { name, value } = e.target;

    setFormData((prev) => ({
      ...prev,
      [name]: name === "duration" ? Number(value) : value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (formData.skills.length === 0) {
      alert("Please select at least one skill.");
      return;
    }

    try {
      setLoading(true);

      const interview = await createInterview(formData);

      navigate(`/interview/${interview.id}`);
    } catch (error) {
      console.error(error);

      alert(
        error?.response?.data?.detail ||
          "Failed to create interview."
      );
    } finally {
      setLoading(false);
    }
  };

  if (resumeLoading) {
    return (
      <div
        className="
          flex
          min-h-screen
          items-center
          justify-center
          bg-gradient-to-br
          from-slate-100
          via-violet-50
          to-cyan-50
          dark:from-slate-950
          dark:via-slate-900
          dark:to-indigo-950
        "
      >
        <Loader />
      </div>
    );
  }

  if (!resume) {
    return (
      <div
        className="
          flex
          min-h-screen
          items-center
          justify-center
          text-center
          text-xl
          font-semibold
        "
      >
        No finalized resume found.
      </div>
    );
  }

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
      <div className="mx-auto max-w-5xl">
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
            <Sparkles size={32} />

            <h1 className="text-3xl font-black">
              Configure AI Interview
            </h1>
          </div>

          <p className="mt-4 text-white/80">
            Customize your interview settings and start
            practicing with AI-generated questions.
          </p>
        </div>

        <Card>
          <form
            onSubmit={handleSubmit}
            className="space-y-8"
          >
            <Input
              label="Role"
              name="role"
              value={formData.role}
              onChange={handleChange}
              placeholder="Enter target role"
            />

            <div className="grid gap-6 md:grid-cols-2">
              <div>
                <label className="mb-2 block font-medium">
                  Experience
                </label>

                <select
                  disabled={loading}
                  name="experience"
                  value={formData.experience}
                  onChange={handleChange}
                  className="
                    w-full
                    rounded-xl
                    border
                    border-slate-300
                    bg-white/80
                    px-4
                    py-3
                    dark:border-slate-700
                    dark:bg-slate-800/60
                  "
                >
                  <option>Fresher</option>
                  <option>1-2 Years</option>
                  <option>3-5 Years</option>
                </select>
              </div>

              <div>
                <label className="mb-2 block font-medium">
                  Difficulty
                </label>

                <select
                  disabled={loading}
                  name="difficulty"
                  value={formData.difficulty}
                  onChange={handleChange}
                  className="
                    w-full
                    rounded-xl
                    border
                    border-slate-300
                    bg-white/80
                    px-4
                    py-3
                    dark:border-slate-700
                    dark:bg-slate-800/60
                  "
                >
                  <option value="EASY">Easy</option>
                  <option value="MEDIUM">Medium</option>
                  <option value="HARD">Hard</option>
                </select>
              </div>
            </div>

            <div>
              <label className="mb-2 block font-medium">
                Duration
              </label>

              <select
                disabled={loading}
                name="duration"
                value={formData.duration}
                onChange={handleChange}
                className="
                  w-full
                  rounded-xl
                  border
                  border-slate-300
                  bg-white/80
                  px-4
                  py-3
                  dark:border-slate-700
                  dark:bg-slate-800/60
                "
              >
                <option value={10}>10 Minutes</option>
                <option value={20}>20 Minutes</option>
                <option value={30}>30 Minutes</option>
              </select>
            </div>

            <div>
              <h2 className="mb-4 text-xl font-bold">
                Select Skills
              </h2>

              <div className="flex flex-wrap gap-3">
                {(resume.extracted_skills || []).map(
                  (skill) => (
                    <button
                      key={skill}
                      type="button"
                      disabled={loading}
                      onClick={() =>
                        toggleSkill(skill)
                      }
                      className={`
                        rounded-full
                        border
                        px-4
                        py-2
                        font-medium
                        transition-all
                        duration-300
                        ${
                          formData.skills.includes(skill)
                            ? "bg-gradient-to-r from-violet-600 to-cyan-500 text-white border-transparent"
                            : "bg-white dark:bg-slate-800 border-slate-300 dark:border-slate-700"
                        }
                      `}
                    >
                      {skill}
                    </button>
                  )
                )}
              </div>
            </div>

            <div className="grid gap-4 md:grid-cols-3">
              <div className="rounded-2xl bg-white/50 p-5 dark:bg-slate-900/40">
                <Brain className="text-violet-500" />
                <h3 className="mt-3 font-semibold">
                  Skills
                </h3>
                <p className="text-3xl font-black text-violet-600">
                  {formData.skills.length}
                </p>
              </div>

              <div className="rounded-2xl bg-white/50 p-5 dark:bg-slate-900/40">
                <Clock3 className="text-cyan-500" />
                <h3 className="mt-3 font-semibold">
                  Duration
                </h3>
                <p className="text-3xl font-black text-cyan-600">
                  {formData.duration}
                </p>
              </div>

              <div className="rounded-2xl bg-white/50 p-5 dark:bg-slate-900/40">
                <Target className="text-emerald-500" />
                <h3 className="mt-3 font-semibold">
                  Level
                </h3>
                <p className="text-xl font-black text-emerald-600">
                  {formData.difficulty}
                </p>
              </div>
            </div>

            <Button
              type="submit"
              disabled={loading}
            >
              {loading
                ? "Creating Interview..."
                : "Start AI Interview"}
            </Button>
          </form>
        </Card>
      </div>
    </div>
  );
}

export default InterviewConfig;
