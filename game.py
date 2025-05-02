'''本项目于2025年4月19日，由谢泓黎建立，如果需要更改请保留声明'''
import pygame
import people
pygame.init()
size=500,500
color=(250,250,250)
screen=pygame.display.set_mode(size)
screen.fill(color)
pygame.display.set_caption("game")
a=people.people(screen)
i=0
