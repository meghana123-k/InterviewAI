// path: frontend/src/components/interview/Timer.jsx

import { useEffect, useState } from "react";
import { Clock3 } from "lucide-react";

export default function Timer({ duration = 15, onTimeUp }) {
  const [timeLeft, setTimeLeft] = useState(duration * 60);

  useEffect(() => {
    setTimeLeft(duration * 60);
  }, [duration]);

  useEffect(() => {
    if (timeLeft <= 0) {
      if (onTimeUp) {
        onTimeUp();
      }
      return;
    }

    const timer = setInterval(() => {
      setTimeLeft((prev) => prev - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [timeLeft, onTimeUp]);

  const minutes = Math.floor(timeLeft / 60);
  const seconds = timeLeft % 60;

  const isWarning = timeLeft <= 300; // last 5 mins

  return (
    <div
      className="
        flex
        items-center
        gap-3
        rounded-2xl
        bg-white/70
        px-5
        py-3
        shadow-lg
        backdrop-blur-xl
        dark:bg-slate-900/60
      "
    >
      <Clock3
        size={18}
        className={isWarning ? "text-red-500" : "text-violet-500"}
      />

      <span className={`font-semibold ${isWarning ? "text-red-500" : ""}`}>
        {String(minutes).padStart(2, "0")}:{String(seconds).padStart(2, "0")}
      </span>
    </div>
  );
}