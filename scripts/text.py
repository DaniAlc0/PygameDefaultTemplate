import pygame

class Text(pygame.font.Font):
    def __init__(self, screen, textColor, textAntialias, font, fontSize):
        super().__init__(font, fontSize)
        # Initialize the screen, color, and antialiasing propertie.
        self.screen = screen
        self.textColor = textColor
        self.textAntialias = textAntialias

class Label(Text):
    def __init__(self, screen, textColor=(0,0,0), textAntialias=True, font=None, fontSize=100):
        super().__init__(screen, textColor, textAntialias, font, fontSize)
    
    # Define a method to write text on the screen.
    def write(self, text, pos, centerW=False, centerH=False):
        # Render the text as a surface using the font and color.
        self.textSurf = self.render(text, self.textAntialias, self.textColor)
        # Calculate the centering offset if centering is enabled.
        centerWidth = self.textSurf.get_width() / 2 if centerW else 0
        centerHeight = self.textSurf.get_height() / 2 if centerH else 0
        # Blit the text surface onto the screen at the specified position.
        self.screen.blit(self.textSurf, (pos[0] - centerWidth, pos[1] - centerHeight))

class TextButton(Text):
    def __init__(self, screen, textColor, textAntialias, font, fontSize):
        super().__init__(screen, textColor, textAntialias, font, fontSize)
    
    # Define a method to write text on the screen with optional button-like behavior.
    def write(self, text, pos, buttomWidth, center=True, outline = True):
        # Render the text as a surface using the font and color.
        self.textSurf = self.render(text, self.textAntialias, self.textColor)
        # If a button width is specified and the text is wider than the button, scale the text down.
        if buttomWidth < self.textSurf.get_width() and buttomWidth != 0:
            self.textSurf = pygame.transform.scale_by(self.textSurf, scale := ((buttomWidth-20)/self.textSurf.get_width()))
        else: scale = 0
        # Calculate the centering offset if centering is enabled.
        centerWidth = self.textSurf.get_width() / 2 if center else 0
        centerHeight = self.textSurf.get_height() / 2 if center else 0
        # Adds outline to the text
        if outline:
            outlineWidth=max(1, self.textSurf.get_height()// 40)
            outColor = tuple(abs(x - 255) for x in self.textColor)
            for dx in [-outlineWidth, outlineWidth]:
                for dy in [-outlineWidth, outlineWidth]:
                    outlineSurf= self.render(text, self.textAntialias, outColor)
                    if scale:  outlineSurf = pygame.transform.scale_by(outlineSurf, scale)
                    self.screen.blit(outlineSurf, (pos[0] - centerWidth + dx, pos[1] - centerHeight + dy))
        # Blit the text surface onto the screen at the specified position, taking into account centering.
        self.screen.blit(self.textSurf, (pos[0] - centerWidth, pos[1] - centerHeight))
