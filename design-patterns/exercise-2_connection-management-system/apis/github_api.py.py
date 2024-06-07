import requests
from config import API_CONFIG

class GitHubAPI:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {
            'Authorization': f"token {API_CONFIG['github']['access_token']}"
        }

    def perform_basic_operations(self):
        response = requests.get(f"{self.base_url}/user", headers=self.headers)
        if response.status_code == 200:
            print("GitHub API connection successful.")
            print(response.json())
        else:
            print("Failed to connect to GitHub API.")
