from pico2d import *
import os

os.chdir('C:\\Users\\PC\\Desktop\\python\\drill05\\2DGP-DRILL5')

open_canvas()
backg = load_image('TUK_GROUND.png')
character = load_image('bear_sheet.png')

running = True

def handle_events():
    global running, x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: #esc르면 꺼지기
            running = False
        #오른쪽 누르는 동안 오른쪽 이동 @끝 벽에 닿으면 이동 X
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x += 1
        #왼쪽 누르는 동안 왼쪽 이동
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                x -= 1
        #위 누르는 동안 위로 이동
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP
                y += 1
        #아래 누르는 동안 아래 이동
        


while running:
    clear_canvas()

    pass

close_canvas()

