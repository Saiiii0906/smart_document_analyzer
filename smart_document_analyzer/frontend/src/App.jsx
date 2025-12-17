import React, { useState, useEffect } from "react";
import Amplify from "aws-amplify";
import awsExports from "../aws-exports";
import UploadBox from "./components/UploadBox";
import SummaryBox from "./components/SummaryBox";
import QnABox from "./components/QnABox";
import { fetchStatus } from "./api";

Amplify.configure(awsExports);

export default function App() {
  const [docId, setDocId] = useState(null);
  const [summary, setSummary] = useState("");

  // Poll summary every 3 seconds
  useEffect(() => {
    if (!docId) return;

    const poll = setInterval(async () => {
      const resp = await fetchStatus(docId);

      if (resp.summary) {
        setSummary(resp.summary);
        clearInterval(poll);
      }
    }, 3000);

    return () => clearInterval(poll);
  }, [docId]);

  return (
    <div style={styles.container}>
      <h1>Smart Document Analyzer</h1>

      <UploadBox onUploaded={(id) => setDocId(id)} />

      <SummaryBox summary={summary} />

      {summary && <QnABox docId={docId} />}
    </div>
  );
}

const styles = {
  container: {
    padding: 30,
    fontFamily: "Arial",
    maxWidth: 900,
    margin: "auto"
  }
};