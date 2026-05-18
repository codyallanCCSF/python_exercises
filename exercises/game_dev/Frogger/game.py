import pygame
import constants as c
import sprites

class Game:
    """Executes game loop - Manager Class"""

    def __init__(self):
        """Initializes Game class member variables and methods"""

        print(f"[game.py] is connected! Running version {c.VERSION}")

        # Initialize all imported pygame modules
        pygame.init()

        # Create game window surface
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        pygame.display.set_caption("Frogger")

        # Track game state and frame timing
        self.running = True
        self.clock = pygame.time.Clock()

        # Initialize Frog and Sprite Group
        self.frog = sprites.Frog()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.frog)

    def run(self):
        """Core game loop"""
        while self.running:
            # 1. Handle events (input)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Check for key press
                elif event.type == pygame.KEYDOWN:
                    self.frog.handle_hop(event.key)

            # 2. Update game state

            # 3. Render / Draw
            self.screen.fill((0, 0, 0)) # Fill screen with black

            # Draw the sprite group to the screen
            self.all_sprites.draw(self.screen)

            pygame.display.flip() # Swap the display buffers
            self.clock.tick(c.FPS) # Maintain 60 FPS

        # Cean up when loop ends
        pygame.quit()

    def say_hello(self):
        print("Hello World!")
