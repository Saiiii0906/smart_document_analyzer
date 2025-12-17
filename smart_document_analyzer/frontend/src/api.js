import { API } from "aws-amplify";

// Upload file: gets pre-signed URL
export const requestUploadURL = async () => {
  return API.post("SmartDocAPI", "/upload", {});
};

// NLP processing request
export const callNLPProcessor = async (payload) => {
  return API.post("SmartDocAPI", "/process", { body: payload });
};

// Poll document status
export const fetchStatus = async (docId) => {
  return API.get("SmartDocAPI", `/status/${docId}`);
};

// Ask a question
export const askQuestion = async (payload) => {
  return API.post("SmartDocAPI", "/ask", { body: payload });
};
