from dependency_injector.wiring import Provide, inject

from src.domain.interfaces import AbstractCollectTweetToReply
from src.infrastructure.containers import Container


@inject
def send_out_tweets(
    collect_tweet_to_reply_service: AbstractCollectTweetToReply = Provide[Container.collect_tweet_to_reply_service],
):
    tweet_reply_to = collect_tweet_to_reply_service.collect_mentions()
    
    return tweet_reply_to
    # 1.  get tweet content
    # 2.  prepare tweet reply
    # 2a. select passage
    # 2b. generate reply text
    # 3.  reply to tweet

