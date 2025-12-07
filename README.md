# Smart Document Analyzer 📄🤖  
An AI-powered document-processing system built using **Amazon Textract**, **AWS Lambda**, **Amazon Bedrock/SageMaker**, and a serverless cloud-native architecture.  
This application extracts text from PDFs/images, generates intelligent summaries, and enables question-answering using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

### 🔍 Intelligent OCR
- Upload PDFs or images  
- Extracts structured text using **Amazon Textract**  
- Supports multi-page documents  

### 🧠 AI Summaries
- Automated text summarization  
- TL;DR bullet generation  
- Powered by **Amazon Bedrock** or **SageMaker JumpStart models**

### ❓ Ask-Anything Q&A
- Ask natural-language questions about the uploaded document  
- Uses RAG (chunking + embeddings + context retrieval)  
- Generates accurate responses using LLMs  

### ☁️ Serverless Architecture
- No servers to manage  
- Highly scalable  
- Low-cost for student projects  

---

## 🏗️ Architecture

```
                 ┌──────────────────────────┐
                 │        Frontend          │
                 │  (React + Amplify)       │
                 └────────────┬─────────────┘
                              │
                              ▼
                      ┌────────────┐
                      │ API Gateway│
                      └──────┬─────┘
                             │
               ┌─────────────┼───────────────────┐
               │             │                   │
               ▼             ▼                   ▼
      ┌────────────────┐  ┌────────────────┐  ┌────────────────┐
      │ Upload Handler │  │ OCR Lambda     │  │ Q/A Lambda     │
      └───────┬────────┘  └───────┬────────┘  └───────┬────────┘
              │                   │                   │
              ▼                   ▼                   ▼
        ┌───────────┐     ┌──────────────┐     ┌──────────────┐
        │ S3 Upload │     │ Textract OCR │     │ LLM Summary   │
        └─────┬─────┘     └─────┬────────┘     └─────┬────────┘
              │                   │                   │
              ▼                   ▼                   ▼
        ┌──────────────┐   ┌──────────────┐   ┌────────────────┐
        │ Raw Text S3  │   │ DynamoDB Meta│   │ Bedrock/SageMaker│
        └──────────────┘   └──────────────┘   └────────────────┘
```

---

## 📁 Project Structure

```
smart-document-analyzer/
│
├── backend/
│   ├── textract-handler.py         # OCR + text extraction Lambda
│   ├── nlp-processor.py            # Summarization + embeddings
│   ├── query-handler.py            # Q/A Lambda function
│   └── utils/                      # Helper scripts
│
├── frontend/
│   ├── src/                        # React frontend
│   ├── public/
│   └── package.json
│
├── infrastructure/
│   ├── cdk/ or cloudformation/     # Infra as code
│   └── iam-policies/
│
├── docs/
│   ├── architecture.png
│   ├── demo-screenshots/
│   └── samples/
│
├── README.md
└── LICENSE
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```sh
git clone https://github.com/<your-username>/smart-document-analyzer.git
cd smart-document-analyzer
```

### 2️⃣ Install Backend Dependencies
```sh
pip install -r backend/requirements.txt
```

### 3️⃣ Configure AWS Credentials
```sh
aws configure
```

Make sure your IAM user has permissions for:
- S3  
- Lambda  
- Textract  
- DynamoDB  
- Bedrock / SageMaker  
- API Gateway  

### 4️⃣ Deploy Backend Infrastructure
Using AWS CDK:
```sh
cd infrastructure/cdk
cdk deploy
```

### 5️⃣ Start Frontend
```sh
cd frontend
npm install
npm start
```

---

## 🧪 How the System Works

### **1. Upload Document**
User uploads a PDF/image → sent to S3 via pre-signed URL.

### **2. OCR Trigger**
S3 event triggers a Lambda function:
- Calls **Amazon Textract**
- Extracts text  
- Saves cleaned text to S3

### **3. NLP Processing**
A second Lambda:
- Chunks text  
- Generates embeddings  
- Creates summary using LLM  
- Saves metadata to DynamoDB  

### **4. Q&A Pipeline**
User provides a question:
- System retrieves relevant text chunks (RAG)  
- LLM generates the best answer  

---

## 🧩 API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/upload` | Generates pre-signed S3 upload URL |
| GET | `/status/{docId}` | Returns processing status + summary |
| POST | `/ask/{docId}` | Answers questions about the document |

---

## 💰 AWS Cost Optimization

To stay within student credits ($199.78):

- Use Textract on small PDFs (≤ 5 pages)
- Delete SageMaker endpoints when not in use
- Prefer **Bedrock** for serverless LLM inference
- Enable S3 lifecycle rules to auto-delete temporary files
- Enable Billing alerts

---

## 📸 Screenshots (Add After Deployment)

Place images under `docs/demo-screenshots/` and include examples here:

```
![Upload Page](docs/demo-screenshots/upload.png)
![Summary Example](docs/demo-screenshots/summary.png)
![Q&A Interface](docs/demo-screenshots/qa.png)
```

---

## 🧰 Tech Stack

### **Frontend**
- React  
- AWS Amplify  

### **Backend**
- AWS Lambda  
- Amazon API Gateway  
- Amazon S3  
- Amazon DynamoDB  
- Amazon Textract  

### **AI**
- Amazon Bedrock  
or  
- AWS SageMaker JumpStart  

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open a PR or fork the project.

---

## 📄 License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for full details.

---

## 👤 Author

**SriSaiKiran Tambalkar**  
B.Tech CSE (AIML) Student  
GitHub: [https://github.com/](https://github.com/Saiiii0906)<Saiiii0906>  
LinkedIn: [https://www.linkedin.com/in](https://www.linkedin.com/in/srisaikiran-tambalkar-479773298?utm_source=share_via&utm_content=profile&utm_medium=member_android)<SriSaiKiran Tambalkar>  
