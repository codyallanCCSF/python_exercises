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

        # Initialize Frog
        self.frog = sprites.Frog()


        # Initialize obstacles group
        self.obstacles = pygame.sprite.Group()
        
        # Define lane configurations: (y_position, speed, num_cars)
        lane_configs = [
            # === BOTTOM HIGHWAY: ALL MOVING RIGHT ===
            # Lane 1 (Bottom-most) - Slow
            {"y": 640, "speed": 2, "count": 3, "color": (255, 140, 0)},
            # Lane 2 - Medium
            {"y": 560, "speed": 3, "count": 2, "color": (0, 255, 255)},
            # Lane 3 (Below Median) - Fast
            {"y": 480, "speed": 5, "count": 2, "color": (255, 20, 147)},
            
            # [MEDIAN SAFE ZONE SITS HERE AROUND Y=460 to Y=500]
            
            # === TOP HIGHWAY: ALL MOVING LEFT ===
            # Lane 4 (Above Median) - Slow/Packed
            {"y": 320, "speed": -3, "count": 3, "color": (255, 255, 0)},
            # Lane 5 - Medium
            {"y": 240, "speed": -5, "count": 3, "color": (138, 43, 226)},
            # Lane 6 (Top-most) - Fast
            {"y": 160, "speed": -7, "count": 2, "color": (255, 0, 0)}
            ]
        car_spacing = 260

        # Loop through configurations
        for lane in lane_configs:
            for i in range(lane["count"]):
                if lane["speed"] > 0:
                    start_x = -(i * car_spacing)
                else:
                    start_x = c.SCREEN_WIDTH + (i * car_spacing)
                    
                car = sprites.Car(
                        y_position=lane["y"], 
                        speed=lane["speed"], 
                        x_position=start_x,
                        color=lane["color"]
                        )
                self.obstacles.add(car)


        # Initialize sprites group and add objects
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.frog)
        self.all_sprites.add(self.obstacles)

    def check_collisions(self):
        """Cheks if the frog has collided with any obstacle"""
        # spritecollideany returns object it hit, or none
        if pygame.sprite.spritecollideany(self.frog, self.obstacles):
            print("SPLAT! The frog was hit by a car!")
            # Reset frog position to the starting line
            self.frog.reset_position()

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

            # 2. Update game state. For every frame:
            self.all_sprites.update()
            self.check_collisions()

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
