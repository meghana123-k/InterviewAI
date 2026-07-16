import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import { Sparkles, Brain, CheckCircle2 } from "lucide-react";

import Card from "../../components/ui/Card";
import Button from "../../components/ui/Button";
import Loader from "../../components/ui/Loader";

import SkillChip from "../../components/resume/SkillChip";
import SkillInput from "../../components/resume/SkillInput";

import { getLatestResume, updateResume } from "../../services/resumeService";

function ResumeReview() {
  const navigate = useNavigate();

  const [resume, setResume] = useState(null);
  const [skills, setSkills] = useState([]);

  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    loadResume();
  }, []);

  const loadResume = async () => {
    try {
      const data = await getLatestResume();

      setResume(data);
      setSkills(data.extracted_skills || []);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  const removeSkill = (skill) => {
    setSkills(skills.filter((s) => s !== skill));
  };

  const addSkill = (skill) => {
    if (!skill.trim()) return;

    if (skills.includes(skill)) return;

    setSkills([...skills, skill]);
  };

  const saveResume = async () => {
    try {
      setSaving(true);

      await updateResume({
        extracted_skills: skills,
      });

      navigate("/dashboard");
    } catch (error) {
      console.error(error);
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
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
      <div className="mx-auto max-w-6xl">
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
            Resume Review
          </h1>

          <p className="mt-3 text-slate-500 dark:text-slate-400">
            Review and refine AI-detected skills before continuing.
          </p>
        </div>

        {/* AI Banner */}

        <div
          className="
            mb-8
            overflow-hidden
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
            <h2 className="text-2xl font-bold">AI Resume Analysis</h2>
          </div>

          <p className="mt-4 max-w-2xl text-white/80">
            Our AI has scanned your resume and extracted the most relevant
            skills. Review them carefully before saving.
          </p>
        </div>

        {/* Main Content */}

        <Card>
          <div className="flex items-center gap-3 mb-6">
            <Brain size={28} className="text-violet-500" />

            <h2 className="text-2xl font-bold">Detected Skills</h2>
          </div>

          {skills.length === 0 ? (
            <div
              className="
                rounded-2xl
                border
                border-dashed
                border-slate-300
                p-8
                text-center
                dark:border-slate-700
              "
            >
              <p className="text-slate-500">No skills detected yet.</p>
            </div>
          ) : (
            <div className="flex flex-wrap gap-3">
              {skills.map((skill) => (
                <SkillChip key={skill} skill={skill} onRemove={removeSkill} />
              ))}
            </div>
          )}

          <div className="mt-8">
            <SkillInput onAdd={addSkill} />
          </div>

          <div
            className="
              mt-10
              rounded-2xl
              bg-violet-50
              p-5
              dark:bg-slate-800
            "
          >
            <div className="flex items-start gap-3">
              <CheckCircle2 className="mt-1 text-green-500" size={20} />

              <div>
                <h3 className="font-semibold">Review Tip</h3>

                <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">
                  Remove irrelevant skills and add any missing technologies to
                  improve interview recommendations and ATS matching.
                </p>
              </div>
            </div>
          </div>

          <div className="mt-8">
            <Button onClick={saveResume} disabled={saving}>
              {saving ? "Saving Resume..." : "Save & Continue"}
            </Button>
          </div>
        </Card>

        {/* Stats Section */}

        <div className="mt-8 grid gap-6 md:grid-cols-3">
          <Card>
            <h3 className="text-lg font-semibold">Skills Found</h3>

            <p className="mt-4 text-4xl font-black text-violet-600">
              {skills.length}
            </p>
          </Card>

          <Card>
            <h3 className="text-lg font-semibold">Resume Status</h3>

            <p className="mt-4 text-xl font-bold text-emerald-600">Uploaded</p>
          </Card>

          <Card>
            <h3 className="text-lg font-semibold">AI Ready</h3>

            <p className="mt-4 text-xl font-bold text-cyan-600">Yes</p>
          </Card>
        </div>
      </div>
    </div>
  );
}

export default ResumeReview;
