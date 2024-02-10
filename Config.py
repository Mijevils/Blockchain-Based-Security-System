import json
import os


class Config():
    def __init__(self):
        self.config = {}

    def makeConfig(self, data):
        if (os.path.isdir('config.json')):
            with open ('config.json', w) as f:
                json.dump(data, f)
        else:
            with open('config.json', 'rb') as f:
                self.config = f
