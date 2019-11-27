import pygame
import random

class MyBall(pygame.sprite.Sprite):

    def __init__(self,image_file,speed,location,screen,myscore):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.top,self.rect.left = location
        self.speed = speed
        self.myscore = myscore

    def move(self):
        # global score,score_surf,score_font

        self.rect = self.rect.move(self.speed)
        if self.rect.left <= 0 or self.rect.right >= self.screen.get_rect().right:
            self.speed[0] = -self.speed[0]

        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            self.myscore.score += 1
            self.myscore.score_surf = self.myscore.score_font.render(str(self.myscore.score),1,(0,0,0))


class MyFont(object):

    def __init__(self,score,myfsize=50,score_pos=[10,10]):
        self.score = score
        self.score_font = pygame.font.Font(None, myfsize)
        self.score_surf = self.score_font.render(str(score), 1, (0, 0, 0))
        self.score_pos = score_pos


class MyPaddle(pygame.sprite.Sprite):

    def __init__(self,location=[0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,20])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


pygame.init()
screen = pygame.display.set_mode([640,480])
clock = pygame.time.Clock()

# score = 0
# score_font = pygame.font.Font(None,50)
# score_surf = score_font.render(str(score),1,(0,0,0))
# score_pos = [10,10]
myscore = MyFont(score=0)

myBall = MyBall('images/bullet1.png', [10,5], [50, 50],screen,myscore)
ball_group = pygame.sprite.Group()
ball_group.add(myBall)

mypaddle = MyPaddle([270,430])

live = 3
done = False
flag = True
while flag:
    clock.tick(30)
    screen.fill([255,255,255])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.MOUSEMOTION:
            mypaddle.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(mypaddle,ball_group,False):
        # myBall.speed[1] = -myBall.speed[1]
        myBall.speed[1] = (-myBall.speed[1])/myBall.speed[1] * random.choice([3,5,10,15])
        myBall.speed[0] = (-myBall.speed[0])/myBall.speed[0] * random.choice([6,10,15,20])
        # print(myBall.speed)

    # myBall.move()

    if not done:
        myBall.move()
        for i in range(0,live):
            screen.blit(myBall.image, [screen.get_rect().width - 40 * i, 20])

        screen.blit(myBall.image,myBall.rect)
        screen.blit(mypaddle.image,mypaddle.rect)
        screen.blit(myscore.score_surf, myscore.score_pos)

        pygame.display.flip()

    if myBall.rect.top >= screen.get_rect().bottom:
        live -= 1
        if live == 0:
            final_text1 = "Game Over"
            final_text2 = "Your final score is: " + str(myscore.score)

            # ft1_font = pygame.font.Font(None, 70)
            # ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))
            #
            # ft2_font = pygame.font.Font(None, 50)
            # ft2_surf = ft2_font.render(final_text2, 1, (0, 0, 0))

            ft1_obj = MyFont(final_text1,70)
            ft2_obj = MyFont(final_text2,50)

            screen.blit(ft1_obj.score_surf,[screen.get_rect().width/2 - ft1_obj.score_surf.get_width()/2,100])
            screen.blit(ft2_obj.score_surf,[screen.get_rect().width/2 - ft2_obj.score_surf.get_width()/2,200])

            done = True
            pygame.display.flip()
        else:
            pygame.time.delay(1000)
            myBall.rect.topleft = [50,50]

pygame.quit()