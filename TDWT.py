# ─── Imports
import random, sys
import pygame
import pygame_widgets
from pygame_widgets.button import Button

# ─── Pygame Setup 
pygame.init()
Width, Height = 1280, 720
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Three Days With Tony")
clock = pygame.time.Clock()
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# ─── Fonts 
ending = pygame.font.Font(None, 45)
title_font = pygame.font.Font(None, 140)
sub_font = pygame.font.Font(None, 50)

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

# ─── Constants 
PHASE_INTERVAL = 15.0   # seconds between each phase increase
REACTION_LIMIT = 10.0     # seconds player has to react

click_times = []       # ingame time of door clicks
SPAM_WINDOW = 1.0      # seconds considered a window of spam
SPAM_LIMIT = 3         # clicks allowed before considered spam

BUTTON_STYLE = dict(
    margin=10,
    radius=12,
    inactiveColour=(255, 255, 255),
    hoverColour=(200, 200, 200),
    pressedColour=(85, 85, 85),
    textColour=(20, 20, 20),
)

# ─── Game Details
door_phase = 0     
phase_timer = 0
reaction_timer = 0
game_time = 0   
game_state = "menu" # MENU --> PLAYING --> GAME_OVER

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
    global door_phase, phase_timer, reaction_timer, game_time, game_state, click_times

    if game_state != "playing":
        return

    click_times.append(game_time)
    click_times = [t for t in click_times if game_time - t <= SPAM_WINDOW]

    if len(click_times) >= SPAM_LIMIT:
        game_state = "game_over"
        curtains.hide()
        cameras.hide()
        door.hide()
        return

    door_phase = 0
    phase_timer = 0
    reaction_timer = 0

def hide_buttons():
    curtains.hide()
    cameras.hide()
    door.hide()

def start_game():
    global game_state
    game_state = "playing"
    start.hide()
    curtains.show()
    cameras.show()
    door.show()


curtains = Button(screen, 100, 570, 200, 75,
    text='Check Curtains', fontSize=30,
    onRelease=check_curtains, **BUTTON_STYLE)

cameras = Button(screen, 550, 570, 200, 75,
    text='Check Cameras', fontSize=30,
    onRelease=check_cameras, **BUTTON_STYLE)

door = Button(screen, 1000, 570, 200, 75,
    text='Close Door', fontSize=30,
    onRelease=check_door, **BUTTON_STYLE)

start = Button(screen, 540, 570, 200, 75,
    text='Start', fontSize=30,
    onRelease=start_game, **BUTTON_STYLE)

curtains.hide()
cameras.hide()
door.hide()


def main():
    global door_phase, phase_timer, reaction_timer, game_time, game_state
    run = True

    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

        screen.fill("black")
        dt = clock.get_time() / 1000

        if game_state == "playing":
            game_time += dt

        if door_phase < 5:
            phase_timer += dt
            if phase_timer >= PHASE_INTERVAL:
                door_phase += 1
                phase_timer = 0


        if door_phase >= 5:
            reaction_timer += dt
            if reaction_timer >= REACTION_LIMIT:
                game_state = "game_over"
                hide_buttons()

        # display the main menu screen
        if game_state == "menu":
            title_text = title_font.render("Three Days With Tony", True, (255, 255, 255)) # Header
            screen.blit(title_text, (Width // 2 - title_text.get_width() // 2, 200)) # Draw

            sub_text = sub_font.render("Survive...", True, (200, 200, 200)) # Sub-Header
            screen.blit(sub_text, (Width // 2 - sub_text.get_width() // 2, 340)) # Draw

        # display the gameplay screen
        elif game_state == "playing":
            hours = 6 + int(game_time // 60) # Calculate
            time_text = ending.render(f"{hours} AM", True, (255, 255, 255)) # Timer
            screen.blit(time_text, (1190, 20)) # Draw

            if door_phase == 0:
                screen.blit(bedroom, (0, 0)) # Draw Default
            else:
                screen.blit(door_phases[door_phase - 1], (0, 0)) # Draw Current

        # display the game over screen
        elif game_state == "game_over":
            over_text = title_font.render("GAME OVER", True, (200, 0, 0)) # Header
            screen.blit(over_text, (Width // 2 - 250, Height // 2 - 70)) # Draw

        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()