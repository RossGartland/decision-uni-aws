import json
import boto3
import datetime
from decimal import Decimal
import os

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('university') 

def lambda_handler(event, context):
    try:
        # Extract the university ID from the path parameter
        university_id = event['pathParameters']['id']  # Assuming the API Gateway passes the ID in the URL

        # Extract the JSON body from the event
        body = json.loads(event['body'])

        # Create a dictionary for the updated university data
        updated_university = {
            'r2022': Decimal(str(body.get('r2022', 0))),  # Default to 0 if not provided, ensure Decimal type
            'r2021': Decimal(str(body.get('r2021', 0))),  # Default to 0 if not provided, ensure Decimal type
            'score': Decimal(str(body.get('score', 0))),  # Ensure Decimal type
            'course': Decimal(str(body.get('course', 0))),  # Ensure Decimal type
            'teaching': Decimal(str(body.get('teaching', 0))),  # Ensure Decimal type
            'feedback': Decimal(str(body.get('feedback', 0))),  # Ensure Decimal type
            'ratio': Decimal(str(body.get('ratio', 0))),  # Ensure Decimal type
            'spend': Decimal(str(body.get('spend', 0))),  # Ensure Decimal type
            'tariff': Decimal(str(body.get('tariff', 0))),  # Ensure Decimal type
            'career': Decimal(str(body.get('career', 0))),  # Ensure Decimal type
            'continuation': Decimal(str(body.get('continuation', 0))),  # Ensure Decimal type
            'institution': body.get('institution', ''),  # Default to empty string if not provided
            'uptdTimestamp': str(datetime.datetime.utcnow())  # Timestamp for update
        }

        # Check if the university exists in the table
        response = table.get_item(Key={'id': university_id})

        if 'Item' in response:
            # The university exists, update the record
            table.update_item(
                Key={'id': university_id},
                UpdateExpression="SET r2022 = :r2022, r2021 = :r2021, score = :score, course = :course, "
                                 "teaching = :teaching, feedback = :feedback, ratio = :ratio, "
                                 "spend = :spend, tariff = :tariff, career = :career, continuation = :continuation, "
                                 "institution = :institution, uptdTimestamp = :uptdTimestamp",
                ExpressionAttributeValues={
                    ':r2022': updated_university['r2022'],
                    ':r2021': updated_university['r2021'],
                    ':score': updated_university['score'],
                    ':course': updated_university['course'],
                    ':teaching': updated_university['teaching'],
                    ':feedback': updated_university['feedback'],
                    ':ratio': updated_university['ratio'],
                    ':spend': updated_university['spend'],
                    ':tariff': updated_university['tariff'],
                    ':career': updated_university['career'],
                    ':continuation': updated_university['continuation'],
                    ':institution': updated_university['institution'],
                    ':uptdTimestamp': updated_university['uptdTimestamp']
                },
                ReturnValues="UPDATED_NEW"  # Return the updated values (optional)
            )

            return {
                'statusCode': 200,
                'headers': {
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                'body': json.dumps({"message": "University updated successfully."})
            }
        else:
            # The university was not found
            return {
                'statusCode': 404,
                'headers': {
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
                'body': json.dumps({"error": "The requested resource was not found."})
            }

    except KeyError as e:
        # Handle missing fields in the request body
        return {
            'statusCode': 400,
            'headers': {
                    "Access-Control-Allow-Headers" : "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
                },
            'body': json.dumps({"error": f"Missing field: {str(e)}"})
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