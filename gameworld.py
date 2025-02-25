import pygame
import random
import sys
from end_screen import end_screen

def game_loop(screen, font):


# Display
    width, height = 1080, 640
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Whack-a-Mole Game")

# Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

# Variables
    score = 0
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    previous_circle_timer = 0
    circle_timer = 1500  # 250ms interval for new circles
    game_running = True

# Grid
    GRID_SIZE = 3
    CELL_SIZE = width // GRID_SIZE
    # Create the circles
    circles = []
# Circle class
    class Circle:
        def __init__(self, filled, x, y):
            self.radius = 50
            self.x = x
            self.y = y
            self.filled = filled

        def draw(self):
            if game_running:
                color = RED if self.filled else BLACK
                pygame.draw.circle(display, color, (self.x, self.y), self.radius, 1 if not self.filled else 0)
               



# Create new circles every 250ms
    def generate_new_circle():
            x = random.choice([(i + 1) * ((width // 2) // 3) for i in range(3)])
            y = random.choice([height // 3, 2 * height // 3])  # Randomly place in upper or lower half of screen
            filled = random.choice([True, False])
            return Circle(filled, x, y)

# Timer tracking
    last_circle_time = pygame.time.get_ticks()  # Time when last circle was created
    hit_sound = pygame.mixer.Sound("hit_sound.ogg")
    miss_sound = pygame.mixer.Sound("miss_sound.flac")
# Main game loop
    while game_running:
        
        
        if pygame.time.get_ticks()>60000:
            game_running = False
            break   
    # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_circle = None
                for circle in circles:
                    distance = ((mouse_x - circle.x) ** 2 + (mouse_y - circle.y) ** 2) ** 0.5
                    if distance <= circle.radius and circle.filled:
                     clicked_circle = circle
                     break
                if clicked_circle is not None:
                    score += 1
                    pygame.mixer.Sound.play(hit_sound)
                    circles.remove(circle)
                else:
                    score -= 1
                    pygame.mixer.Sound.play(miss_sound)
        if score>=10:
            circle_timer = 1000
        if score>=20:
            circle_timer = 800

    # Timer check: If 250ms has passed, generate a new circle
        current_time = pygame.time.get_ticks()
        if current_time - last_circle_time >= circle_timer:
        # Generate a new circle and replace the old one(s)
            circles = [generate_new_circle() for _ in range(3)]  # Add 3 circles every interval
            last_circle_time = current_time  # Update the last circle time

    # Drawing
        display.fill(BLACK)

    # Draw all circles
        for circle in circles:
            circle.draw()

    # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        display.blit(score_text, (10, 10))

    # Update display
        pygame.display.flip()

    # Limit FPS
        clock.tick(60)

    
    return end_screen(display,font,score)