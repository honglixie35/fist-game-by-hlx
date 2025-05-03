import pygame
class people:
    num=0
    a=pygame.image.load("picture/1.png")
    def __init__(self,screen):
        self.num+=1
        aa=self.a.get_rect()
        screen.blit(self.a,(0,0),aa)
        pygame.display.flip()
