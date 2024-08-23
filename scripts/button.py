import pygame
from scripts.text import TextButton

class Button(TextButton):
    def __init__(self, screen, pos, size=(300, 100), textColor=(0,0,0), textHoverColor=(0,0,0), textAntialias=True, textFont=None, textFontSize=100, buttonColor=(128,128,128), buttonHoverColor=(100,100,100), shadowSize=(0,0), shadowColor=(0,0,0), border=-1, borderColor=(0,0,0), borderRadius=0, transparency=0):
        super().__init__(screen, textColor, textAntialias, textFont, textFontSize)
        self.screen = screen
        self.pos = pos

        # Create the button rect.
        self.buttonRect = pygame.Rect(0, 0, size[0], size[1])
        self.buttonRect.center = (pos[0], pos[1])
        self.buttonX = self.buttonRect.x
        self.buttonY = self.buttonRect.y
        self.buttonColor = buttonColor
        self.currentButtonColor = buttonColor

        # Create the shadown rect.
        self.shadowRect = pygame.Rect(0,0,size[0], size[1])
        self.shadowRect.center = (pos[0]+shadowSize[0], pos[1]+shadowSize[1])
        self.shadowSize = shadowSize
        self.shadowColor = shadowColor

        # Border
        self.border = border # Border=-1: OFF / Border>1: ON
        self.borderColor = borderColor
        self.borderRadius = borderRadius

        self.buttonHoverColor = buttonHoverColor
        self.textHoverColor = textHoverColor
        self.textCurrentColor = self.textColor
        self.transparency = transparency # Transparency=0: OFF / Transparency=-1: ON
        self.pressed = False
        
    def draw(self, text):
        # Draw Shadow
        pygame.draw.rect(self.screen, self.shadowColor, self.shadowRect, border_radius=self.borderRadius, width=self.transparency)
        # Draw Buttom
        pygame.draw.rect(self.screen, self.currentButtonColor, self.buttonRect, border_radius=self.borderRadius, width=self.transparency)
        # Draw border
        pygame.draw.rect(self.screen, self.borderColor, self.buttonRect, border_radius=self.borderRadius, width=self.border)
        # Write the specified text at the center of the rectangle, with the width of the rectangle as the maximum width.
        self.write(text, (self.buttonRect.centerx, self.buttonRect.centery), self.buttonRect.width, center=True)
    
    def click(self, aspectRatio):
        mousePos = pygame.mouse.get_pos()
        # Update the rectangle's position and size based on the aspect ratio.
        updatedRect = pygame.Rect(self.buttonX*aspectRatio[0], self.buttonY*aspectRatio[1], self.buttonRect.width*aspectRatio[0], self.buttonRect.height*aspectRatio[1])
        # Check if the mouse is within the updated rectangle.
        if updatedRect.collidepoint(mousePos):
            self.currentButtonColor = self.buttonHoverColor
            self.textColor = self.textHoverColor
            # If the left mouse button is pressed.
            if pygame.mouse.get_pressed()[0]:
                self.buttonRect.center = (self.pos[0]+self.shadowSize[0], self.pos[1]+self.shadowSize[1])
                self.pressed = True
            else:
                # If the pressed flag is True, it means the button was just released.
                if self.pressed:
                    self.buttonRect.center = (self.pos[0], self.pos[1])
                    self.pressed = False
                    # Return to indicate a click.
                    return True
        else:
            self.buttonRect.center = (self.pos[0], self.pos[1])
            self.currentButtonColor = self.buttonColor
            self.textColor = self.textCurrentColor
            self.pressed = False
            return False

class Slider(Button):
    def __init__(self, screen, pos, sliderValue, size=(300, 30), multiplier=1, buttonColor = (100,100,100), buttonHoverColor = (100,100,100), borderRadius = 20, padding = 20, pointerRadius = 8):
        super().__init__(screen, pos, size, buttonColor=buttonColor, buttonHoverColor=buttonHoverColor, borderRadius=borderRadius)
        self.padding = padding
        self.pointerRadius = pointerRadius
        self.multiplier = multiplier
        self.pointerPos = int(((self.buttonRect.width - self.padding*2) * sliderValue / 100) / multiplier) + self.padding

    def drawSlider(self):
        self.draw('')
        pygame.draw.line(self.screen, (0,0,0), (self.buttonX + self.padding, self.buttonY+self.buttonRect.height/2), (self.buttonRect.width - self.padding + self.buttonX, self.buttonRect.height/2 + self.buttonY), width=2)
        pygame.draw.circle(self.screen, (0,0,0), (self.buttonX + self.pointerPos, self.buttonY+self.buttonRect.height/2), radius=self.pointerRadius)
    
    def clickSlider(self, aspectRatio):
        mousePos = pygame.mouse.get_pos()
        updatedRect = pygame.Rect((self.buttonX + self.padding)*aspectRatio[0], self.buttonY*aspectRatio[1], (self.buttonRect.width-self.padding*2)*aspectRatio[0], self.buttonRect.height*aspectRatio[1])
        if updatedRect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0]:
                self.pointerPos =  mousePos[0] - updatedRect.x
                self.sliderValue = round((self.pointerPos*100/updatedRect.width)*self.multiplier)
                # self.pointerPos = (self.pointerPos + self.padding) / aspectRatio[0] # Smooth
                self.pointerPos = int(((self.buttonRect.width - self.padding*2) * self.sliderValue / 100) / self.multiplier) + self.padding # Truncated
                return True
        return False
