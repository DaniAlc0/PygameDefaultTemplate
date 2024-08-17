import pygame
from scripts.settings import Settings

class Screen(Settings):
    # Manages the game screen.
    def __init__(self):
        super().__init__()
        # Set default screen width and height.
        self.WIDTH = 1280
        self.HEIGHT = 720
        # Set the screen using the video settings from the Settings class.
        self.setScreen(self.videoSettings['width'], self.videoSettings['height'], self.videoSettings['vsync'])
        self.clock = pygame.time.Clock()

    def setScreen(self, width, height, vsync):
        self.displaySurf = pygame.display.set_mode((width, height), vsync=vsync)
        # Calculate the width and height ratios to scale the screen.
        self.widthRatio = width / self.WIDTH
        self.heightRatio = height / self.HEIGHT
        self.aspectRatio = (self.widthRatio, self.heightRatio)
        pygame.display.set_caption('Pygame Default Template')
    
    def scaleScreen(self, screen):
        # Scale the screen surface to fit the display surface.
        pygame.transform.scale(screen, self.displaySurf.get_size(), self.displaySurf)
    
    def resizeScreen(self, width, height, vsync):
        # Update the video settings in the Settings class.
        self.setSettings('video','width', width)
        self.setSettings('video', 'height', height)
        self.setSettings('video', 'vsync', vsync)
        # Quit the current display and set up a new one with the updated settings.
        pygame.display.quit()
        self.setScreen(width, height, vsync)
    
    def deltaTime(self):
        # Get the time since the last frame in milliseconds and convert it to seconds
        self.dt = self.clock.tick(self.videoSettings['fps']) / 1000
    
    def screenUpdate(self):
        # Update the entire display window
        pygame.display.update()
