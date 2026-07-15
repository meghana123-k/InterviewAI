import { LogOut } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../contexts/AuthContext";

function Navbar() {
  const navigate = useNavigate();

  const { user, logout } = useAuth();

  const handleLogout = () => {
    logout();

    navigate("/login");
  };

  return (
    <header className="border-b bg-white">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-8">
        <h1 className="text-2xl font-bold text-blue-600">InterviewAI</h1>

        <div className="flex items-center gap-6">
          <span className="font-medium">{user?.username}</span>

          <button
            onClick={handleLogout}
            className="rounded-lg p-2 hover:bg-slate-100"
          >
            <LogOut size={20} />
          </button>
        </div>
      </div>
    </header>
  );
}

export default Navbar;
