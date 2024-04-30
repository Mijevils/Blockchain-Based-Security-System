import json
import os


class Config():
    def readConfig(self):
        """
        Description: Function to read config.json and determine what directories should be under protection
        Input: Self
        Output: The content of config.json
        """
        if os.path.isfile('config.json'):
            with open ('config.json', 'rb') as file:
                if (os.stat("config.json").st_size == 0):
                    return {"paths" : []}
                else:
                    return json.load(file)
        else:
            self.makeConfig()
            return {"paths" : []}

    def makeConfig(self):
        """
        Description: Function to make a config file in case it is not found.
        Input: None, just self
        Output: None
        """
        if not (os.path.isfile('config.json')):
            with open('config.json', 'x') as f:
                self.config = f
        else:
            print("File config.json already exists.")

    def writeConfig(self, path):
        """
        Description: Write data to the config file.
        Input: A string path, containing the path of a protected file.
        Output: None
        """
        if not os.path.isfile("config.json"):
            self.makeConfig()

        data = self.readConfig()
        data["paths"].append(path)

        with open('config.json', 'w') as file:
            json.dump(data,file)

    def clearConfig(self):
        """
        Description: Wipes config file.
        Input: None, just self
        Output: None
        """
        if os.path.isfile("config.json"):
            with open('config.json', "r+") as file:
                file.truncate(0)
        else:
            print("No file named config.json")

    def getProtecteds(self):
        """
        Description: Obtains path array from config file
        Input: None, just self.
        Output: String array containing protected file paths.
        """
        data = self.readConfig()
        return data["paths"]

#a = Config()
#a.getProtecteds()
