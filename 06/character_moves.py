from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
x = 0
y = 90
while ( x < 750):
     clear_canvas_now()
     grass.draw_now(400, 30)
     character.draw_now(x, y)
     x += 10
     delay(0.01)
while ( y < 550):
     clear_canvas_now()
     grass.draw_now(400, 30)
     character.draw_now(x, y)
     y += 10
     delay(0.01)
while ( x > 0):
     clear_canvas_now()
     grass.draw_now(400, 30)
     character.draw_now(x, y)
     x = x - 10
     delay(0.01)
while ( y > 90):
     clear_canvas_now()
     grass.draw_now(400, 30)
     character.draw_now(x, y)
     y = y - 10
     delay(0.01)


close_canvas()
