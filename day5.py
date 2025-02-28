import pygame
from copy import deepcopy
from random import choice, randrange
import time

W, H =10,20
TILE = 45
GAME_RES= W * TILE, H * TILE
FPS = 60


pygame.init()
game_sc = pygame.display.set_mode(GAME_RES)
clock =pygame.time.Clock()

grid = [pygame.Rect( x*TILE, y*TILE, TILE, TILE) for x in range(W) for y in range(H)]

figures_pos =[[(-1,0),(-2,0),(0,0),(1,0)],
              [(0,-1),(-1,-1),(-1,0),(0,0)],
              [(-1,0),(-1,1),(0,0),(0,-1)],
              [(0,0),(-1,0),(0,1),(-1,-1)],
              [(0,0),(0,-1),(0,1),(-1,-1)],
              [(0,0),(0,-1),(0,1),(-1,-1)],  #[4] 影片說改 1 -1
              [(0,0),(0,-1),(0,1),(-1,0)]]

figures = [[pygame.Rect( x+W//2, y+1 ,1,1) for x,y in fig_pos] for fig_pos in figures_pos]
figure_rect = pygame.Rect(0, 0, TILE-2, TILE-2)
field =[[0 for i in range(W)] for j in range(H)]

#speed是下降的速度
anim_count, anim_speed, anim_limit = 0, 10, 2000
figure = deepcopy(choice(figures))

#最後結束的色彩
get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))
color = get_color()

#檢查邊界
def check_borders():
    if figure[i].x < 0 or figure[i].x > W-1:
        return False
    elif figure[i].y > H-1 or field[figure[i].y][figure[i].x]:
        return False
    return True


#重來
def reset_game():
    global field, figure, color, anim_count, anim_limit
    field = [[0 for _ in range(W)] for _ in range(H)]
    figure = deepcopy(choice(figures))
    color = get_color()
    anim_count = 0
    anim_limit = 2000



while True:
    dx , rotate= 0, False
    game_sc.fill(pygame.Color("black"))
#control  ok
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                anim_limit = 100
            elif event.key == pygame.K_UP:
                rotate = True


#move x ok
    figure_old = deepcopy(figure)
    for i in range(4):
        figure[i].x += dx
        if not check_borders():
            figure = deepcopy(figure_old)
            break
#move y ok
    anim_count += anim_speed
    if anim_count > anim_limit:
        anim_count = 0
        figure_old = deepcopy(figure)
        for i in range(4):
            figure[i].y += 1
            if not check_borders():
                for i in range(4):
                    field[figure_old[i].y][figure_old[i].x] = pygame.Color("white")
                figure = deepcopy(choice(figures))
                anim_limit = 2000
                break

#rotate
    center = figure[0]
    figure_old = deepcopy(figure)
    if rotate:
        for i in range(4):
            x = figure[i].y - center.y
            y = figure[i].x - center.x
            figure[i].x = center.x- x
            figure[i].y = center.y+ y
            if not check_borders():
                figure = deepcopy(figure_old)
                break

#check lines
    line = H-1
    for row in range(H-1 , -1, -1):
        count = 0
        for i in range (W):
            if field[row][i]:
                count += 1
            field[line][i] = field[row][i]
        if count < W:
            line -= 1


#draw grid
    [pygame.draw.rect(game_sc,(40,40,40), i_rect ,1) for i_rect in grid]
#draw figure
    for i in range(4):
        figure_rect.x = figure[i].x * TILE
        figure_rect.y = figure[i].y * TILE
        pygame.draw.rect(game_sc, pygame.Color("White"),figure_rect)

    #draw field
    for y, raw in enumerate(field):
        for x, col in enumerate(raw):
            if col:
                figure_rect.x, figure_rect.y = x*TILE, y*TILE
                pygame.draw.rect(game_sc, col, figure_rect)
    

    #game over
    for i in range(W):
        if field[0][i]:
            field =[[0 for i in range(W) for i in range(H)]]
            for i_rect in grid:
                pygame.draw.rect(game_sc, get_color(), i_rect)
                pygame.display.flip()
                clock.tick(200)

            time.sleep(2)  # Pause for a moment
            reset_game()  # Restart the game


    pygame.display.flip()
    clock.tick()