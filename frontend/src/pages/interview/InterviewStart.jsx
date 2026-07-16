import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import {
  Brain,
  Clock3,
  Target,
  Sparkles,
  ShieldCheck,
  PlayCircle,
} from "lucide-react";

import Card from "../../components/ui/Card";
import Button from "../../components/ui/Button";
import Loader from "../../components/ui/Loader";

import { getInterview } from "../../services/interviewService";

function InterviewStart() {
  const { id } = useParams();

  const navigate = useNavigate();

  const [interview, setInterview] = useState(null);

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchInterview = async () => {
      try {
        const data = await getInterview(id);
        setInterview(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    };

    fetchInterview();
  }, [id]);

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

  if (!interview) {
    return <div className="p-10 text-center text-xl">Interview not found.</div>;
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
        {/* Hero Banner */}

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

            <h1 className="text-3xl font-black">AI Mock Interview</h1>
          </div>

          <p className="mt-4 max-w-2xl text-white/80">
            Prepare yourself for a realistic AI-powered interview experience
            tailored to your role, skills, and difficulty level.
          </p>
        </div>

        {/* Interview Details */}

        <div className="grid gap-6 md:grid-cols-2">
          <Card>
            <div className="flex items-center gap-3">
              <Brain size={28} className="text-violet-500" />

              <h2 className="text-xl font-bold">Interview Details</h2>
            </div>

            <div className="mt-6 space-y-5">
              <div className="flex justify-between">
                <span className="text-slate-500">Role</span>

                <span className="font-semibold">{interview.role}</span>
              </div>

              <div className="flex justify-between">
                <span className="text-slate-500">Difficulty</span>

                <span className="font-semibold">{interview.difficulty}</span>
              </div>

              <div className="flex justify-between">
                <span className="text-slate-500">Questions</span>

                <span className="font-semibold">
                  {interview.total_questions}
                </span>
              </div>

              <div className="flex justify-between">
                <span className="text-slate-500">Duration</span>

                <span className="font-semibold">{interview.duration} min</span>
              </div>
            </div>
          </Card>

          <Card>
            <div className="flex items-center gap-3">
              <ShieldCheck size={28} className="text-emerald-500" />

              <h2 className="text-xl font-bold">Instructions</h2>
            </div>

            <ul className="mt-6 space-y-4 text-slate-600 dark:text-slate-300">
              <li>• Read each question carefully before answering.</li>

              <li>• Keep your answers concise and relevant.</li>

              <li>• Do not refresh or close the browser.</li>

              <li>• Stay focused throughout the session.</li>

              <li>• AI will evaluate your responses.</li>
            </ul>
          </Card>
        </div>

        {/* Stats */}

        <div className="mt-8 grid gap-6 md:grid-cols-3">
          <Card>
            <Clock3 size={36} className="text-cyan-500" />

            <h3 className="mt-4 font-semibold">Time Limit</h3>

            <p className="mt-2 text-3xl font-black text-cyan-600">
              {interview.duration}
            </p>

            <p className="text-sm text-slate-500">Minutes</p>
          </Card>

          <Card>
            <Target size={36} className="text-violet-500" />

            <h3 className="mt-4 font-semibold">Difficulty</h3>

            <p className="mt-2 text-2xl font-black text-violet-600">
              {interview.difficulty}
            </p>
          </Card>

          <Card>
            <Brain size={36} className="text-emerald-500" />

            <h3 className="mt-4 font-semibold">Questions</h3>

            <p className="mt-2 text-3xl font-black text-emerald-600">
              {interview.total_questions}
            </p>
          </Card>
        </div>

        {/* Start Button */}

        <div className="mt-10">
          <Button
            onClick={() => navigate(`/interview/${id}/session`)}
            className="
              flex
              items-center
              justify-center
              gap-3
            "
          >
            <PlayCircle size={20} />
            Start Interview
          </Button>
        </div>
      </div>
    </div>
  );
}

export default InterviewStart;
