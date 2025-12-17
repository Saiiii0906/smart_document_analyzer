import json
import boto3
import os
from utils.text_utils import chunk_text
from utils.bedrock_utils import generate_summary, embed_text
from utils.dynamo_utils import save_chunks, update_summary
from utils.s3_utils import read_s3_text

S3_BUCKET = os.environ.get("TEXT_BUCKET")
TABLE_NAME = os.environ.get("TABLE_NAME")
EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL")
SUMMARY_MODEL = os.environ.get("SUMMARY_MODEL")


def lambda_handler(event, context):
    body = json.loads(event["body"])
    text_key = body["text_key"]
    doc_id = body["doc_id"]

    # Load extracted text
    text = read_s3_text(S3_BUCKET, text_key)

    # Split into chunks
    chunks = chunk_text(text, max_chars=1500)

    # Generate embeddings
    embedded_chunks = []
    for chunk in chunks:
        vector = embed_text(chunk, EMBEDDING_MODEL)
        embedded_chunks.append({"chunk": chunk, "vector": vector})

    # Save chunk + embeddings to DynamoDB
    save_chunks(TABLE_NAME, doc_id, embedded_chunks)

    # Generate Summary
    summary = generate_summary(text, SUMMARY_MODEL)

    # Update metadata
    update_summary(TABLE_NAME, doc_id, summary)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "NLP processing completed", "summary": summary}),
    }