from aws_cdk import Stack, aws_lambda as _lambda, aws_dynamodb as dynamodb, aws_apigateway as apigateway
from constructs import Construct

class DecisionUniversityLambdasStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Reference the existing DynamoDB Table
        university_table_name = "university"  # Replace with your actual table name
        table = dynamodb.Table.from_table_name(self, "university", university_table_name)

        #Create Lambda to get universities from DynamoDB
        get_university_function= _lambda.Function(
            self, 'GetUniversitiesFunction',
            runtime=_lambda.Runtime.PYTHON_3_9,  # Python runtime
            handler='get_universities.lambda_handler',  # Adjusted handler for the new file name
            code=_lambda.Code.from_asset('lambdas/get_universities'),  # Path to 'university_services' directory
        )
        table.grant_read_data(get_university_function)

        
        # Define Lambda function
        get_university_by_id_function= _lambda.Function(
            self, 'GetUniversityByIdFunction',
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler='get_university_by_id.lambda_handler',
            code=_lambda.Code.from_asset('lambdas/get_university_by_id'),
        )
        table.grant_read_data(get_university_by_id_function)

        # Create Lambda function to create a university
        create_university_function = _lambda.Function(
            self, 'CreateUniversityFunction',
            runtime=_lambda.Runtime.PYTHON_3_9,  # Python runtime
            handler='create_university.lambda_handler',  # File name and function name
            code=_lambda.Code.from_asset('lambdas/create_university'),  # Path to the folder where your Lambda function resides
        )
        table.grant_write_data(create_university_function)

        # Create Lambda function to update a university
        update_university_function = _lambda.Function(
            self, 'UpdateUniversityFunction',
            runtime=_lambda.Runtime.PYTHON_3_9,  # Python runtime
            handler='update_university.lambda_handler',  # File name and function name
            code=_lambda.Code.from_asset('lambdas/update_university'),  # Path to the folder where your Lambda function resides
        )
        table.grant_read_write_data(update_university_function)

        # Create Lambda function to delete a university
        delete_university_function = _lambda.Function(
            self, 'DeleteUniversityFunction',
            runtime=_lambda.Runtime.PYTHON_3_9,  # Python runtime
            handler='delete_university.lambda_handler',  # File name and function name
            code=_lambda.Code.from_asset('lambdas/delete_university'),  # Path to the folder where your Lambda function resides
        )
        # Grant the Lambda function permission to delete items from DynamoDB
        table.grant_read_write_data(delete_university_function)

        # Create API Gateway
        api = apigateway.RestApi(self, "UniversityAPI",
                                 rest_api_name="Decision University API",
                                 description="API for decision university.",
                                 endpoint_types=[apigateway.EndpointType.REGIONAL])

        # Create a /get_universities resource
        universities = api.root.add_resource('universities')
        universities.add_method("GET", apigateway.LambdaIntegration(get_university_function))
        universities.add_method("POST", apigateway.LambdaIntegration(create_university_function))
        # Create a /universities/{id} resource for the 'GetUniversityById' Lambda
        university_by_id = universities.add_resource("{id}")
        university_by_id.add_method("GET", apigateway.LambdaIntegration(get_university_by_id_function))
        university_by_id.add_method("PUT", apigateway.LambdaIntegration(update_university_function))
        university_by_id.add_method("DELETE", apigateway.LambdaIntegration(delete_university_function)) 

