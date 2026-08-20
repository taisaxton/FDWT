import random, sys
import pygame # pip install pygame
import pygame_widgets # pip install pygame_widgets
from pygame_widgets.button import Button


# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Five Days With Tony") 
clock = pygame.time.Clock()


run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    mouse = pygame.mouse.get_pos()                                    
    
    
    print (mouse)
    
    # Screen Reset
    screen.fill("black")

    clock.tick(60)  # Frames Per Second
    
    pygame_widgets.update(events)
    pygame.display.update()
    
pygame.quit()
sys.exit()