import requests
import sys

apiKey = sys.argv[1]
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
    'subject': 'Hello world From Python',
    'htmlContent': '<html><head></head><body><p>Hello,</p>This is my first transactional email sent from Brevo.</p></body></html>',
}

response = requests.post('https://api.brevo.com/v3/smtp/email', headers=headers, data=json_data)
print(response.raw)