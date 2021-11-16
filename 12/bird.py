import game_framework
from pico2d import *
from ball import Ball
import random
import game_world

# 홍관조의 크기는 19cm이다. 홍관조 19c
# 1픽셀에 3센티미터이므로 7픽셀 크기가 된다.
# 참새의 시속은 29~40키로 평균 35키로이다.
# 1초당 15회의 날갯짓을 한다. 즉 0.067초에 한번씩 날갯짓을 한다.

# bird Run Speed
PIXEL_PER_METER = (100.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 35.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.067
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y, self.velocity = random.randint(100, 1500-1), random.randint(100, 700), RUN_SPEED_PPS
        self.frame = 14
        if(random.randint(1,2) % 2):
            self.velocity *= -1

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        if self.x < 25 or self.x > 1600 - 25:
            self.velocity *= -1
