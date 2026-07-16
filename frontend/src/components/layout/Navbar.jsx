import { LogOut, Moon, Sun, User } from "lucide-react";
import { useNavigate } from "react-router-dom";

import { useAuth } from "../../contexts/AuthContext";
import { useTheme } from "../../contexts/ThemeContext";

function Navbar() {
  const navigate = useNavigate();

  const { user, logout } = useAuth();

  const { darkMode, toggleTheme } = useTheme();

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  return (
    <header
      className="
        sticky
        top-0
        z-50
        border-b
        border-white/10
        bg-white/70
        backdrop-blur-xl
        dark:bg-slate-950/70
      "
    >
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6">
        <div>
          <h1
            className="
              text-3xl
              font-black
              bg-gradient-to-r
              from-violet-500
              to-cyan-500
              bg-clip-text
              text-transparent
            "
          >
            InterviewAI
          </h1>
        </div>

        <div className="flex items-center gap-4">
          <button
            onClick={toggleTheme}
            className="
              rounded-xl
              p-3
              transition
              hover:bg-slate-200
              dark:hover:bg-slate-800
            "
          >
            {darkMode ? <Sun size={20} /> : <Moon size={20} />}
          </button>

          <div
            className="
              flex
              items-center
              gap-3
              rounded-xl
              bg-white/60
              px-4
              py-2
              backdrop-blur-md
              dark:bg-slate-800/60
            "
          >
            <User size={18} />

            <span className="font-medium">{user?.username}</span>
          </div>

          <button
            onClick={handleLogout}
            className="
              rounded-xl
              p-3
              text-red-500
              transition
              hover:bg-red-100
              dark:hover:bg-red-900/30
            "
          >
            <LogOut size={20} />
          </button>
        </div>
      </div>
    </header>
  );
}

export default Navbar;
