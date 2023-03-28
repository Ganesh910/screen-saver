import pygame
import sys

pygame.init()

info = pygame.display.Info()
width, height = info.current_w, info.current_h

screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("Arial", 72)

text = "Pandey G"
x=-500
y = height//2

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x+=5
    if x>width:
        x=-500
    screen.fill((255, 255, 255))
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (x, y))
    pygame.display.update()

    clock.tick(60)
