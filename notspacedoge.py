import pygame
import time
import random
pygame.font.init()



WIDTH, HEIGHT = 1000, 800   #視窗大小
WIN =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Not The Space Dodge")

BG = pygame.image.load("bg.JPG")
PLAYER_WIDTH = 20  #物件大小
PLAYER_HEIGHT = 30

PLAYER_VEL=3  #移動距離
FONT = pygame.font.SysFont("comicsans", 30)

STAR_WIDTH=10
STAR_HEIGHT=10
STAR_VEL=20



def draw(player, elapsed_time, stars):
    WIN.blit(BG,(0, 0))

    time_txt = FONT.render(f" Time:{round(elapsed_time)}s", 1, "white")
    WIN.blit(time_txt, (10,10))  #計時的字體大小

    for star in stars:
        pygame.draw.rect(WIN, "white" , star)

    pygame.draw.rect(WIN, (255, 0, 155), player) #物件顏色
    pygame.display.update()



def main():
    run = True

    player =pygame.Rect(200, HEIGHT -PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock =pygame.time.Clock()

    start_time =time.time()
    elapsed_time =0

    star_add_incr =30  #下降的速度
    star_count = 0

    stars =[]
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        #掉下來的物件
        if star_count > star_add_incr:
            for _ in range(10):  #一次有多少物件下來
                star_x =random.randint(0,WIDTH-STAR_WIDTH)
                star =pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)


            star_add_incr = max(200, star_add_incr-50)
            star_count =0


        #開關視窗
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run= False
                break


        keys = pygame.key.get_pressed()
        #物件移動範圍，如何移動
        if keys[  pygame.K_LEFT] and player.x- PLAYER_VEL >=0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x+ PLAYER_VEL +player.width <= WIDTH:
            player.x += PLAYER_VEL

        
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star. height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit =True
                break
        
        if hit:
            lost_txt = FONT. render("Loser!", 1, "white")
            WIN.blit(lost_txt, (WIDTH/2 - lost_txt.get_width()/2, HEIGHT/2-lost_txt.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

 

        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__ =="__main__":
    main()


