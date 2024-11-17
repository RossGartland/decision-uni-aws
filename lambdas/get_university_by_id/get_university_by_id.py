import boto3
import json
import os
from boto3.dynamodb.conditions import Key
from decimal import Decimal

# Initialize DynamoDB client and table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('university') 

def lambda_handler(event, context):
    # Get the 'id' from the path parameters
    university_id = event.get('pathParameters', {}).get('id')
    
    if not university_id:
        return {
            'statusCode': 400,
            'body': json.dumps({"error": "University ID is required"})
        }
    
    try:
        # Query DynamoDB table by primary key 'id'
        response = table.get_item(Key={'id': university_id})
        university = response.get('Item')

        # If the university is found, format and return it
        if university:
            # Convert any Decimal types to standard JSON-compatible types
            university = json.loads(json.dumps(university, default=str))
            return {
                'statusCode': 200,
                'headers': {
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                'body': json.dumps(university)
            }
        
        else:
            # University not found
            return {
                'statusCode': 404,
                'headers': {
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                'body': json.dumps({"error": "The requested resource was not found."})
            }
    
    except Exception as e:
        # Handle errors (e.g., connection issues, permissions)
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }