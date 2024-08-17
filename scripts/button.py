import pygame
from scripts.text import TextButton

class Button(TextButton):
    def __init__(self, screen, width, height, pos, borderRadius=0, size=100):
        super().__init__(screen, size)
        # Create a new rectangle object with the specified width and height.
        self.rect = pygame.Rect(0, 0, width, height)
        # Set the center of the rectangle to the specified position.
        self.rect.center = (pos[0], pos[1])
        # Set the top color of the button.
        self.topColor = 'darkgrey'
        self.screen = screen
        self.borderRadius = borderRadius
        self.pressed = False
    
    def draw(self, text):
        # Draw a rectangle on the screen with the top color and the specified rectangle.
        pygame.draw.rect(self.screen, self.topColor, self.rect, border_radius=self.borderRadius)
        # Write the specified text at the center of the rectangle, with the width of the rectangle as the maximum width.
        self.write(text, (self.rect.centerx, self.rect.centery), self.rect.width)
    
    def click(self, aspectRatio):
        mousePos = pygame.mouse.get_pos()
        # Update the rectangle's position and size based on the aspect ratio.
        updatedRect = pygame.Rect(self.rect.x*aspectRatio[0], self.rect.y*aspectRatio[1], self.rect.width*aspectRatio[0], self.rect.height*aspectRatio[1])
        # Check if the mouse is within the updated rectangle.
        if updatedRect.collidepoint(mousePos):
            # If the left mouse button is pressed.
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                 # If the pressed flag is True, it means the button was just released.
                if self.pressed:
                    self.pressed = False
                    # Return to indicate a click.
                    return True
        return False
