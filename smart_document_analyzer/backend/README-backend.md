# Backend — Smart Document Analyzer

This folder contains all AWS Lambda functions + utilities for:
- OCR extraction (Textract)
- NLP pipeline (Chunking, Embeddings, Summaries)
- RAG-based Q/A

## Functions
| File | Purpose |
|------|---------|
| textract-handler.py | Extract text from documents |
| nlp-processor.py | Generate embeddings + summaries |
| query-handler.py | Document Q/A pipeline |
| utils/ | Helper functions |

## Environment Variables
- UPLOAD_BUCKET  
- TEXT_BUCKET  
- TABLE_NAME  
- SUMMARY_MODEL  
- EMBEDDING_MODEL  
- ANSWER_MODEL  

