import toml

class ConfigReader:
    
    def __init__(self, file_name) -> None:
        self.file_name = file_name  
        print(toml.load(file_name))
        pass
    
ConfigReader("config.toml")