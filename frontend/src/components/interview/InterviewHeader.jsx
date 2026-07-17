import { Clock3 } from "lucide-react";

export default function InterviewHeader({ status = "Interview Active" }) {
  return (
    <div className="mb-8 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
      <div>
        <h1 className="text-4xl font-black text-slate-800 dark:text-white">
          AI Interview Session
        </h1>

        <p className="mt-2 text-slate-500 dark:text-slate-400">
          Answer each question thoughtfully and confidently.
        </p>
      </div>

      <div className="flex items-center gap-3 rounded-2xl bg-white/70 px-5 py-3 shadow-lg backdrop-blur-xl dark:bg-slate-900/60">
        <Clock3 size={18} />
        <span className="font-semibold">{status}</span>
      </div>
    </div>
  );
}
