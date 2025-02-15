from requests_oauthlib import OAuth1Session

from domain.interfaces import AbstractTweetPostService
from src.domain.interfaces import AbstractPassageToSvgService
from src.domain.models.configuration import Configuration
from src.domain.models.passages import Passage


class TweetPostService(AbstractTweetPostService):
    def __init__(
        self, configuration: Configuration, oauth: OAuth1Session, passage_to_svg_service: AbstractPassageToSvgService
    ):
        self.__configuration = configuration
        self.__oauth = oauth
        self.__passage_svg_service = passage_to_svg_service

    def post(self, text: str, reply_tweet_id: str, passage: Passage) -> dict:
        payload = {'text': text}

        # If image path is provided, upload it first
        media_id = self.upload_media(passage)
        payload['media'] = {'media_ids': [media_id]}

        # Post tweet
        response = self.__oauth.post(url='https://api.twitter.com/2/tweets', json=payload)

        if response.status_code != 201:
            raise Exception(f'Request returned an error: {response.status_code} {response.text}')

        return response.json()

    def upload_media(self, passage: Passage) -> str:
        print(f'Uploading image: {passage.passage_id}')

        # Get the image file
        files = {'media': self.__passage_svg_service.get_svg(passage)}
        upload_url = 'https://upload.twitter.com/1.1/media/upload.json'

        response = self.__oauth.post(url=upload_url, files=files)

        if response.status_code != 200:
            raise Exception(f'Upload failed: {response.status_code} {response.text}')

        media_id = response.json()['media_id']
        print(f'Upload successful! Media ID: {media_id}')
        return str(media_id)
