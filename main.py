import pygame


def main():
    pygame.init()
    window = pygame.display.set_mode((960, 540))
    pygame.display.set_caption("Dungeonfall")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill("#211b2b")
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
