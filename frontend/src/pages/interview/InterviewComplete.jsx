import { Link } from "react-router-dom";
import { CheckCircle2, ArrowLeft, Trophy } from "lucide-react";

export default function InterviewComplete() {
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
        flex
        items-center
        justify-center
        px-6
      "
    >
      <div
        className="
          w-full
          max-w-2xl
          rounded-3xl
          bg-white/70
          p-10
          shadow-2xl
          backdrop-blur-xl
          dark:bg-slate-900/60
          text-center
        "
      >
        <div className="flex justify-center">
          <div
            className="
              flex
              h-24
              w-24
              items-center
              justify-center
              rounded-full
              bg-green-100
            "
          >
            <CheckCircle2 size={54} className="text-green-600" />
          </div>
        </div>

        <h1
          className="
            mt-8
            text-4xl
            font-black
            text-slate-800
            dark:text-white
          "
        >
          Interview Completed
        </h1>

        <p
          className="
            mt-4
            text-lg
            text-slate-600
            dark:text-slate-400
          "
        >
          Your interview has been submitted successfully.
        </p>

        <div
          className="
            mt-8
            rounded-2xl
            bg-gradient-to-r
            from-violet-500/10
            to-cyan-500/10
            p-6
          "
        >
          <div className="flex items-center justify-center gap-2">
            <Trophy size={20} className="text-amber-500" />

            <span className="font-semibold">Great Job!</span>
          </div>

          <p className="mt-2 text-sm text-slate-500">
            Your answers have been recorded. AI evaluation and detailed feedback
            will be available shortly.
          </p>
        </div>

        <div className="mt-10">
          <Link
            to="/dashboard"
            className="
              inline-flex
              items-center
              gap-2
              rounded-xl
              bg-gradient-to-r
              from-violet-600
              to-cyan-500
              px-8
              py-3
              font-semibold
              text-white
              shadow-lg
              transition
              hover:scale-[1.02]
            "
          >
            <ArrowLeft size={18} />
            Back to Dashboard
          </Link>
        </div>
      </div>
    </div>
  );
}
