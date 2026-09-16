# Imports
import random, sys
import pygame 
import pygame_widgets 
from pygame_widgets.button import Button

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Five Days With Tony")
clock = pygame.time.Clock()


class Animatronic:
    def __init__(self, name, position):
        self.name = name
        self.position = position # Starting Position

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


def main():
    run = True
    game_time = 0

    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False # Screen Reset
                quit()

        mouse = pygame.mouse.get_pos()                                    
        screen.fill("black")
        game_time += clock.get_time() / 1000

        if game_time >= 360: # 6 Mins (6 AM)
            run = False
        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick(60)  # FPS
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()