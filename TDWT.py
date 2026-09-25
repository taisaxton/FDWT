# THREE DAYS WITH TONY

# ─── Installations
# pip install pygame
# pip install pygame-widgets

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
bedroom = pygame.transform.scale(pygame.image.load("bedroom_phase0.png"), (Width, Height))
backyard = pygame.transform.scale(pygame.image.load("backyard_phase0.png"), (Width, Height))
camera_map = pygame.transform.scale(pygame.image.load("map.png"), (int(Width * 0.725), int(Height * 0.725)))

door_phases = [
    pygame.transform.scale(pygame.image.load("bedroom_phase1.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("bedroom_phase2.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("bedroom_phase3.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("bedroom_phase4.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("bedroom_phase5.png"), (Width, Height)),
]

curtain_phases = [
    pygame.transform.scale(pygame.image.load("backyard_phase1.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("backyard_phase2.png"), (Width, Height)),
    pygame.transform.scale(pygame.image.load("backyard_phase3.png"), (Width, Height)),
]

CAMERA_ROOMS = [
    {"name": "Play Room",  "rect": pygame.Rect(640, 110, 130, 100)},
    {"name": "Bedroom 2",  "rect": pygame.Rect(505, 200, 135, 140)},
    {"name": "Storage",    "rect": pygame.Rect(940, 215, 135, 125)},
]

viewing_cameras = False
current_camera = None

# ─── Constants
PHASE_INTERVAL = 15.0   # secs between each door phase increases
REACTION_LIMIT = 10.0   # secs player has to react once door phase hits max

click_times = []        # ingame time of door clicks
SPAM_WINDOW = 1.0        # secs considered a window of spam
SPAM_LIMIT = 3            # clicks allowed before considered spam

CURTAIN_INTERVAL = 15.0   # secs between curtain phase increases
WATCH_REQUIRED = 5.0      # secs of continuous watching needed to reset
CURTAIN_REACTION_LIMIT = 10.0   # secs player has once curtain hits max phase before losing

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
game_state = "menu"   # MENU --> PLAYING --> GAME_OVER

curtain_phase = 0
curtain_phase_timer = 0
curtain_reaction_timer = 0
watch_start = None      
viewing_curtains = False

# ─── Classes
class Animatronic:
    def __init__(self, name, position):
        self.name = name
        self.position = position 

    def move(self):
        pass

# ─── Animatronics
Tony = Animatronic("Tony", "Bedroom 3")
Cookie = Animatronic("Cookie", "Play Room")
GoldenHero = Animatronic("Golden Hero", "Bedroom 2")
Springson = Animatronic("Springson", "Backyard")
Toeneriette = Animatronic("Toeneriette", "Storage")

# ─── Functions
def hide_buttons():
    curtains.hide()
    cameras.hide()
    door.hide()
    restart.hide()

def check_curtains():
    global viewing_curtains, watch_start
    if game_state != "playing":
        return
    if viewing_cameras:   # can't check both at once
        return

    viewing_curtains = not viewing_curtains
    watch_start = None    # always clear on toggle, open or close

    if viewing_curtains:
        cameras.hide()
        door.hide()
    else:
        cameras.show()
        door.show()

def check_cameras():
    global viewing_cameras
    if game_state != "playing":
        return
    if viewing_curtains:  # can't check both at once
        return
    viewing_cameras = not viewing_cameras

    if viewing_cameras:
        curtains.hide()
        door.hide()
    else:
        curtains.show()
        door.show()

def check_door():
    global door_phase, phase_timer, reaction_timer, game_state, click_times

    if game_state != "playing":
        return

    click_times.append(game_time)
    click_times = [t for t in click_times if game_time - t <= SPAM_WINDOW]

    if len(click_times) >= SPAM_LIMIT:
        game_state = "game_over"
        hide_buttons()
        restart.show()
        return

    door_phase = 0
    phase_timer = 0
    reaction_timer = 0

def start_game():
    global game_state
    game_state = "playing"
    start.hide()
    curtains.show()
    cameras.show()
    door.show()

def restart_game():
    global door_phase, phase_timer, reaction_timer, game_time, game_state
    global click_times, curtain_phase, curtain_phase_timer, curtain_reaction_timer
    global watch_start, viewing_curtains, viewing_cameras

    door_phase = 0
    phase_timer = 0
    reaction_timer = 0
    game_time = 0
    click_times = []
    curtain_phase = 0
    curtain_phase_timer = 0
    curtain_reaction_timer = 0

    watch_start = None

    viewing_curtains = False
    viewing_cameras = False

    game_state = "menu"
    restart.hide()
    start.show()

# ─── Buttons
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

restart = Button(screen, 540, 570, 200, 75,
    text='Restart', fontSize=30,
    onRelease=restart_game, **BUTTON_STYLE)
restart.hide()

def main():
    global door_phase, phase_timer, reaction_timer, game_time, game_state
    global viewing_cameras, current_camera
    global curtain_phase, curtain_phase_timer, curtain_reaction_timer, watch_start, viewing_curtains
    run = True

    while run:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and viewing_cameras:
                for room in CAMERA_ROOMS:
                    if room["rect"].collidepoint(event.pos):
                        current_camera = room["name"]
                        break

        screen.fill("black")
        dt = clock.get_time() / 1000

        if game_state == "playing":
            game_time += dt

            if game_time >= 360:  # 6 Mins (6 AM --> 12 AM)
                game_state = "game_over"
                hide_buttons()
                restart.show()

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
                    restart.show()

            if curtain_phase < len(curtain_phases):
                curtain_phase_timer += dt
                if curtain_phase_timer >= CURTAIN_INTERVAL:
                    curtain_phase += 1
                    curtain_phase_timer = 0

            if curtain_phase >= len(curtain_phases):
                curtain_reaction_timer += dt
                if curtain_reaction_timer >= CURTAIN_REACTION_LIMIT:
                    game_state = "game_over"
                    hide_buttons()
                    restart.show()
            else:
                curtain_reaction_timer = 0

            if viewing_curtains and curtain_phase > 0:
                if watch_start is None:
                    watch_start = game_time
                elif game_time - watch_start >= WATCH_REQUIRED:
                    curtain_phase = 0
                    watch_start = None
                    viewing_curtains = False
                    cameras.show()
                    door.show()
            else:
                watch_start = None

        # display the main menu screen
        if game_state == "menu":
            title_text = title_font.render("Three Days With Tony", True, (255, 255, 255))
            screen.blit(title_text, (Width // 2 - title_text.get_width() // 2, 200))

            sub_text = sub_font.render("Survive...", True, (200, 200, 200))
            screen.blit(sub_text, (Width // 2 - sub_text.get_width() // 2, 340))

        # display the gameplay screen
        elif game_state == "playing":
            hours = 6 + int(game_time // 60)
            time_text = ending.render(f"{hours} AM", True, (255, 255, 255))
            screen.blit(time_text, (1190, 20))

            if viewing_cameras:
                screen.blit(camera_map, camera_map.get_rect(center=(Width // 2, Height // 2)))

                for room in CAMERA_ROOMS:
                    pygame.draw.rect(screen, (255, 0, 0), room["rect"], 2)

                if current_camera:
                    feed_text = sub_font.render(f"Viewing: {current_camera}", True, (255, 0, 0))
                    screen.blit(feed_text, (20, 20))
                else:
                    hint_text = sub_font.render("Click a camera location", True, (255, 0, 0))
                    screen.blit(hint_text, (20, 20))

            elif viewing_curtains:
                if curtain_phase == 0:
                    screen.blit(backyard, (0, 0))
                else:
                    screen.blit(curtain_phases[curtain_phase - 1], (0, 0))
                    elapsed = game_time - watch_start if watch_start is not None else 0
            
            else:
                if door_phase == 0:
                    screen.blit(bedroom, (0, 0))
                else:
                    screen.blit(door_phases[door_phase - 1], (0, 0))

        # display the game over screen
        elif game_state == "game_over":
            over_text = title_font.render("GAME OVER", True, (200, 0, 0))
            screen.blit(over_text, (Width // 2 - 250, Height // 2 - 70))

        pygame_widgets.update(events)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()