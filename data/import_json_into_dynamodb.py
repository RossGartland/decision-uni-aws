import boto3
import json
from decimal import Decimal

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'university'
table = dynamodb.Table(table_name)

# Load JSON data and automatically convert floats to Decimal
with open('university.json', 'r') as json_file:
    items = json.load(json_file, parse_float=Decimal)  # This automatically converts floats to Decimal

# Flatten the 'id' field if it's in the MongoDB format
for item in items:
    if 'id' in item and '$oid' in item['id']:
        item['id'] = item['id']['$oid']  # Convert nested id to a simple string
        
    # Check if 'comments' exists and update the comment 'id' fields
    if 'comments' in item:
        for comment in item['comments']:
            if isinstance(comment, dict) and 'id' in comment and '$oid' in comment['id']:
                comment['id'] = comment['id']['$oid']  # Convert the comment 'id' to string

# Batch write items to DynamoDB
with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)
        print(f"Inserted item: {item}")
