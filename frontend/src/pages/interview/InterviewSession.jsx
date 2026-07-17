// path: frontend/src/pages/interview/InterviewSession.jsx

import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";

import useInterview from "../../hooks/useInterview";

import InterviewHeader from "../../components/interview/InterviewHeader";
import ProgressCard from "../../components/interview/ProgressCard";
import QuestionCard from "../../components/interview/QuestionCard";
import AnswerBox from "../../components/interview/AnswerBox";
import AIInfoCard from "../../components/interview/AIInfoCard";
import FeedbackCard from "../../components/interview/FeedbackCard";

export default function InterviewSession() {
  const { id } = useParams();
  const navigate = useNavigate();

  const { question, progress, loading, submitting, completed, submitAnswer } =
    useInterview(id);

  const [answer, setAnswer] = useState("");

  useEffect(() => {
    if (completed) {
      navigate(`/interview/${id}/completed`, {
        replace: true,
      });
    }
  }, [completed, id, navigate]);

  const handleSubmit = async () => {
    if (!answer.trim()) {
      alert("Please enter your answer.");
      return;
    }

    try {
      await submitAnswer(answer);
      setAnswer("");
    } catch (error) {
      alert(error?.response?.data?.detail || "Failed to submit answer.");
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        Loading interview...
      </div>
    );
  }

  if (!question) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        No question available.
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
        dark:from-slate-950
        dark:via-slate-900
        dark:to-indigo-950
      "
    >
      <div className="mx-auto max-w-7xl px-6 py-10">
        <InterviewHeader />

        <div className="grid gap-6 lg:grid-cols-3">
          <div className="lg:col-span-2">
            <QuestionCard question={question} progress={progress} />

            <AnswerBox
              answer={answer}
              setAnswer={setAnswer}
              submitting={submitting}
              onSubmit={handleSubmit}
            />
          </div>

          <div className="space-y-6">
            <ProgressCard progress={progress} />

            <AIInfoCard />

            <FeedbackCard />
          </div>
        </div>
      </div>
    </div>
  );
}
