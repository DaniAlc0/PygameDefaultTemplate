import pygame

class Text(pygame.font.Font):
    def __init__(self, screen, color=(0,0,0), font=None, size=100, antialias=True):
        super().__init__(font, size)
        # Initialize the screen, color, and antialiasing propertie.
        self.screen = screen
        self.color = color
        self.antialias = antialias

class Label(Text):
    def __init__(self, screen):
        super().__init__(screen)
    
    # Define a method to write text on the screen.
    def write(self, text, pos, centerW=False, centerH=False):
        # Render the text as a surface using the font and color.
        self.textSurf = self.render(text, self.antialias, self.color)
        # Calculate the centering offset if centering is enabled.
        centerWidth = self.textSurf.get_width() / 2 if centerW else 0
        centerHeight = self.textSurf.get_height() / 2 if centerH else 0
        # Blit the text surface onto the screen at the specified position.
        self.screen.blit(self.textSurf, (pos[0] - centerWidth, pos[1] - centerHeight))

class TextButton(Text):
    def __init__(self, screen, size):
        super().__init__(screen, size=size)
    
    # Define a method to write text on the screen with optional button-like behavior.
    def write(self, text, pos, buttomWidth=0, center=True):
        # Render the text as a surface using the font and color.
        self.textSurf = self.render(text, self.antialias, self.color)
        # If a button width is specified and the text is wider than the button, scale the text down.
        if buttomWidth < self.textSurf.get_width() and buttomWidth != 0:
            self.textSurf = pygame.transform.scale_by(self.textSurf, (buttomWidth-20)/self.textSurf.get_width())
        # Calculate the centering offset if centering is enabled.
        centerWidth = self.textSurf.get_width() / 2 if center else 0
        centerHeight = self.textSurf.get_height() / 2 if center else 0
        # Blit the text surface onto the screen at the specified position, taking into account centering.
        self.screen.blit(self.textSurf, (pos[0] - centerWidth, pos[1] - centerHeight))
