import json
import os

class Settings():
    # Manages Settings stored in a JSON file.
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), '..')
        self.filePath = os.path.join(self.path, 'config', 'settings.json')
        self.settings = self.loadSettings()
        self.gameSettings()
    
    def loadSettings(self):
        # Loads settings from the JSON file and returns a dictionary.
        with open(self.filePath, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    def gameSettings(self):
        # Initializes game settings from the aloaded settings.
        self.videoSettings = self.getSettings('video')
        self.audioSettings = self.getSettings('audio')
        self.language = self.getSettings('language')
        self.languageSet = self.language['languageSet']
        self.gameTexts = self.language[self.languageSet]
        self.gameData = self.getSettings('gameData')
        self.controls = self.getSettings('keys')
    
    def updateSettings(self):
        # Updates the JSON file with the new settings stored in the settings dictionary.
        with open(self.filePath, 'w', encoding='utf-8') as file:
            json.dump(self.settings, file, indent=4, ensure_ascii=False)
        self.gameSettings()

    def getSettings(self, key):
        # Returns the value of the setting specified by the key.
        return self.settings.get(key)
    
    def setSettings(self, option, key, value):
        # Sets the value of the setting specified by the key and updates the JSON file.
        self.settings[option][key] = value
        self.updateSettings()
