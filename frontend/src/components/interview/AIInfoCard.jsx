import { Sparkles } from "lucide-react";

export default function AIInfoCard() {
  return (
    <div className="rounded-3xl bg-white/70 p-6 shadow-xl backdrop-blur-xl dark:bg-slate-900/60">
      <div className="flex items-center gap-2">
        <Sparkles size={20} className="text-violet-500" />
        <h3 className="font-bold">AI Interviewer</h3>
      </div>

      <p className="mt-3 text-sm text-slate-500">
        Questions are generated dynamically based on your role, experience, and
        selected skills.
      </p>
    </div>
  );
}
