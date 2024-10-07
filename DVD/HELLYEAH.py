import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD Logo")

# Colors
WHITE = (255, 255, 255)
LOGO_COLOR = (255, 0, 0)  # Red for the DVD logo

# Load the DVD logo (you can use any image or create a simple rect)
logo_width, logo_height = 100, 50  # Dimensions of the DVD logo

# Starting position and velocity
x = random.choice([0, WIDTH - logo_width])  # Start from a corner
y = random.choice([0, HEIGHT - logo_height])
speed_x, speed_y = 5, 5  # Speed at which the logo moves

# Ensure it moves towards the next corner
if x == 0 and y == 0:
    speed_x, speed_y = 5, 5  # Move bottom right
elif x == WIDTH - logo_width and y == 0:
    speed_x, speed_y = -5, 5  # Move bottom left
elif x == 0 and y == HEIGHT - logo_height:
    speed_x, speed_y = 5, -5  # Move top right
else:
    speed_x, speed_y = -5, -5  # Move top left

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the logo
    x += speed_x
    y += speed_y

    # Check if it hits any corner and reverse direction
    if (x <= 0 and y <= 0):  # Top left corner
        speed_x, speed_y = 5, 5
    elif (x >= WIDTH - logo_width and y <= 0):  # Top right corner
        speed_x, speed_y = -5, 5
    elif (x <= 0 and y >= HEIGHT - logo_height):  # Bottom left corner
        speed_x, speed_y = 5, -5
    elif (x >= WIDTH - logo_width and y >= HEIGHT - logo_height):  # Bottom right corner
        speed_x, speed_y = -5, -5

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the DVD logo (for simplicity, we'll use a rectangle)
    pygame.draw.rect(screen, LOGO_COLOR, (x, y, logo_width, logo_height))

    # Update the display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
