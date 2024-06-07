from apis.twitter_api import TwitterAPI
from apis.github_api import GitHubAPI

class ApiFactory:
    @staticmethod
    def get_api(api_name):
        if api_name == 'twitter':
            return TwitterAPI()
        elif api_name == 'github':
            return GitHubAPI()
        else:
            return None
