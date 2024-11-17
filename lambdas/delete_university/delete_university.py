import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('university') 

def lambda_handler(event, context):
    try:
        # Extract the university ID from the path parameter
        university_id = event['pathParameters']['id']  # Assuming the API Gateway passes the ID in the URL
        
        # Attempt to delete the university record from DynamoDB
        response = table.delete_item(
            Key={'id': university_id}
        )

        # Check if the item was deleted
        if response.get('Attributes') is None:
            return {
                'statusCode': 404,
                'headers': {
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                'body': json.dumps({"error": "The requested resource was not found."})
            }
        
        # Successful deletion
        return {
            'statusCode': 204,
            'headers': {
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
            'body': json.dumps({})
        }

    except Exception as e:
        # Handle other errors
        return {
            'statusCode': 500,
            'headers': {
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
            'body': json.dumps({"error": str(e)})
        }