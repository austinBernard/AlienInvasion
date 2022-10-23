import pygame

class Ship:
    
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #Load ship image and start the ship at the bottom of the screen
        self.image = pygame.image.load('space-ship.png')
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ships horizontal postion
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        #Movement flags
        self.moving_right = False
        self.moving_left = False
    
    
    def update(self):
        #Update the ships x value, not the rectangle (rect)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        self.rect.x = self.x
     
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)