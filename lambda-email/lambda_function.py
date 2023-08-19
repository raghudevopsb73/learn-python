import json
import requests
import os

def lambda_handler(event, context):
    apiKey = os.environ.get('api_token')
    headers = {
        'accept': 'application/json',
        'api-key': apiKey,
        'content-type': 'application/json',
    }

    json_data = {
        'sender': {
            'name': 'Raghu',
            'email': 'raghuk.vit@gmail.com',
        },
        'to': [
            {
                'email': 'raghudevopsb72@gmail.com',
                'name': 'Raghu',
            },
        ],
        'subject': 'Hello world From Python -  1',
        'htmlContent': '<html><head></head><body><p>Hello,</p>This is my first transactional email sent from Brevo.</p></body></html>',
    }

    response = requests.post('https://api.brevo.com/v3/smtp/email', headers=headers, json=json_data)
    return {
        'statusCode': json.dumps(response.status_code)
    }

