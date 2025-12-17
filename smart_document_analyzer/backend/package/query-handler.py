import json
import boto3
import os
from utils.dynamo_utils import fetch_chunks
from utils.text_utils import cosine_similarity
from utils.bedrock_utils import generate_answer

TABLE_NAME = os.environ.get("TABLE_NAME")
ANSWER_MODEL = os.environ.get("ANSWER_MODEL")


def lambda_handler(event, context):
    body = json.loads(event["body"])
    question = body["question"]
    doc_id = body["doc_id"]

    # Load chunks from DynamoDB
    chunks = fetch_chunks(TABLE_NAME, doc_id)

    # Rank chunks by similarity
    ranking = []
    for item in chunks:
        similarity = cosine_similarity(question, item["vector"])
        ranking.append((similarity, item["chunk"]))

    ranking.sort(reverse=True)
    top_chunks = [c[1] for c in ranking[:3]]

    context_text = "\n\n".join(top_chunks)

    # Ask LLM
    answer = generate_answer(question, context_text, ANSWER_MODEL)

    return {"statusCode": 200, "body": json.dumps({"answer": answer})}