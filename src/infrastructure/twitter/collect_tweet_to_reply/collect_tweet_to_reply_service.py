import requests

from src.domain.interfaces import AbstractCollectTweetToReply
from src.domain.models.configuration import Configuration
from src.domain.models.twitter.tweet_to_reply.tweet_to_reply import TweetToReply


class CollectTweetToReplyService(AbstractCollectTweetToReply):
    def __init__(self, configuration: Configuration):
        self.__configuration = configuration

    def collect_mentions(self) -> list[TweetToReply]:
        user_id = self.__configuration.twitter_main_user

        search_url = 'https://api.twitter.com/2/users/{}/mentions'.format(user_id)

        params = {
            'tweet.fields': 'author_id,conversation_id,created_at,public_metrics,text',
        }

        def bearer_oauth(r):
            r.headers['Authorization'] = f'Bearer {self.__configuration.twitter_bearer_token}'
            r.headers['User-Agent'] = 'v2RecentSearchPython'
            return r

        response = requests.get(search_url, auth=bearer_oauth, params=params)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        tweet_data = response.json()['data']


        return [TweetToReply(
            user_id=tweet['author_id'],
            conversation_id=tweet['conversation_id'],
            last_tweet_id=tweet['id'],
        ) for tweet in tweet_data]
