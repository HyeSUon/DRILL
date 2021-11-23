from pico2d import *
import random
Ball_Number = 20
# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
class Ball:
    def __init__(self):
        if(random.randint(1,2) % 2):
            self.Big = False
            self.image = load_image('ball21x21.png')
        else:
            self.Big = True
            self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100, 700), 599
        self.sp = random.randint(1, 10)
    def draw(self):
         self.image.draw(self.x, self.y)

    def update(self):
        if(self.y**2 < 71**2):
            if(self.Big):
                self.y = 70
            else:
                self.y = 60
        else:
            self.y -= self.sp


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
grass = Grass()
balls = [ Ball() for i in range(Ball_Number)]
running = True
# game main loop code
while running:
    handle_events()
    for ball in balls:
        ball.update()
    #game logic

    #game drawing
    clear_canvas()
    grass.draw()
    for ball in balls:
        ball.draw()

    update_canvas()
# finalization code