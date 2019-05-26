import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Top Down Shooter")

##########################

speed = 15
thing1 = 0
shooting1 = False
diretion1 = "none"
shootSpeed = 60
diretion2 = "none"
enemyDirition = "none"
enemyMinSpeed = 2
enemyMaxSpeed = 5
score = 0
bulletRadius = 15
lives = 5


#####################   sprite class   ###################

class sprite:
    def __init__(self, file, x, y):
        self.sprite = pygame.image.load(file)
        self.y = y
        self.x = x
        self.hitbox = (self.x, self.y, 60, 55)
        self.screen = pygame.display.set_mode((800, 600))
        self.health = 100

    def reduce_health(self, damage):
        self.health -= damage

    def blit(self):
        screen.blit(self.sprite, (self.x, self.y))

    def resize(self, w, h):
        self.sprite = pygame.transform.scale(self.sprite, (w, h))

    def rotate(self, deg):
        self.sprite = pygame.transform.rotate(self.sprite, deg)

    def drawHitBox(self):
        self.hitbox = (self.x, self.y, 60, 55)
        pygame.draw.rect(screen, (255, 255, 255), self.hitbox, 2)


#########################   enemy class   ##########################

class enemy:
    def __init__(self, x,y, sprite, how_many_hit_till_death, minSpeed, maxSpeed, hits = 0, isDied = False,):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.how_many_hit_till_death = how_many_hit_till_death
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed
        self.hits =  hits
        self.isDied = isDied

    def ranPos(self):
        self.x = random.randint(100, 700)
        self.y = 0

    def move(self,min,max):
        self.y += random.uniform(min, max)

    def hit(self):
        self.how_many_hit_till_death -= 1
        if self.hits > self.how_many_hit_till_death:
            self.isDied = True
            # put animation here later
            self.ranPos()
            print("score:")
            print(score)


#################   create sprites   ##########################

spritey_da_sprite = sprite("sprite.png", 400, 500)
spritey_da_sprite.resize(90, 85)

lazer1 = sprite("bullet.png", 0, 0)
lazer1.resize(bulletRadius * 2, bulletRadius * 2)

background = sprite("background.png", 0, 0)
background.resize(800, 600)

enemySprite1 = sprite("EMEMY.png", 400, 300)
enemySprite1.resize(60, 55)


enemySprite2 = sprite("EMEMY.png", 400, 300)
enemySprite2.resize(60, 55)

enemySprite3 = sprite("EMEMY.png", 400, 300)
enemySprite3.resize(60, 55)


enemySprite4 = sprite("EMEMY.png", 400, 300)
enemySprite4.resize(60, 55)


enemySprite5 = sprite("EMEMY.png", 400, 300)
enemySprite5.resize(60, 55)

##################   make the enemys   ##################

enemy1 = enemy(0,0,enemySprite1,1,enemyMinSpeed,enemyMaxSpeed,0,False)
enemy1.ranPos()

###################   loop   ########################

while 1:
    pygame.event.get()

    keys = pygame.key.get_pressed()

    if keys[100]:
        spritey_da_sprite.x = spritey_da_sprite.x + speed
        diretion1 = "right"
    if keys[97]:
        spritey_da_sprite.x = spritey_da_sprite.x - speed
        diretion1 = "left"
    if keys[115]:
        spritey_da_sprite.y = spritey_da_sprite.y + speed
        diretion1 = "up"
    if keys[119]:
        spritey_da_sprite.y = spritey_da_sprite.y - speed
        diretion1 = "down"
    if keys[pygame.K_q]:
        break

    if keys[pygame.K_RIGHT]:
        diretion1 = "right"
    if keys[pygame.K_LEFT]:
        diretion1 = "left"
    if keys[pygame.K_UP]:
        diretion1 = "down"
    if keys[pygame.K_DOWN]:
        diretion1 = "up"

    ##################   shooting   #####################

    if keys[pygame.K_SPACE]:
        thing1 = 0
        shooting1 = True

    if shooting1 == False:
        lazer1.x = spritey_da_sprite.x + 66.5
        lazer1.y = spritey_da_sprite.y + 5

    if shooting1 == True:
        lazer1.y -= shootSpeed


    if lazer1.x > 800 or lazer1.x < 0:
        shooting1 = False

    if lazer1.y > 600 or lazer1.y < 0:
        shooting1 = False

    ###################   colider   ###################

    if lazer1.y - bulletRadius < enemySprite1.hitbox[1] + enemySprite1.hitbox[3] and lazer1.y + bulletRadius > enemySprite1.hitbox[1]:
        if lazer1.x - bulletRadius > enemySprite1.hitbox[0] and lazer1.x - bulletRadius < enemySprite1.hitbox[0] + enemySprite1.hitbox[2]:
            enemy1.hit()
            enemyMinSpeed +=1
            enemyMaxSpeed +=1
            score +=1
            shooting1 = False

    ###################    enemy stuff    ######################

    enemy1.move(enemyMinSpeed,enemyMaxSpeed)
    if enemy1.y > 700:
        enemy1.y = 0
        enemy1.x = random.randint(100, 700)
        lives -=1
        print("lives:")
        print(lives)
    enemySprite1.x = enemy1.x
    enemySprite1.y = enemy1.y

    ###################   bliting and stuff   ######################
    if spritey_da_sprite.x > 750:
        spritey_da_sprite.x = 750
    elif spritey_da_sprite.x < -50:
        spritey_da_sprite.x = -50
    elif spritey_da_sprite.y > 550:
        spritey_da_sprite.y = 550
    elif spritey_da_sprite.y < -50:
        spritey_da_sprite.y = -50

    if lives == 0:
        print("YOUR FINAL SCORE IS:")
        print(score)
        break
    screen.fill((255, 255, 255))
    background.blit()
    spritey_da_sprite.blit()
    lazer1.blit()
    enemySprite1.blit()
    enemySprite1.drawHitBox()

    pygame.display.flip()

