import { createRoot } from "react-dom/client";

function App() {
  return (
    <main>
      <h1>BugAI</h1>
      <p>Development foundation</p>
      <p>Website discovery, AI generation, and test execution are planned.</p>
    </main>
  );
}

createRoot(document.getElementById("root")!).render(<App />);
