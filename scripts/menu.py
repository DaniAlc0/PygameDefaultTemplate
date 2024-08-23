import pygame
from scripts.text import Label
from scripts.button import Button, Slider

class Menu():
    def __init__(self, game):
        self.game = game
        self.newScreen()
    
    def newScreen(self):
        # Create a new screen surface with the game's width and height.
        self.screen = pygame.Surface((self.game.WIDTH, self.game.HEIGHT))

        # Create text and button objects.
        self.text = Label(self.screen)
        self.button1 = Button(self.screen, pos=(150, 150))
        self.button2 = Button(self.screen, pos=(150, 300), borderRadius=20, textColor=(0,0,255), textHoverColor=(255,0,0))
        self.button3 = Button(self.screen, pos=(150, 450), shadowSize=(6,6))
        self.button4 = Button(self.screen, pos=(500, 600), border=2, transparency=-1, textHoverColor=(128,128,128))
        self.button5 = Button(self.screen, pos=(500, 150), border=2, borderRadius=20)
        self.button6 = Button(self.screen, pos=(500, 300), borderRadius=20, shadowSize=(6,6), border=2)
        self.button7 = Button(self.screen, pos=(500, 450), borderRadius=20, shadowSize=(6,6), textColor=(255,255,255), textHoverColor=(255,255,255), buttonColor=(20,20,20), buttonHoverColor=(0,0,0), shadowColor=(100,100,100))
        self.button8 = Button(self.screen, pos=(1200, 30), size=(150, 50), textFontSize=50, borderRadius=20, shadowSize=(6,6), border=2)

        self.slider = Slider(self.screen, pos=(850, 150), sliderValue=self.game.audioSettings['mainVolume'])

    def run(self):
        self.events()
        self.update()
        self.draw()
        self.inputs()
    
    def update(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
        
    def draw(self):
        # Scale the screen surface to fit the display surface.
        self.game.scaleScreen(self.screen)
        self.screen.fill((255,255,255))

        # Draw buttons with their respective text.
        self.button1.draw('1600x900')
        self.button2.draw('1280x720')
        self.button3.draw('720x480')
        if self.game.videoSettings['showFps']:
            status = 'ON'
            self.text.write('FPS: ', (0, 0))
            self.text.write(str(int(self.game.clock.get_fps())), (170, 0))
        else:
            status = 'OFF'
        self.button4.draw(f'{self.game.gameTexts['showFps']} - {status}')
        self.button5.draw('English')
        self.button6.draw('Português')
        if self.game.videoSettings['vsync'] == 1:
            status = 'ON'
        else:
            status = 'OFF'
        self.button7.draw(f'VSync - {status}')
        self.text.write(self.game.gameTexts['language'], (int(self.game.WIDTH/2), 0), centerW=True)
        self.button8.draw(self.game.gameTexts['exit'])
        self.slider.drawSlider()

    def inputs(self):
        # Handle button clicks.
        if self.button1.click(self.game.aspectRatio):
            self.game.resizeScreen(1600, 900, self.game.videoSettings['vsync'])
            self.newScreen()
        if self.button2.click(self.game.aspectRatio):
            self.game.resizeScreen(1280, 720, self.game.videoSettings['vsync'])
            self.newScreen()
        if self.button3.click(self.game.aspectRatio):
            self.game.resizeScreen(720, 480, self.game.videoSettings['vsync'])
            self.newScreen()
        if self.button4.click(self.game.aspectRatio):
            self.game.setSettings('video', 'showFps', False) if self.game.videoSettings['showFps'] else self.game.setSettings('video', 'showFps', True)
        if self.button5.click(self.game.aspectRatio):
            self.game.setSettings('language', 'languageSet', 'en-US')
        if self.button6.click(self.game.aspectRatio):
            self.game.setSettings('language', 'languageSet', 'pt-BR')
        if self.button7.click(self.game.aspectRatio):
            self.game.setSettings('video', 'vsync', 0) if self.game.videoSettings['vsync'] == 1 else self.game.setSettings('video', 'vsync', 1)
            self.game.resizeScreen(self.game.videoSettings['width'], self.game.videoSettings['height'], self.game.videoSettings['vsync'])
        if self.button8.click(self.game.aspectRatio):
            self.game.running = False
        if self.slider.clickSlider(self.game.aspectRatio):
            self.game.setSettings('audio', 'mainVolume', self.slider.sliderValue)
