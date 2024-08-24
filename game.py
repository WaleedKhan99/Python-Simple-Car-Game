import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Car Game")


# Load images
car_image = pygame.image.load("car.png")
car_width, car_height = car_image.get_size()
obstacle_image = pygame.image.load("obstacle.png")
obstacle_width, obstacle_height = obstacle_image.get_size()

# Set up game variables
car_x = 400 - (car_width / 2)
car_y = 400
car_speed = 0
obstacle_x = random.randint(0, 700)
obstacle_y = -obstacle_height
obstacle_speed = 8
score = 0
font = pygame.font.Font(None, 36)

# Define functions
def draw_car(x, y):
    screen.blit(car_image, (x, y))

def draw_obstacle(x, y):
    screen.blit(obstacle_image, (x, y))

def display_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def check_collision():
    if car_x + car_width > obstacle_x and car_x < obstacle_x + obstacle_width \
    and car_y + car_height > obstacle_y and car_y < obstacle_y + obstacle_height:
        return True
    else:
        return False

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_speed = -5
            elif event.key == pygame.K_RIGHT:
                car_speed = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_speed = 0

    # Update game variables
    car_x += car_speed
    obstacle_y += obstacle_speed

    # Check for collision
    if check_collision():
        running = False

    # Draw objects
    screen.fill((175, 239, 156))
    draw_car(car_x, car_y)
    draw_obstacle(obstacle_x, obstacle_y)
    display_score()
    pygame.display.update()

    # Check if obstacle has gone off screen and update score
    if obstacle_y > 600:
        obstacle_x = random.randint(0, 700)
        obstacle_y = -obstacle_height
        score += 1

    # Set game speed
    pygame.time.Clock().tick(60)

# Clean up and exit game
pygame.quit()
