import random, sys
import pygame

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Five Days With Tony") 
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse = pygame.mouse.get_pos()
    print (mouse)
    
    # Screen Reset
    screen.fill("black")
    pygame.display.flip()

    clock.tick(60)  # Frames Per Second

pygame.quit()
sys.exit()