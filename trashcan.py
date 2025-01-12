import pygame
import sys
import random
import math

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" No trash here")
clock = pygame.time.Clock()

can_back_raw = pygame.image.load("C:\\Users\\user\\Desktop\\python\\100\\trash_can_back.png").convert_alpha()
can_front_raw = pygame.image.load("C:\\Users\\user\\Desktop\\python\\100\\trash_can_front.png").convert_alpha()
garbage_raw = pygame.image.load("C:\\Users\\user\\Desktop\\python\\100\\images.png").convert_alpha()

SCALE_CAN = 0.4
SCALE_GARBAGE = 0.25

def scale_image(img, scale):
    w = int(img.get_width() * scale)
    h = int(img.get_height() * scale)
    return pygame.transform.scale(img, (w,h))

can_back = scale_image(can_back_raw, SCALE_CAN)
can_front = scale_image(can_front_raw, SCALE_CAN)
garbage_img = scale_image(garbage_raw, SCALE_GARBAGE)

can_w, can_h = can_back.get_width(), can_back.get_height()
garbage_h, garbage_w = garbage_img.get_height(), garbage_img.get_width()

can_x =(WIDTH - can_w) // 2
can_y = HEIGHT - can_h

garbage_x = can_x - garbage_w -30
garbage_y = HEIGHT - garbage_h

darggin = False
vx, vy =0 , 0

inside_can = False

GRAVITY = 0.4 #重力
FRICTION =0.98 #阻力
BOUNCE_WALL = -0.5 #與螢幕邊界碰撞的反彈係數

def collide_with_can(x, y):
    can_cx = can_x + can_w //2
    can_cy = can_y + can_h //2
    g_cx = x + garbage_w // 2
    g_cy = y + garbage_h //2
    dist_sq =(can_cx -g_cx)**2 + (can_cy - g_cy)**2
    return dist_sq < 60**2

runnning = True
while runnning:
    clock.tick (60)
    for event in pygame.event. get():
        if event.type == pygame.QUIT:
            runnning = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            gx = garbage_x + garbage_w //2
            gy = garbage_y + garbage_h //2
            if (mx -gx)**2 +(my-gy)**2 < (garbage_w //2)**2:
                darggin = True
                vx = vy =0

        elif event.type == pygame.MOUSEBUTTONUP:
            darggin = False
        
        elif event.type == pygame.MOUSEMOTION and darggin:
            mx, my = event.pos
            garbage_x = mx - garbage_w //2
            garbage_y = my - garbage_h//2

    if not darggin:
        if not inside_can:
            if collide_with_can(garbage_x, garbage_y):
                inside_can = True

        vy += GRAVITY
        vx *=FRICTION
        vy *=FRICTION

        garbage_x += vx
        garbage_y += vy

        if inside_can:
            inside_can = False
            garbage_y = can_y - garbage_h
            angle = random.uniform(45, 135)
            speed = random. uniform(12 ,18)
            vx = speed *math.cos(math.radians(angle))
            vy = -speed* math.sin(math.radians(angle))

        if garbage_y > HEIGHT -garbage_h:
            garbage_y =HEIGHT -garbage_h
            vy *= BOUNCE_WALL
        if garbage_x <0:
            garbage_x = 0
            vx *= BOUNCE_WALL
        elif garbage_x > WIDTH - garbage_w:
            garbage_x = WIDTH - garbage_w
            vx *= BOUNCE_WALL


    screen.fill((220, 220, 220))
    screen.blit(can_back, (can_x, can_y))
    screen.blit(garbage_img, (garbage_x, garbage_y))
    screen.blit(can_front, (can_x, can_y))
    pygame.display.flip()


pygame.quit()
sys.exit()



