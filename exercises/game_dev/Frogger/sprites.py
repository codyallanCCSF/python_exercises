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

        # Movement distance per key press (frog size)
        self.hop_distance = 40

    def handle_hop(self, key):
        """Moves the frog a single discrete step on key press"""
        if key == pygame.K_UP:
            self.rect.y -= self.hop_distance
        elif key == pygame.K_DOWN:
            self.rect.y += self.hop_distance
        elif key == pygame.K_LEFT:
            self.rect.x -= self.hop_distance
        elif key == pygame.K_RIGHT:
            self.rect.x += self.hop_distance

        # Boundary check - Left
        if self.rect.left < 0:
            self.rect.left = 0

        # Boundary check - Right
        if self.rect.right > c.SCREEN_WIDTH:
            self.rect.right = c.SCREEN_WIDTH

        # Boundary check - Bottom
        if self.rect.bottom > c.SCREEN_HEIGHT:
            self.rect.bottom = c.SCREEN_HEIGHT

        # Boundary check - Top
        if self.rect.top < 0:
            self.rect.top = 0


