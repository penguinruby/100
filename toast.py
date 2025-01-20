import pygame
import sys
import os

def resource_path(relative_path:str) -> str:
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class DraggToast:
    def __init__(self, width=800, height=800):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption("JAM TOAST")
        self.background_color = (0, 0, 0)
        self.gravity = 0.5
        self.dragging = True
        self.falling = True
        self.image_velocity = [0,0]

        self.image1 = pygame.image.load(resource_path("C:\\Users\\user\\Desktop\\python\\100\\ToastOnFloor.png"))
        self.image2 = pygame.image.load(resource_path("C:\\Users\\user\\Desktop\\python\\100\\Toast.png"))
        self.image3 = pygame.image.load(resource_path("C:\\Users\\user\\Desktop\\python\\100\\ToastFly.png"))

        self.image1 = pygame.transform.scale(
            self.image1,
            (int(self.image1.get_width()*0.6), int(self.image1.get_height()*0.6))
        )
        self.image2 = pygame.transform.scale(
            self.image2,
            (int(self.image2.get_width()*0.6), int(self.image2.get_height()*0.6))
        )
        self.image3 = pygame.transform.scale(
            self.image3,
            (int(self.image3.get_width()*0.6), int(self.image3.get_height()*0.6))
        )

        self.image_rect = self.image1.get_rect()
        self.image_rect.topleft =(100,100)


    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.image_rect.collidepoint(event.pos):
                        self.dragging = True
                        self.falling = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.dragging = False
                    self.falling = True
                elif event.type == pygame.MOUSEMOTION:
                    if self.dragging:
                        # self.image_rect.center = event.pos
                        x, y = event.pos
                        # 限制 x 和 y 的范围，使图像始终在窗口内
                        x = max(self.image_rect.width // 2, min(x, self.screen.get_width() - self.image_rect.width // 2))
                        y = max(self.image_rect.height//2 , min(y, self.screen.get_height() - self.image_rect.height//2 ))
                        self.image_rect.center = (x, y)


            if not self.dragging:
                self.image_velocity[1] += self.gravity
                self.image_rect = self.image_rect.move(self.image_velocity)
                if self.image_rect.bottom > self.screen.get_height():
                    self.image_rect.bottom = self.screen.get_height()
                    self.image_velocity[1] = 0
                    self.falling = False

            self.screen.fill(self.background_color)



            if  self.dragging:
                self.screen.blit(self.image2, self.image_rect)
            elif self.falling:
                self.screen.blit(self.image3, self.image_rect)
            else:
                self.screen.blit(self.image1, self.image_rect)
            
            pygame.display.flip()

        pygame.quit()
        sys.exit()





if __name__ =="__main__":
    game = DraggToast()
    game.run_game()

