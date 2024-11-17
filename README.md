# Decision University Platform - AWS Refactor

Decision University is a platform designed to assist prospective students in browsing and comparing universities using data from the Guardian University Rankings dataset. This application was initially created as a Python Flask API for a university project. The original version can be found on GitHub: decision-university-api.
Purpose of the Refactor

As part of my journey into AWS and serverless technologies, I decided to refactor the existing Python Flask API into a cloud-native architecture using AWS Lambda and other AWS tools. This transition not only modernizes the platform but also improves scalability, reliability, and cost efficiency.
Architecture Overview

The application leverages the following AWS services:

    AWS S3:
        Hosts the Angular front-end UI.
        Stores static assets such as images and website files.

    Angular UI:
        A responsive user interface that provides a seamless experience for browsing and comparing universities.
        Connects to the backend via AWS API Gateway.

    AWS API Gateway:
        Serves as the entry point for the API, routing requests to the appropriate AWS Lambda functions.

    AWS Lambda:
        Implements the backend logic in Python.
        Processes requests and interacts with the database.

    DynamoDB:
        A fast and reliable NoSQL database to store and manage university ranking data.




# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
