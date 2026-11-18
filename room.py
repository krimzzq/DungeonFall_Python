import pygame

def draw_room(window):
    window.fill("#211b2b")
    pygame.draw.rect(window, "#3c354b", (40, 40, 880, 460))
    pygame.draw.rect(window, "#85728f", (40, 40, 880, 460), 6)
    pygame.draw.rect(window, "#69536b", (260, 180, 80, 60))
    pygame.draw.rect(window, "#69536b", (620, 300, 80, 60))
