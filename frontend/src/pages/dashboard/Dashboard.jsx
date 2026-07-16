// path: frontend/src/pages/dashboard/Dashboard.jsx

import Navbar from "../../components/layout/Navbar";
import Button from "../../components/ui/Button";
import { useEffect, useState } from "react";
import { getLatestResume } from "../../services/resumeService";

import { Link } from "react-router-dom";

import { FileText, Brain, Trophy, Sparkles } from "lucide-react";

function Dashboard() {
  const [resume, setResume] = useState(null);
  const [loadingResume, setLoadingResume] = useState(true);
  useEffect(() => {
    fetchResume();
  }, []);

  const fetchResume = async () => {
    try {
      const data = await getLatestResume();
      setResume(data);
    } catch (error) {
      // No resume uploaded yet (404 or similar)
      setResume(null);
    } finally {
      setLoadingResume(false);
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
        dark:from-slate-950
        dark:via-slate-900
        dark:to-indigo-950
      "
    >
      <Navbar />
      <main className="mx-auto max-w-7xl px-6 py-10">
        <div className="mb-10">
          <h1
            className="
              text-5xl
              font-black
              text-slate-800
              dark:text-white
            "
          >
            Welcome Back 👋
          </h1>

          <p className="mt-3 text-slate-500 dark:text-slate-400">
            Track your interview preparation journey.
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-3">
          <div
            className="
              rounded-3xl
              border
              border-white/20
              bg-white/60
              p-6
              shadow-xl
              backdrop-blur-xl
              dark:bg-slate-900/60
            "
          >
            <Brain size={40} className="text-violet-500" />

            <h2 className="mt-4 text-lg font-semibold">Interviews</h2>

            <p className="mt-3 text-5xl font-black text-violet-600">0</p>
          </div>

          <div
            className="
              rounded-3xl
              border
              border-white/20
              bg-white/60
              p-6
              shadow-xl
              backdrop-blur-xl
              dark:bg-slate-900/60
            "
          >
            <Trophy size={40} className="text-emerald-500" />

            <h2 className="mt-4 text-lg font-semibold">Average Score</h2>

            <p className="mt-3 text-5xl font-black text-emerald-600">--</p>
          </div>

          <div
            className="
              rounded-3xl
              border
              border-white/20
              bg-white/60
              p-6
              shadow-xl
              backdrop-blur-xl
              dark:bg-slate-900/60
            "
          >
            <FileText size={40} className="text-cyan-500" />

            <h2 className="mt-4 text-lg font-semibold">Resume Status</h2>

            {loadingResume ? (
              <p className="mt-3 text-lg text-slate-500">Loading...</p>
            ) : !resume ? (
              <p className="mt-3 text-lg text-red-500">Not Uploaded</p>
            ) : resume.resume_status === "READY" ? (
              <p className="mt-3 text-lg font-semibold text-green-600">Ready</p>
            ) : (
              <p className="mt-3 text-lg font-semibold text-yellow-500">
                Pending Review
              </p>
            )}
          </div>
        </div>

        <div
          className="
            mt-10
            rounded-3xl
            overflow-hidden
            bg-gradient-to-r
            from-violet-600
            via-indigo-600
            to-cyan-600
            p-10
            text-white
            shadow-2xl
          "
        >
          <Sparkles size={42} />

          <h2 className="mt-4 text-3xl font-black">AI Resume Analysis</h2>

          <p className="mt-3 max-w-xl text-white/80">
            Upload your resume and get instant AI-powered feedback, ATS score,
            strengths, weaknesses, and improvement suggestions.
          </p>

          <div className="mt-6 flex flex-wrap gap-4">
            <Link to="/resume/upload">
              <Button className="bg-white text-black hover:bg-slate-200">
                {resume ? "Update Resume" : "Upload Resume"}
              </Button>
            </Link>

            {resume?.resume_status === "READY" && (
              <Link to="/interview/configure">
                <Button>Start Interview</Button>
              </Link>
            )}
          </div>
        </div>
        <div className="mt-10 grid gap-6 lg:grid-cols-2">
          <div
            className="
              rounded-3xl
              bg-white/60
              p-8
              shadow-xl
              backdrop-blur-xl
              dark:bg-slate-900/60
            "
          >
            <h3 className="text-xl font-bold">Interview Progress</h3>

            <div className="mt-6">
              <div className="mb-3 flex justify-between">
                <span>Completion</span>

                <span>0%</span>
              </div>

              <div className="h-4 rounded-full bg-slate-200 dark:bg-slate-800">
                <div className="h-4 w-0 rounded-full bg-gradient-to-r from-violet-500 to-cyan-500"></div>
              </div>
            </div>
          </div>

          <div
            className="
              rounded-3xl
              bg-white/60
              p-8
              shadow-xl
              backdrop-blur-xl
              dark:bg-slate-900/60
            "
          >
            <h3 className="text-xl font-bold">AI Insights</h3>

            <p className="mt-4 text-slate-500 dark:text-slate-400">
              Complete interviews to receive AI-generated strengths, weaknesses,
              and personalized improvement recommendations.
            </p>
          </div>
        </div>
      </main>
    </div>
  );
}

export default Dashboard;
