from pico2d import *
import os

os.chdir('C:\\Users\\PC\\Desktop\\python\\drill05\\2DGP-DRILL5')

open_canvas()
backg = load_image('TUK_GROUND.png')
character1 = load_image('run1.png')
character2 = load_image('run2.png')

running = True
x = 800 // 2  # 시작 위치 x
y = 600 // 2  # 시작 위치 y
frame = 0
dir1 = 0
dir2 = 0

def move_right():
    global x
    x = min(800, x + 5)  # 오른쪽 끝을 넘지 않도록 함


def move_left():
    global x
    x = max(0, x - 5)  # 왼쪽 끝을 넘지 않도록 함


def move_up():
    global y
    y = min(600, y + 5)  # 위쪽 끝을 넘지 않도록 함


def move_down():
    global y
    y = max(0, y - 5)  # 아래쪽 끝을 넘지 않도록 함


def handle_events():
    global running, dir1, dir2
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:  # ESC 누르면 종료
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir1 += 1  # 오른쪽 이동
            elif event.key == SDLK_LEFT:
                dir1 -= 1  # 왼쪽 이동
            elif event.key == SDLK_UP:
                dir2 += 1  # 위쪽 이동
            elif event.key == SDLK_DOWN:
                dir2 -= 1  # 아래쪽 이동
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT or event.key == SDLK_LEFT:
                dir1 = 0  # 키를 떼면 이동 멈춤
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                dir2 = 0  # 키를 떼면 이동 멈춤


while running:
    clear_canvas()
    backg.draw(400, 300)  # 배경 그리기
    character1.clip_draw(frame * 100, 0, 86, 200, x, y, 200, 200)

    if dir1 > 0 and dir2 > 0:  # 오른쪽 위 대각선 이동
        character1.clip_draw(frame * 100, 0, 100, 200, x, y, 200, 200)
        move_right()
        move_up()
    elif dir1 > 0 and dir2 < 0:  # 오른쪽 아래 대각선 이동
        character1.clip_draw(frame * 100, 0, 100, 200, x, y, 200, 200)
        move_right()
        move_down()
    elif dir1 < 0 and dir2 > 0:  # 왼쪽 위 대각선 이동
        character2.clip_draw(frame * 100, 0, 100, 200, x, y, 200, 200)
        move_left()
        move_up()
    elif dir1 < 0 and dir2 < 0:  # 왼쪽 아래 대각선 이동
        character2.clip_draw(frame * 100, 0, 100, 200, x, y, 200, 200)
        move_left()
        move_down()
    if dir1 > 0:
        clear_canvas()
        backg.draw(400, 300)
        move_right()
        character1.clip_draw(frame * 100, 0, 86, 200, x, y, 200, 200)
    elif dir1 < 0:
        clear_canvas()
        backg.draw(400, 300)
        move_left()
        character2.clip_draw(frame * 100, 0, 84, 200, x, y, 200, 200)
    update_canvas()
    handle_events()

    if dir2 > 0:
        move_up()
    elif dir2 < 0:
        move_down()

    frame = (frame + 1) % 8
    x += dir1 * 10
    y += dir2 * 10
    delay(0.1)

close_canvas()