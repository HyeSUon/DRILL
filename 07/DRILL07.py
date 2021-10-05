from pico2d import *
import random

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYUP and event.key == SDLK_ESCAPE:
            running = False
    pass
def hand_arrow_move():
    global dir_x, dir_y, x, y
    if y > hand_y:
          dir_y = -1
    elif y < hand_y:
        dir_y = 1
    else:
        dir_y = 0
    if x > hand_x:
        dir_x = -1
    elif x < hand_x:
        dir_x = 1
    else:
        dir_x = 0

def hand_random_move():
    global hand_x, hand_y, x, y
    if x > hand_x-5 and x < hand_x+5 and y > hand_y - 5 and hand_y < hand_y + 5:
        hand_x = random.randrange(100, 700)
        hand_y = random.randrange(100, 500)

open_canvas()
# fill here
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
running = True
x, y = 800 // 2, 600 // 2
frame = 0
dir_x = 0 # -1 left, +1 right
dir_y = 0
hand_x = random.randrange(100, 700)
hand_y = random.randrange(100, 500)
character_right = True

while running:
    clear_canvas()
    if x > hand_x - 5 and x < hand_x + 5:
        character_right = True
    elif x > hand_x:
        character_right = False
    else:
        character_right = True

    if character_right == True:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    hand.draw(hand_x, hand_y)
    update_canvas()
    handle_events()
    hand_arrow_move()
    hand_random_move()
    frame = (frame + 1) % 8
    x += dir_x*5
    y += dir_y*5
    delay(0.01)

close_canvas()




