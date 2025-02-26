import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Display
width, height = 1080, 640
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Whack-a-Mole Game")

# Farver
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Variabler
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
previous_circle_timer = 0
circle_timer = 1500  # 250ms interval for new circles

# Grid
GRID_SIZE = 3
CELL_SIZE = width // GRID_SIZE

# Cirkel class
class Circle:
    def __init__(self, filled, x, y):
        self.radius = 50
        self.x = x
        self.y = y
        self.filled = filled

    def draw(self):
        color = RED if self.filled else BLACK
        pygame.draw.circle(display, color, (self.x, self.y), self.radius, 1 if not self.filled else 0)

# Create the circles
circles = []

# Laver nye cirkler baseret på "circle_timer"
def generate_new_circle():
    x = random.choice([(i + 1) * ((width // 2) // 3) for i in range(3)])
    y = random.choice([height // 3, 2 * height // 3])  # Randomly place in upper or lower half of screen
    filled = random.choice([True, False])
    return Circle(filled, x, y)

# Timer tracking
last_circle_time = pygame.time.get_ticks()  # Time when last circle was created

# Main game loop
while True:
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
                circles.remove(circle)
            else:
                score -= 1

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
# if __name__ == "__main__":
#     hit_sound = pygame.mixer.Sound("hit_sound.ogg")
#     miss_sound = pygame.mixer.Sound("miss_sound.flac")

#     # Main game loop
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if start_time is not None:
#                     elapsed_time = pygame.time.get_ticks() - start_time
#                     mouse_x, mouse_y = pygame.mouse.get_pos()
#                     clicked_circle = None
#                     for circle in circles:
#                         distance = ((mouse_x - circle.x) ** 2 + (mouse_y - circle.y) ** 2) ** 0.5
#                         if distance <= circle.radius and circle.filled:
#                             clicked_circle = circle
#                             break
#                     if clicked_circle is not None and elapsed_time <= round_time:
#                         score += 1
#                         hit_sound.play()
#                     else:
#                         score -= 1
#                         miss_sound.play()
#                     circles = [Circle(False, (i + 1) * ((width//2) // 3)) for i in range(2)]
#                     circles.append(Circle(True, random.choice([(i + 1) * ((width //2) // 3) for i in range(3)])))
#                     start_time = None

#         display.fill(BLACK)

#         for circle in circles:
#             circle.draw()

#         score_text = font.render(f"Score: {score}", True, WHITE)
#         display.blit(score_text, (10, 10))

#         pygame.display.flip()
#         clock.tick(60)

#         if start_time is None and circles[-1].filled:
#             start_time = pygame.time.get_ticks()

#     import pygame

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# WIDTH, HEIGHT = 300, 300
# screen = pygame.display.set_mode((WIDTH, HEIGHT))

# # Colors
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)

# # Grid settings
# GRID_SIZE = 3
# CELL_SIZE = WIDTH // GRID_SIZE  # Each cell will be 100x100 pixels (300/3)

# # Object settings (e.g., spawning red squares)
# square_size = 30

# # Main loop
# running = True
# while running:
#     screen.fill(WHITE)  # Fill the background with white

#     for row in range(GRID_SIZE):
#         for col in range(GRID_SIZE):
#             # Calculate the position of the top-left corner of the cell
#             x = col * CELL_SIZE
#             y = row * CELL_SIZE

#             # Draw a red square in each grid cell
#             pygame.draw.rect(screen, RED, (x + (CELL_SIZE - square_size) // 2, 
#                                            y + (CELL_SIZE - square_size) // 2, 
#                                            square_size, square_size))

#     pygame.display.flip()

#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# # Quit Pygame
# pygame.quit()
