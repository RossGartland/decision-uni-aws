import boto3
import json
from decimal import Decimal
import uuid

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('university') 

def lambda_handler(event, context):
    try:
        # Get data from the event (usually from API Gateway)
        data = json.loads(event['body'])
        university_id = str(uuid.uuid4())
        # Convert float fields to Decimal
        university_data = {
            'id': university_id,  
            'r2022': Decimal(str(data['r2022'])),  # Convert to string first to avoid precision issues
            'r2021': Decimal(str(data['r2021'])),
            'score': Decimal(str(data['score'])),
            'course': Decimal(str(data['course'])),
            'teaching': Decimal(str(data['teaching'])),
            'feedback': Decimal(str(data['feedback'])),
            'ratio': Decimal(str(data['ratio'])),
            'spend': Decimal(str(data['spend'])),
            'tariff': Decimal(str(data['tariff'])),
            'career': Decimal(str(data['career'])),
            'continuation': Decimal(str(data['continuation'])),
            'institution': data['institution'],
            'comments': data.get('comments', []),  
            'crtdTimestamp': data.get('crtdTimestamp', None)  # Set the timestamp if passed
        }

        # Insert the data into DynamoDB
        table.put_item(Item=university_data)

        return {
            'statusCode': 201,
            'headers': {
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
            'body': json.dumps({
                'message': 'University created successfully!',
                'id': university_id  
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
            'body': json.dumps({
                "error": str(e)
            })
        }