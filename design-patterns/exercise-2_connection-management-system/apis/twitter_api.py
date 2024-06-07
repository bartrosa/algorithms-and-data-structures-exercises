import requests
from requests_oauthlib import OAuth1
from config import API_CONFIG

class TwitterAPI:
    def __init__(self):
        self.auth = OAuth1(
            API_CONFIG['twitter']['api_key'],
            API_CONFIG['twitter']['api_secret_key'],
            API_CONFIG['twitter']['access_token'],
            API_CONFIG['twitter']['access_token_secret']
        )
        self.base_url = "https://api.twitter.com/1.1"

    def perform_basic_operations(self):
        response = requests.get(f"{self.base_url}/account/verify_credentials.json", auth=self.auth)
        if response.status_code == 200:
            print("Twitter API connection successful.")
            print(response.json())
        else:
            print("Failed to connect to Twitter API.")
