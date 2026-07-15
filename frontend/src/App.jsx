import Button from "./components/ui/Button";
import Card from "./components/ui/Card";
import Input from "./components/ui/Input";

function App() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-slate-100">
      <Card className="w-full max-w-md space-y-5">
        <h1 className="text-3xl font-bold text-blue-600">InterviewAI</h1>

        <Input label="Email" placeholder="Enter email" />

        <Input label="Password" type="password" placeholder="Enter password" />

        <Button>Login</Button>

        <Button variant="outline">Create Account</Button>
      </Card>
    </div>
  );
}

export default App;
