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

# Set the width and height of the screen
screen_size = [640, 480]
screen = pygame.display.set_mode(screen_size)

# Set the name of the screen
game_name = "Game Torpedo Attack"
game_ver = "0.0.1"
pygame.display.set_caption(game_name + "    version - " + game_ver)

# Set the FPS of the game
FPS = 30


def draw_day_sea(screen_size):
    """
    Draw some sea on the screen
    :param screen_size: screen size
    :return: sea
    """
    pygame.draw.rect(screen,
                     MediumAquaMarine,
                     [0, screen_size[1] - screen_size[1]/3,
                      screen_size[0], screen_size[1]])

grid_submarine_rect = pygame.Rect(screen_size[0]/2, screen_size[1] - screen_size[1]/4, screen_size[0]/2, screen_size[1] - screen_size[1]/4 + screen_size[1]/12)

print(grid_submarine_rect)

def draw_grid_submarine(grid_submarine_rect):
    # Draw on the screen a GREEN line from (0, 0) to (50, 30)
    # 5 pixels wide.
    pygame.draw.line(screen, Black, [grid_submarine_rect[0], grid_submarine_rect[1]], [grid_submarine_rect[2], grid_submarine_rect[3]], 2)
    for i in range(1, 10):
        pygame.draw.line(screen, Black, [grid_submarine_rect[0] + i*10, grid_submarine_rect[1]], [grid_submarine_rect[2] + i*10, grid_submarine_rect[3]], 2)






rect = pygame.Rect(40, 40, 120, 120)


#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    # This limits the while loop to a max of 10 times per second.
    clock.tick(FPS)

    screen.fill(LightSkyBlue)

    draw_day_sea(screen_size)
    draw_grid_submarine(grid_submarine_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-40, 0)
                grid_submarine_rect.move_ip(-40, 0)
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(40, 0)
                grid_submarine_rect.move_ip(40, 0)
            elif event.key == pygame.K_UP:
                rect.move_ip(0, -40)
                grid_submarine_rect.move_ip(0, -40)
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0, 40)
                grid_submarine_rect.move_ip(0, 40)

        # Draw on the screen a GREEN line from (0, 0) to (50, 30)
        # 5 pixels wide.



    pygame.draw.line(screen, Black, [rect[0], rect[1]], [rect[2], rect[3]], 5)
    pygame.draw.ellipse(screen, Navy, [rect[0], rect[1], rect[2], rect[3]], 5)
    pygame.display.flip()

print(rect[0])
pygame.quit()
print("Goodbay sys")
sys.exit()
