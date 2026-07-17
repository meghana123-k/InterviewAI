// path: frontend/src/components/interview/ProgressCard.jsx

import { CheckCircle2 } from "lucide-react";

export default function ProgressCard({ progress }) {
  const progressPercentage = progress?.progress_percentage || 0;

  const currentQuestion = progress?.current_question || 0;

  const totalQuestions = progress?.total_questions || 0;

  return (
    <div
      className="
        rounded-3xl
        bg-white/70
        p-6
        shadow-xl
        backdrop-blur-xl
        dark:bg-slate-900/60
      "
    >
      <div className="flex items-center gap-2">
        <CheckCircle2 size={20} className="text-emerald-500" />

        <h3 className="text-lg font-bold">Progress</h3>
      </div>

      <div className="mt-5">
        <div className="mb-2 flex justify-between">
          <span className="text-slate-600 dark:text-slate-300">Completed</span>

          <span className="font-semibold">{progressPercentage}%</span>
        </div>

        <div className="h-3 rounded-full bg-slate-200 dark:bg-slate-700">
          <div
            className="
              h-3
              rounded-full
              bg-gradient-to-r
              from-violet-500
              to-cyan-500
              transition-all
              duration-500
            "
            style={{
              width: `${progressPercentage}%`,
            }}
          />
        </div>

        <div className="mt-4 flex items-center justify-between text-sm">
          <span className="text-slate-500 dark:text-slate-400">
            Questions Answered
          </span>

          <span className="font-semibold text-slate-700 dark:text-slate-200">
            {currentQuestion} / {totalQuestions}
          </span>
        </div>

        <div className="mt-4 rounded-2xl bg-slate-100 p-4 dark:bg-slate-800">
          <div className="text-xs uppercase tracking-wide text-slate-500">
            Interview Status
          </div>

          <div className="mt-1 font-semibold text-slate-800 dark:text-white">
            In Progress
          </div>
        </div>
      </div>
    </div>
  );
}