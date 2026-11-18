import pygame
def draw_menu(window):
    window.fill('#211b2b')
    title = pygame.font.Font(None, 72).render('DungeonFall', True, '#f5e3c6')
    hint = pygame.font.Font(None, 30).render('Press Enter to start', True, '#c9b9d1')
    window.blit(title,title.get_rect(center = (480, 220)))
    window.blit(hint,hint.get_rect(center = (480, 300)))
