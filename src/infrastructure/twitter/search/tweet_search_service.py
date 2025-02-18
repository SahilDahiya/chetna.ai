import requests

from src.domain.interfaces.abstract_tweet_search_service import AbstractTweetSearchService
from src.domain.models.configuration import Configuration


class TweetSearchService(AbstractTweetSearchService):
    def __init__(self, configuration: Configuration):
        self.__configuration = configuration

    def user_tweets(self, user_id: str):
        search_url = 'https://api.twitter.com/2/tweets/search/recent'
        query_params = {
            'query': f'lang:en from:{user_id} -has:media -is:retweet -is:reply -is:quote is:verified',
            'tweet.fields': 'author_id,created_at,public_metrics,text',
        }

        def bearer_oauth(r):
            r.headers['Authorization'] = f'Bearer {self.__configuration.twitter_bearer_token}'
            r.headers['User-Agent'] = 'v2RecentSearchPython'
            return r

        response = requests.get(search_url, auth=bearer_oauth, params=query_params)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()
