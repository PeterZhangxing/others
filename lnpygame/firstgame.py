import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

bg = pygame.image.load("images/background.png")
screen.blit(bg,(0,0))

hero = pygame.image.load("images/me1.png")
hero_rect = pygame.Rect(150, 300, 102, 126)
screen.blit(hero,hero_rect)

pygame.display.update()

myclock = pygame.time.Clock()

while True:

    myclock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit("exited the game")

    hero_rect.y -= 1
    if hero_rect.bottom <= 0:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero,hero_rect)
    pygame.display.update()