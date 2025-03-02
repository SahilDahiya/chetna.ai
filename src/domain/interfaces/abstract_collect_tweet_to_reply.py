from abc import ABC, abstractmethod


class AbstractCollectTweetToReply(ABC):
    @abstractmethod
    def collect_mentions(self):
        pass
