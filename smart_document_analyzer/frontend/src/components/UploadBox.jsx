import React, { useState } from "react";
import { requestUploadURL, callNLPProcessor } from "../api";

export default function UploadBox({ onUploaded }) {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);

  const uploadFile = async () => {
    if (!file) return alert("Please select a file.");

    setUploading(true);

    const resp = await requestUploadURL();
    const { uploadURL, docId } = resp;

    await fetch(uploadURL, {
      method: "PUT",
      body: file
    });

    await callNLPProcessor({ text_key: `${docId}.txt`, doc_id: docId });

    setUploading(false);
    onUploaded(docId);
  };

  return (
    <div style={styles.box}>
      <h2>Upload Document</h2>
      <input
        type="file"
        accept="application/pdf,image/*"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button onClick={uploadFile} disabled={uploading}>
        {uploading ? "Uploading..." : "Upload"}
      </button>
    </div>
  );
}

const styles = {
  box: {
    border: "1px solid #ccc",
    padding: 20,
    borderRadius: 8,
    width: "50%",
    margin: "auto",
    textAlign: "center"
  }
};
