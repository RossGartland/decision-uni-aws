import boto3
import json
import os
from boto3.dynamodb.conditions import Key
from decimal import Decimal

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('university') 

def lambda_handler(event, context):
    # Scan DynamoDB table without sorting
    try:
        response = table.scan()
        items = response['Items']
        
        # Convert Decimal to standard Python types
        items = json.loads(json.dumps(items, default=str))
        
        return {
            'statusCode': 200,
            'headers': {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
            'body': json.dumps(items)
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }