import { MessageSquare } from "lucide-react";

export default function FeedbackCard() {
  return (
    <div className="rounded-3xl bg-white/70 p-6 shadow-xl backdrop-blur-xl dark:bg-slate-900/60">
      <div className="flex items-center gap-2">
        <MessageSquare size={20} className="text-cyan-500" />
        <h3 className="font-bold">AI Feedback</h3>
      </div>

      <p className="mt-3 text-sm text-slate-500">
        Feedback and evaluation will appear after interview completion.
      </p>
    </div>
  );
}
