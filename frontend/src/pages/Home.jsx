import { useEffect, useState } from "react";
import api from "../services/api";

function Home() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    api
      .get("health/")
      .then((response) => {
        setMessage(response.data.message);
      })
      .catch(() => {
        setMessage("Backend not connected");
      });
  }, []);

  return (
    <div style={{ padding: "40px" }}>
      <h1>InterviewAI</h1>

      <h2>{message}</h2>
    </div>
  );
}

export default Home;
