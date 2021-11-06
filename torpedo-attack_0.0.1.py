# Import the required library
import pygame
import sys
from math import pi

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
Black = (0, 0, 0)
LightSkyBlue = (135, 206, 250)
DeepSkyBlue = (0, 191, 255)
MediumAquaMarine = (102, 205, 170)
Navy = (0, 0, 128)
SteelBlue = (70, 130, 180)
LightSteelBlue = (176, 196, 222)

# Set the height and width of the screen
screen_size = [640, 480]
screen = pygame.display.set_mode(screen_size)

# Set the name of the screen
game_name = "Game Torpedo Attack"
game_ver = "0.0.1"
pygame.display.set_caption(game_name + "    version - " + game_ver)

# Set the FPS of the game
FPS = 30




rect = pygame.Rect(40, 40, 120, 120)

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    # This limits the while loop to a max of 10 times per second.
    clock.tick(FPS)

    screen.fill(LightSkyBlue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-40, 0)
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(40, 0)
            elif event.key == pygame.K_UP:
                rect.move_ip(0, -40)
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0, 40)

    pygame.draw.rect(screen, MediumAquaMarine, rect, 0)
    pygame.display.flip()

print("Goodbay pygame")
pygame.quit()
print("Goodbay sys")
sys.exit()
