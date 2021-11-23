from pico2d import *

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SHIFT_DOWN, SHIFT_UP, DASH_TIMER = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    ((SDL_KEYDOWN, SDLK_LSHIFT) or (SDL_KEYDOWN, SDLK_RSHIFT)): SHIFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    ((SDL_KEYUP, SDLK_LSHIFT) or (SDL_KEYUP, SDLK_RSHIFT)): SHIFT_UP
}
table = {
    "WAKE": {"TIMER10": "WAKE", "WASD": "MOVE", "SHIFT": "WAKE", "N_WASD": "WAKE", "N_SHIFT": "WAKE"},
    "MOVE": {"TIMER10": "MOVE", "WASD": "MOVE", "SHIFT": "RUN", "N_WASD": "WAKE", "N_SHIFT": "MOVE"},
    "RUN": { "TIMER10": "MOVE", "WASD": "RUN", "SHIFT": "RUN", "N_WASD": "WAKE", "N_SHIFT": "MOVE"},
}


# Boy States
class DashState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.timer = 100
    def exit(boy, event):
        pass
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(DASH_TIMER)
        boy.x += boy.velocity*2
        boy.y = clamp(25, boy.y, 800-25)
    def draw(boy):
        if boy.velocity == 1:
             boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
             boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

class IdleState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
    def exit(boy, event):
            pass
    def do(boy):
        boy.timer -= 1
        boy.frame = (boy.frame + 1) % 8
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame*100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame*100, 200 ,100, 100, boy.x, boy.y)

class RunState:
     def enter(boy, event):
         if event == RIGHT_DOWN:
             boy.velocity += 1
         elif event == LEFT_DOWN:
             boy.velocity -= 1
         elif event == RIGHT_UP:
             boy.velocity -= 1
         elif event == LEFT_UP:
             boy.velocity += 1
         boy.dir = boy.velocity
     def exit(boy, event):
         pass
     def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.y = clamp(25, boy.y, 800-25)
     def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)
next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, SHIFT_UP: IdleState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SHIFT_DOWN: IdleState,
                (LEFT_DOWN, RIGHT_UP): RunState, (RIGHT_DOWN, LEFT_UP): RunState,
                },
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, SHIFT_UP: RunState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SHIFT_DOWN: DashState,
               },
    DashState: {LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SHIFT_DOWN: DashState,
                 LEFT_UP: IdleState, RIGHT_UP: IdleState, SHIFT_UP: RunState,
                DASH_TIMER: RunState}
}







class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
    def add_event(self, event):
        self.event_que.insert(0,event)
    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + '  Dir  ' + str(self.dir) + 'Timer :' + str(self.timer)
                    + '  State: ' + str(self.cur_state))
    def handle_event(self, event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


    def change_state(self,  state):
        # fill here
        pass

