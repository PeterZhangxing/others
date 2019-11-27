import pygame


class MyBall(pygame.sprite.Sprite):

    def __init__(self,image_file,location,speed,screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.top,self.rect.left = location
        self.speed = speed
        self.screen = screen

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left <= 0 or self.rect.right >= self.screen.get_size()[0]:
            self.speed[0] = -self.speed[0]

pygame.init()

delay = 200
interval = 20
pygame.key.set_repeat(delay,interval)

screen = pygame.display.set_mode([640,480])
# print(screen.get_size())
backgroud = pygame.Surface(screen.get_size())
backgroud.fill([255,255,255])

clock = pygame.time.Clock()

image_file = "./images/bomb.png"
location = [15,15]
speed = [10,0]
myball = MyBall(image_file,location,speed,screen)

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                myball.rect.top -= 10
                if myball.rect.bottom <= 0:
                    myball.rect.top = screen.get_size()[1]
            if event.key == pygame.K_DOWN:
                myball.rect.top += 10
                if myball.rect.top >= screen.get_size()[1]:
                    myball.rect.bottom = 0

    clock.tick(30)
    screen.blit(backgroud,[0,0])

    myball.move()
    screen.blit(myball.image,myball.rect)

    pygame.display.flip()

pygame.quit()