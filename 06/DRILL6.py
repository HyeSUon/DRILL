from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def Rec_move():
    x = 400
    y = 90
    while x < 780:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 5
        delay(0.01)
    while y < 560:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now( x, y)
        y += 5
        delay(0.01)
    while x > 0:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 5
        delay(0.01)
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 5
        delay(0.01)
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 5
        delay(0.01)
def Cir_move():
    cnt = -90
    x = 400
    y = 90
    while cnt < 270:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = 400 + math.cos(cnt / 360 * 2 * math.pi) * 360
        y = 300 + math.sin (cnt / 360 * 2 * math.pi) * 220
        cnt += 1
        delay(0.01)
while(True):
    Rec_move()
    Cir_move()

close_canvas()
