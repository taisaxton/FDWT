import random, sys
import pygame # pip install pygame
import pygame_widgets # pip install pygame_widgets
from pygame_widgets.button import Button


# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Five Days With Tony") 
clock = pygame.time.Clock()


class Animatronic:
    def __init__(self, name, position):
        self.name = name
        self.position = position # Starting position

def move(self):
    # Logic for animatronic movement
    pass

Tony = Animatronic("Tony", "Bedroom 3")
Cookie = Animatronic("Cookie", "Play Room")
GoldenHero = Animatronic("Golden Hero", "Bedroom 2")
Springson = Animatronic("Springson", "Backyard")
Toeneriette = Animatronic("Toeneriette", "Storage")

LeftDoor = Button(
    screen,
    100,  # X-coord
    500,  # Y-coord
    150,  # Width
    75,  # Height

    text='Close',  
    fontSize=30,  
    margin=10,  
    radius=10,
    inactiveColour=(255, 255, 255),  
    hoverColour=(200, 200, 200), 
    pressedColour=(85, 85, 85),  
    onClick=lambda: print('Click')
)

Cameras = Button(
    screen,
    500,  # X-coord
    500,  # Y-coord
    200,  # Width
    75,  # Height

    text='Check Cameras',  
    fontSize=30,  
    margin=10,  
    radius=10,
    inactiveColour=(255, 255, 255),  
    hoverColour=(200, 200, 200), 
    pressedColour=(85, 85, 85),  
    onClick=lambda: print('Click')
)

RightDoor = Button(
    screen,
    1000,  # X-coord
    500,  # Y-coord
    150,  # Width
    75,  # Height

    text='Close',  
    fontSize=30,  
    margin=10,  
    radius=10,
    inactiveColour=(255, 255, 255),  
    hoverColour=(200, 200, 200), 
    pressedColour=(85, 85, 85),  
    onClick=lambda: print('Click')
)

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