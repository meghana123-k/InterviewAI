import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import Card from "../../components/ui/Card";
import Input from "../../components/ui/Input";
import Button from "../../components/ui/Button";
import ThemeToggle from "../../components/ui/ThemeToggle";

import { useAuth } from "../../contexts/AuthContext";

function Login() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setForm((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      setLoading(true);

      await login(form);

      navigate("/dashboard");
    } catch {
      setError("Invalid username or password");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="
        relative
        flex
        min-h-screen
        items-center
        justify-center
        overflow-hidden
        bg-gradient-to-br
        from-indigo-200
        via-violet-100
        to-cyan-100
        dark:from-slate-950
        dark:via-slate-900
        dark:to-indigo-950
      "
    >
      <ThemeToggle />

      <div className="absolute left-10 top-20 h-72 w-72 rounded-full bg-violet-500/30 blur-3xl"></div>

      <div className="absolute right-10 bottom-20 h-72 w-72 rounded-full bg-cyan-500/30 blur-3xl"></div>

      <Card className="w-full max-w-md">
        <div className="mb-8 text-center">
          <h1
            className="
              text-5xl
              font-black
              bg-gradient-to-r
              from-violet-600
              to-cyan-500
              bg-clip-text
              text-transparent
            "
          >
            InterviewAI
          </h1>

          <p className="mt-3 text-slate-500 dark:text-slate-400">
            Practice. Improve. Get Hired.
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-5">
          <Input
            label="Username"
            name="username"
            value={form.username}
            onChange={handleChange}
          />

          <Input
            label="Password"
            name="password"
            type="password"
            value={form.password}
            onChange={handleChange}
          />

          {error && <p className="text-sm text-red-500">{error}</p>}

          <Button type="submit" disabled={loading}>
            {loading ? "Signing In..." : "Login"}
          </Button>
        </form>

        <p className="mt-6 text-center text-sm text-slate-600 dark:text-slate-400">
          Don't have an account?
          <Link
            to="/signup"
            className="
              ml-2
              font-semibold
              text-violet-600
            "
          >
            Sign Up
          </Link>
        </p>
      </Card>
    </div>
  );
}

export default Login;
