import json
import boto3
import os
from utils.s3_utils import upload_text_to_s3
from utils.dynamo_utils import update_status

s3 = boto3.client("s3")
textract = boto3.client("textract")

UPLOAD_BUCKET = os.environ.get("UPLOAD_BUCKET")
TEXT_BUCKET = os.environ.get("TEXT_BUCKET")
TABLE_NAME = os.environ.get("TABLE_NAME")


def lambda_handler(event, context):
    record = event["Records"][0]
    bucket = record["s3"]["bucket"]["name"]
    key = record["s3"]["object"]["key"]

    print(f"Processing file: s3://{bucket}/{key}")

    # Call Textract
    response = textract.detect_document_text(
        Document={"S3Object": {"Bucket": bucket, "Name": key}}
    )

    # Extract text lines
    lines = []
    for block in response.get("Blocks", []):
        if block["BlockType"] == "LINE":
            lines.append(block["Text"])

    extracted_text = "\n".join(lines)

    # Save extracted text
    text_key = key + ".txt"
    upload_text_to_s3(TEXT_BUCKET, text_key, extracted_text)

    # Update DynamoDB status
    update_status(TABLE_NAME, key, "TEXT_EXTRACTED", text_key)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Text extracted", "text_key": text_key}),
    }