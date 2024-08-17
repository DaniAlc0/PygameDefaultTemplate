import pygame
from scripts.screen import Screen
from scripts.menu import Menu

class Game(Screen):
    def __init__(self):
        pygame.init()
        super().__init__()
        self.running = True
        # Set initial game state to 'menu'.
        self.gameState = 'menu'
        # Create an instance of the Menu class, passing the current Game instance as an argument.
        self.menu = Menu(self)
    
    def run(self):
        while self.running:
            # Calculate the time elapsed since the last frame (delta time).
            self.deltaTime()
            # Handle user input and update the game state.
            self.controller()
            # Update the screen
            self.screenUpdate()
        pygame.quit()
    
    # Define a method to handle user input and update the game state.
    def controller(self):
        # If the current game state is 'menu', run the menu.
        if self.gameState == 'menu':
            self.menu.run()
