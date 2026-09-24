# ─── Imports
import random, sys
import pygame
import pygame_widgets
from pygame_widgets.button import Button

# ─── Pygame Setup 
pygame.init()
Width, Height = 1280, 720
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Five Days With Tony")
clock = pygame.time.Clock()

# icon = pygame.image.load('icon.png')
# pygame.display.set_icon(icon)

# ─── Images 
bedroom = pygame.transform.scale(
    pygame.image.load("bedroom_phase0.png"), (Width, Height)
)

door_phases = [
    pygame.transform.scale(pygame.image.load("bedroom_phase1.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("bedroom_phase2.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("bedroom_phase3.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("bedroom_phase4.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("bedroom_phase5.png"), (Width, Height)),
]

# ─── Fonts 
ending = pygame.font.Font(None, 45)
title_font = pygame.font.Font(None, 140)
sub_font = pygame.font.Font(None, 50)

# ─── Constants 
PHASE_INTERVAL = 20.0   # seconds between each phase increase
REACTION_LIMIT = 10.0     # seconds player has to react

BUTTON_STYLE = dict(
    margin=10,
    radius=12,
    inactiveColour=(255, 255, 255),
    hoverColour=(200, 200, 200),
    pressedColour=(85, 85, 85),
    textColour=(20, 20, 20),
)

# ─── Game State 
door_phase = 0     
phase_timer = 0
reaction_timer = 0

game_over = False

# ─── Classes 
class Animatronic:
    def __init__(self, name, position):
        self.name = name
        self.position = position  # Starting Position

    def move(self):
        # Animatronic Movement
        pass

# ─── Animatronics
Tony = Animatronic("Tony", "Bedroom 3")
Cookie = Animatronic("Cookie", "Play Room")
GoldenHero = Animatronic("Golden Hero", "Bedroom 2")
Springson = Animatronic("Springson", "Backyard")
Toeneriette = Animatronic("Toeneriette", "Storage")

# ─── Buttons
def check_curtains():
    pass

def check_cameras():
    pass

def check_door():
    global door_phase, phase_timer, reaction_timer
    door_phase = 0
    phase_timer = 0
    reaction_timer = 0

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
    global door_phase, phase_timer, danger_timer, game_over

    run = True
    game_time = 0

    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

        dt = clock.get_time() / 1000
        game_time += dt

        screen.fill("black")

        if not game_over:
            if door_phase < 5:
                phase_timer += dt
                if phase_timer >= PHASE_INTERVAL:
                    door_phase += 1
                    phase_timer = 0

            if door_phase >= 5:
                reaction_timer += dt
                if reaction_timer >= REACTION_LIMIT:
                    game_over = True

            if game_time >= 360:
                run = False

        hours = 6 + int(game_time // 60)
        time_text = ending.render(f"{hours} AM", True, (255, 255, 255))
        screen.blit(time_text, (1190, 20))

        if game_over:
            over_text = title_font.render("GAME OVER", True, (200, 0, 0))
            screen.blit(over_text, (Width // 2 - 250, Height // 2 - 70))
        elif door_phase == 0:
            screen.blit(bedroom, (0, 0))
        else:
            screen.blit(door_phases[door_phase - 1], (0, 0))

        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()