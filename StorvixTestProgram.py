import ConfigReader
import PostService
import DataFetcher
import DataPusher
import Signaler


def main():
    config = ConfigReader.ConfigReader("config.toml")
    settings = config.get_info()
    #Use settings for something
    fetcher = DataFetcher.DataFetcher()
    pusher = DataPusher.DataPusher()
    signaler = Signaler.Signaler()
    poster = PostService.PostService(fetcher, pusher, signaler)
    
    
    
if __name__ == '__main__':
    main()