import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flappy Game')
window.fill((255, 255, 255))

# Set up the clock for a decent framerate
clock = pygame.time.Clock()

# Main game loop
running = True

#image
bird = pygame.image.load('bird.gif')

x = 300
y = 300
while running:
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the window with a color (RGB)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

        for i in pygame.event.get():
            if i.type == QUIT:
                pygame.quit()
                sys.exit()
            if i.type == KEYDOWN:
                if i.key == K_UP:
                    y -= 10

        window.blit(bird, (x, y))





        pygame.display.update()
    except Exception as e:
        print(f"An error occurred: {e}")
        break
    except KeyboardInterrupt:
        print(f"Keyboard interrupt detected.")
        break

# Quit Pygame
pygame.quit()
sys.exit()