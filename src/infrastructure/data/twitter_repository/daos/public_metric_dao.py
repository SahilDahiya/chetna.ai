from typing_extensions import TypedDict

from src.domain.models.twitter.tweet import PublicMetrics


class PublicMetricsDAO(TypedDict):
    retweet_count: int
    reply_count: int
    like_count: int
    quote_count: int
    impression_count: int
    bookmark_count: int


def public_metrics_dao_to_public_metrics(public_metric_dao: PublicMetricsDAO) -> PublicMetrics:
    return PublicMetrics(
        retweet_count=public_metric_dao['retweet_count'],
        reply_count=public_metric_dao['reply_count'],
        like_count=public_metric_dao['like_count'],
        quote_count=public_metric_dao['quote_count'],
        impression_count=public_metric_dao['impression_count'],
        bookmark_count=public_metric_dao['bookmark_count'],
    )


def public_metrics_to_public_metrics_dao(public_metrics: PublicMetrics) -> PublicMetricsDAO:
    return PublicMetricsDAO(
        retweet_count=public_metrics.retweet_count,
        reply_count=public_metrics.reply_count,
        like_count=public_metrics.like_count,
        quote_count=public_metrics.quote_count,
        impression_count=public_metrics.impression_count,
        bookmark_count=public_metrics.bookmark_count,
    )
