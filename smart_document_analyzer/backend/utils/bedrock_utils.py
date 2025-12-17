import boto3
import json

bedrock = boto3.client("bedrock-runtime")


def generate_summary(text, model_id):
    prompt = f"Summarize the following document in 150-200 words:\n\n{text}"
    response = bedrock.invoke_model(
        modelId=model_id,
        contentType="application/json",
        body=json.dumps({"input": prompt})
    )
    output = json.loads(response["body"].read().decode())
    return output.get("output_text", "No summary available.")


def generate_answer(question, context, model_id):
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    response = bedrock.invoke_model(
        modelId=model_id,
        contentType="application/json",
        body=json.dumps({"input": prompt})
    )
    output = json.loads(response["body"].read().decode())
    return output.get("output_text", "No answer available.")


def embed_text(text, model_id):
    response = bedrock.invoke_model(
        modelId=model_id,
        contentType="application/json",
        body=json.dumps({"input": text})
    )
    output = json.loads(response["body"].read().decode())
    return output.get("embedding", [])
