// path: frontend/src/components/interview/AnswerBox.jsx

export default function AnswerBox({ answer, setAnswer, submitting, onSubmit }) {
  return (
    <div
      className="
        mt-6
        rounded-3xl
        bg-white/70
        p-6
        shadow-xl
        backdrop-blur-xl
        dark:bg-slate-900/60
      "
    >
      <div className="flex items-center justify-between">
        <h3 className="text-lg font-bold">Your Answer</h3>

        <span className="text-sm text-slate-500">
          {answer.length} characters
        </span>
      </div>

      <textarea
        rows={10}
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        placeholder="Write your answer here..."
        className="
          mt-4
          w-full
          rounded-2xl
          border
          border-slate-300
          bg-white
          p-5
          outline-none
          transition
          focus:border-violet-500
          dark:border-slate-700
          dark:bg-slate-800
          dark:text-white
        "
      />

      <div className="mt-6 flex justify-end">
        <button
          onClick={onSubmit}
          disabled={submitting || !answer.trim()}
          className="
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
            disabled:cursor-not-allowed
            disabled:opacity-60
          "
        >
          {submitting ? "Submitting..." : "Submit Answer"}
        </button>
      </div>
    </div>
  );
}