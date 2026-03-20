import { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState("");
  const [isError, setIsError] = useState(false);
  const [errorType, setErrorType] = useState("");


  const handleSubmit = async () => {
    if (!input.trim()) {
      setResult("Please enter at least one dependency");
      setIsError(true);
      setErrorType("input");
      return;
    }
    const lines = input.trim().split("\n");

    const edges = lines.map(line => {
      const parts = line.trim().split(" ");
      return [parts[0], parts[1]];
    });

    const response = await fetch("https://dependency-resolver.onrender.com/resolve", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ edges })
    });

    const data = await response.json();

    if (data.status === "error") {
      setResult(data.cycle.join(" → "));
      setIsError(true);
      setErrorType("cycle");
    } else {
      setResult(data.order.join(" → "));
      setIsError(false);
      setErrorType("");
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1 style={styles.title}>Dependency Resolver</h1>
        <p style={{ color: "#666", marginBottom: "15px" }}>
          Resolve task dependencies using graph algorithms
        </p>
        <textarea
          style={styles.textarea}
          placeholder={`Enter dependencies (Task Dependency):
Frontend Backend
Backend Database`}
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button
          style={{ marginBottom: "10px" }}
          onClick={() =>
            setInput("Frontend Backend\nBackend Database")
          }
        >
          Try Example
        </button>

        <button style={styles.button} onClick={handleSubmit}>
          Resolve
        </button>
        {result && (
          <div
            style={{
              ...styles.result,
              backgroundColor: isError ? "#ffe6e6" : "#e6ffe6",
              color: isError ? "#cc0000" : "#006600",
              border: isError ? "2px solid red" : "2px solid green",
              padding: "12px",
              borderRadius: "8px",
              fontSize: "16px"
            }}
          >
            {isError && errorType === "cycle" && "❌ Cycle Detected: "}
            {isError && errorType === "input" && "⚠️ Error: "}
            {!isError && "✅ Valid Order: "}
            {result}
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  container: {
    height: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    background: "#f4f6f8"
  },
  card: {
    background: "#fff",
    padding: "30px",
    borderRadius: "10px",
    boxShadow: "0 4px 20px rgba(0,0,0,0.1)",
    textAlign: "center",
    width: "350px"
  },
  title: {
    marginBottom: "20px"
  },
  textarea: {
    width: "100%",
    height: "120px",
    padding: "10px",
    borderRadius: "5px",
    border: "1px solid #ccc",
    marginBottom: "15px",
    fontSize: "14px"
  },
  button: {
    width: "100%",
    padding: "12px",
    borderRadius: "8px",
    border: "none",
    background: "#4CAF50",
    color: "white",
    fontSize: "16px",
    cursor: "pointer",
    fontWeight: "bold"
  },
  result: {
    marginTop: "20px",
    fontWeight: "bold"
  }
};

export default App;