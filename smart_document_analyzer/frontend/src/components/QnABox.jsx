import React, { useState } from "react";
import { askQuestion } from "../api";

export default function QnABox({ docId }) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const submit = async () => {
    const resp = await askQuestion({ question, doc_id: docId });
    setAnswer(resp.answer);
  };

  return (
    <div style={styles.box}>
      <h2>Ask Questions About the Document</h2>

      <textarea
        placeholder="Type your question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        style={styles.text}
      />

      <button onClick={submit}>Ask</button>

      {answer && (
        <div style={styles.answerBox}>
          <h3>Answer:</h3>
          <p style={{ whiteSpace: "pre-line" }}>{answer}</p>
        </div>
      )}
    </div>
  );
}

const styles = {
  box: {
    border: "1px solid #ddd",
    padding: 20,
    marginTop: 20,
    borderRadius: 8
  },
  text: {
    width: "100%",
    height: 80,
    marginBottom: 10
  },
  answerBox: {
    background: "#f5f5f5",
    padding: 10,
    marginTop: 10,
    borderRadius: 6
  }
};