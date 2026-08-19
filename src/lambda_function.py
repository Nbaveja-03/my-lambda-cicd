import json


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from Lambda! Deployed via GitHub Actions CI/CD.",
            "version": "1.0.0"
        })
    }
