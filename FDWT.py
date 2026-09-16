# Imports
import random, sys
import pygame 
import pygame_widgets 
from pygame_widgets.button import Button

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Five Days With Tony")

bedroom = pygame.image.load("bedroom.png")
bedroom = pygame.transform.scale(bedroom, (1280, 720))
ending = pygame.font.Font(None, 45)
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

def check_curtains():
    pass


def check_cameras():
    pass


def check_door():
    pass


curtains = Button(screen, 100, 500, 200, 75,
    text='Check Curtains', fontSize=30,
        onRelease=check_curtains, **BUTTON_STYLE)

cameras = Button(screen, 550, 500, 200, 75,
    text='Check Cameras', fontSize=30,
        onRelease=check_cameras, **BUTTON_STYLE)

door = Button(screen, 1000, 500, 200, 75,
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