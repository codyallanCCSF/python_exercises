import pygame
import constants as c

print("[sprites.py] is connected and awake!")

class Frog(pygame.sprite.Sprite):
    """Defines the Frog subclass of Sprite class"""    

    def __init__(self):
        """Initializes Frog class member variables and methods"""
        super().__init__()
        
        # Create a 40x40 green rectangle
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0))

        # Get the bounding rectandgle at bottom center
        self.rect = self.image.get_rect()
        self.rect.centerx = c.SCREEN_WIDTH // 2
        self.rect.bottom = c.SCREEN_HEIGHT - 20


