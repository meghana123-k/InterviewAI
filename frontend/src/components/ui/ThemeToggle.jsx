import { Moon, Sun } from "lucide-react";
import { useTheme } from "../../contexts/ThemeContext";

function ThemeToggle() {
  const { darkMode, toggleTheme } = useTheme();

  return (
    <button
      onClick={toggleTheme}
      className="
        fixed
        right-6
        top-6
        z-50
        rounded-full
        bg-white/20
        backdrop-blur-xl
        p-3
        text-white
        shadow-lg
        transition
        hover:scale-110
        dark:bg-slate-800/40
      "
    >
      {darkMode ? <Sun size={20} /> : <Moon size={20} />}
    </button>
  );
}

export default ThemeToggle;
