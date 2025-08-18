import configparser
import os

class ConfigReader:
    def __init__(self, env='QA'):
        self.config = configparser.ConfigParser()
        path = os.path.join(os.path.dirname(__file__),'..','config', 'config.ini')
        self.config.read(path)
        self.env = env.upper()

    def get(self,key):
        return self.config[self.env][key]
