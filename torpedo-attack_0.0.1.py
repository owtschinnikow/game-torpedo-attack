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


grid_submarine_rect = pygame.Rect(screen_size[0], screen_size[1], 0, 0)
def draw_grid_submarine(grid_submarine_rect):
    # Draw on the screen a GREEN line from (0, 0) to (50, 30)
    # 5 pixels wide.
    pygame.draw.line(screen,
                     Black,
                     [grid_submarine_rect[0]/2, grid_submarine_rect[1] - grid_submarine_rect[1]/4],
                     [grid_submarine_rect[0]/2, grid_submarine_rect[1] - grid_submarine_rect[1]/4 + grid_submarine_rect[1]/12],
                     2)
    for i in range(1, 10):
        pygame.draw.line(screen,
                         Black,
                         [grid_submarine_rect[0]/2 + i*10, grid_submarine_rect[1] - grid_submarine_rect[1]/4.4],
                         [grid_submarine_rect[0]/2 + i*10, grid_submarine_rect[1] - grid_submarine_rect[1]/4 + grid_submarine_rect[1]/15],
                         2)
        pygame.draw.line(screen,
                         Black,
                         [grid_submarine_rect[0]/2 - i*10, grid_submarine_rect[1] - grid_submarine_rect[1]/4.4],
                         [grid_submarine_rect[0]/2 - i*10, grid_submarine_rect[1] - grid_submarine_rect[1]/4 + grid_submarine_rect[1]/15],
                         2)
    for i in range(10, 11):
        pygame.draw.line(screen,
                         Black,
                         [grid_submarine_rect[0]/2 + i*10, grid_submarine_rect[1] - grid_submarine_rect[1]],
                         [grid_submarine_rect[0]/2 + i*10, grid_submarine_rect[1] - grid_submarine_rect[1]/4 + grid_submarine_rect[1]],
                         2)
        pygame.draw.line(screen,
                         Black,
                         [grid_submarine_rect[0]/2 - i*10, grid_submarine_rect[1] - grid_submarine_rect[1]],
                         [grid_submarine_rect[0]/2 - i*10, grid_submarine_rect[1] - grid_submarine_rect[1]/4 + grid_submarine_rect[1]],
                         2)


def move_grid_submarine():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and grid_submarine_rect[0] > 0:
            grid_submarine_rect.move_ip(-20, 0)
        elif event.key == pygame.K_RIGHT and grid_submarine_rect[0] < screen_size[0] * 2:
            grid_submarine_rect.move_ip(20, 0)


def move_tortedo():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and grid_submarine_rect[0] > 0:
            grid_submarine_rect.move_ip(-20, 0)
        elif event.key == pygame.K_RIGHT and grid_submarine_rect[0] < screen_size[0] * 2:
            grid_submarine_rect.move_ip(20, 0)

torpedo_rect = grid_submarine_rect
def draw_torpedo(torpedo_rect):
    """
    Draw some torpedo on the screen
    :param grid_submarine_rect:
    :return: torpedo
    """
    pygame.draw.rect(screen,
                     Navy,
                     [torpedo_rect[0]/2,
                      torpedo_rect[1],
                      0,
                      -10], 2)

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

torpedo = []

while not done:
    # This limits the while loop to a max of FPS.
    clock.tick(FPS)
    # Made screen with sky
    screen.fill(LightSkyBlue)
    # Draw objects
    draw_day_sea(screen_size)
    draw_grid_submarine(grid_submarine_rect)

    torpedo = []
    # Chek game QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("draw_torpedo")
            torpedo.append([draw_torpedo(torpedo_rect)])

        # Move grid of submarin
        move_grid_submarine()
    print(torpedo)






    pygame.display.flip()



pygame.quit()
sys.exit()
