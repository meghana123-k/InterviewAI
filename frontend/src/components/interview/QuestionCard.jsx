// path: frontend/src/components/interview/QuestionCard.jsx

import { Brain } from "lucide-react";

export default function QuestionCard({ question, progress }) {
  if (!question) return null;

  return (
    <div
      className="
        rounded-3xl
        bg-white/70
        p-8
        shadow-xl
        backdrop-blur-xl
        dark:bg-slate-900/60
      "
    >
      <div className="flex items-center gap-3">
        <Brain size={28} className="text-violet-500" />

        <h2 className="text-xl font-bold">Current Question</h2>
      </div>

      <div className="mt-8">
        {/* Badges */}

        <div className="flex flex-wrap gap-3">
          <span
            className="
              rounded-full
              bg-violet-100
              px-4
              py-2
              text-sm
              font-medium
              text-violet-700
            "
          >
            Question {progress?.current_question || 1}
            {" of "}
            {progress?.total_questions || 0}
          </span>

          {question.skill && (
            <span
              className="
                rounded-full
                bg-cyan-100
                px-4
                py-2
                text-sm
                font-medium
                text-cyan-700
              "
            >
              {question.skill}
            </span>
          )}

          {question.difficulty && (
            <span
              className={`
                rounded-full
                px-4
                py-2
                text-sm
                font-medium
                ${
                  question.difficulty === "EASY"
                    ? "bg-emerald-100 text-emerald-700"
                    : question.difficulty === "MEDIUM"
                      ? "bg-amber-100 text-amber-700"
                      : "bg-rose-100 text-rose-700"
                }
              `}
            >
              {question.difficulty}
            </span>
          )}
        </div>

        {/* Question */}

        <h3
          className="
            mt-6
            text-2xl
            font-bold
            leading-relaxed
            text-slate-800
            dark:text-white
          "
        >
          {question.question}
        </h3>
      </div>
    </div>
  );
}