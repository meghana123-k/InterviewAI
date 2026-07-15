import Navbar from "../../components/layout/Navbar";
import { Link } from "react-router-dom";
import Button from "../../components/ui/Button";
function Dashboard() {
  return (
    <div className="min-h-screen bg-slate-100">
      <Navbar />

      <main className="mx-auto max-w-7xl p-8">
        <h1 className="mb-8 text-4xl font-bold">Dashboard</h1>

        <div className="grid gap-6 md:grid-cols-3">
          <div className="rounded-xl bg-white p-6 shadow-lg">
            <h2 className="text-lg font-semibold">Interviews</h2>

            <p className="mt-4 text-4xl font-bold text-blue-600">0</p>
          </div>
          <div className="rounded-xl bg-white p-6 shadow-lg">
            <h2 className="text-lg font-semibold">Average Score</h2>

            <p className="mt-4 text-4xl font-bold text-emerald-600">--</p>
          </div>
          <div className="rounded-xl bg-white p-6 shadow-lg">
            <h2 className="text-lg font-semibold">Resume</h2>

            <p className="mt-4 text-lg text-slate-500">Not Uploaded</p>
          </div>

          <Link to="/resume/upload">
            <Button>Upload Resume</Button>
          </Link>
        </div>
      </main>
    </div>
  );
}

export default Dashboard;
