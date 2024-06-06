import json
from .exceptions import *


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Configuration(metaclass=SingletonMeta):
    _attributes = ['APIKEY', 'APISECRET', 'URL_BASE', 'URL_PORT']

    def load(self, file_path):
        try:
            with open(file_path, 'r') as config_file:
                config_data = json.load(config_file)
                self.load_json(config_data)
        except:
            exit("Exception")

    def load_json(self, datas):
        keys = datas.keys()

        for attr in Configuration._attributes:
            if attr in keys:
                setattr(self, attr, datas[attr])
            else:
                raise InvalidConfigurationException

    def get_baseurl(self):
        if self.URL_PORT is None:
            return self.URL_BASE
        else:
            return f"{self.URL_BASE}:{self.URL_PORT}"