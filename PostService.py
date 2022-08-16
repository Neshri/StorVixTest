import DataFetcher
import DataPusher

class PostService:
    
    def __init__(self, fetcher, pusher, signaler) -> None:
        self.fetcher = fetcher
        self.pusher = pusher
        self.signaler = signaler
        