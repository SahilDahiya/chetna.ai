import os

import requests
from dotenv import load_dotenv

load_dotenv()
url = 'https://api.x.com/2/users/{id}/followers'

bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')

headers = {'Authorization': 'Bearer {}'.format(bearer_token)}

response = requests.request('GET', url, headers=headers)

print(response.text)
