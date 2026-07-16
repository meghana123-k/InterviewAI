import { Brain, Clock3, Mic, MessageSquare } from "lucide-react";

function InterviewSession() {
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
        {/* Header */}

        <div className="mb-8 flex items-center justify-between">
          <div>
            <h1
              className="
                text-4xl
                font-black
                text-slate-800
                dark:text-white
              "
            >
              AI Interview Session
            </h1>

            <p className="mt-2 text-slate-500 dark:text-slate-400">
              Answer each question carefully.
            </p>
          </div>

          <div
            className="
              flex
              items-center
              gap-2
              rounded-2xl
              bg-white/70
              px-5
              py-3
              shadow-lg
              backdrop-blur-xl
              dark:bg-slate-900/60
            "
          >
            <Clock3 size={18} />

            <span className="font-semibold">15:00</span>
          </div>
        </div>

        {/* Main Layout */}

        <div className="grid gap-6 lg:grid-cols-3">
          {/* Question Panel */}

          <div className="lg:col-span-2">
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
                  Question 1 of 10
                </span>

                <h3 className="mt-6 text-2xl font-bold">
                  Explain the difference between REST and GraphQL APIs.
                </h3>
              </div>

              <div className="mt-8">
                <textarea
                  rows={8}
                  placeholder="Type your answer here..."
                  className="
                    w-full
                    rounded-2xl
                    border
                    border-slate-300
                    bg-white
                    p-4
                    outline-none
                    transition
                    focus:border-violet-500
                    dark:border-slate-700
                    dark:bg-slate-800
                  "
                />
              </div>

              <div className="mt-6 flex gap-4">
                <button
                  className="
                    rounded-xl
                    bg-gradient-to-r
                    from-violet-600
                    to-cyan-500
                    px-6
                    py-3
                    font-semibold
                    text-white
                  "
                >
                  Submit Answer
                </button>

                <button
                  className="
                    rounded-xl
                    border
                    border-slate-300
                    px-6
                    py-3
                    font-semibold
                  "
                >
                  Skip
                </button>
              </div>
            </div>
          </div>

          {/* Right Panel */}

          <div className="space-y-6">
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
              <h3 className="text-lg font-bold">Progress</h3>

              <div className="mt-5">
                <div className="mb-2 flex justify-between">
                  <span>Completed</span>
                  <span>10%</span>
                </div>

                <div className="h-3 rounded-full bg-slate-200">
                  <div
                    className="
                      h-3
                      w-[10%]
                      rounded-full
                      bg-gradient-to-r
                      from-violet-500
                      to-cyan-500
                    "
                  />
                </div>
              </div>
            </div>

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
                <Mic size={20} className="text-emerald-500" />

                <h3 className="font-bold">Voice Mode</h3>
              </div>

              <p className="mt-3 text-sm text-slate-500">
                Voice answering support can be enabled here.
              </p>
            </div>

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
                <MessageSquare size={20} className="text-cyan-500" />

                <h3 className="font-bold">AI Feedback</h3>
              </div>

              <p className="mt-3 text-sm text-slate-500">
                Feedback will appear after answering questions.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default InterviewSession;
