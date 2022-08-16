import toml


class ConfigReader:
    """ConfigReader parses configuration files and returns dictionaries
    """
    def __init__(self, file_name) -> None:
        self.file_name = file_name  
        
    
    def get_info(self):
        """Returns available information

        Returns:
            dict: Dictionary made from the data in the configuration file._
        """
        return toml.load(self.file_name)

