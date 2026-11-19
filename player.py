import pygame


def move_player(position, keys, dt):
    direction = pygame.Vector2(
        int(keys[pygame.K_d]) - int(keys[pygame.K_a]),
        int(keys[pygame.K_s]) - int(keys[pygame.K_w]),
    )
    if direction.length_squared() > 0:
        position = position + direction.normalize() * 200 * dt
    return position
