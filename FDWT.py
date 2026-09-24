# Imports
import random, sys
import pygame 
import pygame_widgets 
from pygame_widgets.button import Button

# Pygame Setup
pygame.init()
Width, Height = 1280, 720
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Five Days With Tony")
clock = pygame.time.Clock()

bedroom = pygame.image.load("bedroom_phase0.png")
bedroom = pygame.transform.scale(bedroom, (Width, Height))

ending = pygame.font.Font(None, 45)
title_font = pygame.font.Font(None, 140)
sub_font = pygame.font.Font(None, 50)

door_phases = [
    pygame.transform.scale(pygame.image.load("bedroom_phase1.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("bedroom_phase2.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("bedroom_phase3.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("bedroom_phase4.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("bedroom_phase5.png"), (Width, Height)),
]

# Button Style Setup
BUTTON_STYLE = dict(
    margin=10,
    radius=12,
    inactiveColour=(255, 255, 255),
    hoverColour=(200, 200, 200),
    pressedColour=(85, 85, 85),
    textColour=(20, 20, 20),
)

class Animatronic:
    def __init__(self, name, position):
        self.name = name
        self.position = position # Starting Position

    def move(self):
        # Animatronic Movement
        pass

Tony = Animatronic("Tony", "Bedroom 3")
Cookie = Animatronic("Cookie", "Play Room")
GoldenHero = Animatronic("Golden Hero", "Bedroom 2")
Springson = Animatronic("Springson", "Backyard")
Toeneriette = Animatronic("Toeneriette", "Storage")

def check_curtains():
    pass


def check_cameras():
    pass


def check_door():
    pass


curtains = Button(screen, 100, 570, 200, 75,
    text='Check Curtains', fontSize=30,
        onRelease=check_curtains, **BUTTON_STYLE)

cameras = Button(screen, 550, 570, 200, 75,
    text='Check Cameras', fontSize=30,
        onRelease=check_cameras, **BUTTON_STYLE)

door = Button(screen, 1000, 570, 200, 75,
    text='Close Door', fontSize=30,
        onRelease=check_door, **BUTTON_STYLE)


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

        hours = int(game_time // 60)

        time_text = ending.render(f"{hours:0}AM", True, (255, 255, 255))
        screen.blit(time_text, (1190, 20))

        screen.blit(bedroom, (0, 0))
        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick(60)  # FPS
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()