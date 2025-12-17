import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")


def update_status(table_name, doc_id, status, text_key=None):
    table = dynamodb.Table(table_name)
    table.update_item(
        Key={"docId": doc_id},
        UpdateExpression="SET #s = :s, textKey = :t",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={":s": status, ":t": text_key},
    )


def save_chunks(table_name, doc_id, chunk_list):
    table = dynamodb.Table(table_name)
    for idx, item in enumerate(chunk_list):
        table.put_item(
            Item={
                "docId": f"{doc_id}#chunk{idx}",
                "parent": doc_id,
                "chunk": item["chunk"],
                "vector": item["vector"],
            }
        )


def fetch_chunks(table_name, doc_id):
    table = dynamodb.Table(table_name)
    response = table.scan(
        FilterExpression=Key("parent").eq(doc_id)
    )
    return response.get("Items", [])


def update_summary(table_name, doc_id, summary):
    table = dynamodb.Table(table_name)
    table.update_item(
        Key={"docId": doc_id},
        UpdateExpression="SET summary = :s, status = :ok",
        ExpressionAttributeValues={":s": summary, ":ok": "COMPLETED"},
    )