import React from "react";

export default function SummaryBox({ summary }) {
  if (!summary) return null;

  return (
    <div style={styles.box}>
      <h2>📄 Summary</h2>
      <p style={{ whiteSpace: "pre-line" }}>{summary}</p>
    </div>
  );
}

const styles = {
  box: {
    border: "1px solid #ddd",
    padding: 20,
    marginTop: 20,
    borderRadius: 8,
    background: "#fafafa"
  }
};
