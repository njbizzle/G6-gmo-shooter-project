import pygame
import random

screen = pygame.display.set_mode((800, 600))


#####################   sprite class   ###################

class sprite:
    def __init__(self, file, x, y):
        self.sprite = pygame.image.load(file)
        self.y = y
        self.x = x
        self.screen = pygame.display.set_mode((800, 600))
        self.health = 100
        self.rect = pygame.Rect((x, y), self.sprite.get_size())

    def blit(self):
        screen.blit(self.sprite, (self.x, self.y))

    def resize(self, w, h):
        self.sprite = pygame.transform.scale(self.sprite, (w, h))

    def rotate(self, deg):
        self.sprite = pygame.transform.rotate(self.sprite, deg)

    def drawHitBox(self):
        self.rect = pygame.Rect((self.x, self.y), self.sprite.get_size())
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


#####################   player class   ############################

class player(sprite):
    def __init__(self, file, x, y):
        sprite.__init__(self, file, x, y)
        self.x = x
        self.y = y

    def move(self, speed):
        keys = pygame.key.get_pressed()
        if keys[100]:
            self.x = self.x + speed
        if keys[97]:
            self.x = self.x - speed
        if keys[115]:
            self.y = self.y + speed
        if keys[119]:
            self.y = self.y - speed

    def reduce_health(self, damage):
        self.health -= damage

    def drawPlayerHitBox(self):
        self.rect = pygame.Rect((self.x + 10, self.y), self.sprite.get_size())
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


#################   enemy class   ##########################

class enemy(sprite):
    def __init__(self, file, x, y, how_many_hit_till_death, minSpeed, maxSpeed, hits=0, ):
        sprite.__init__(self, file, x, y)
        self.x = x
        self.y = y
        self.how_many_hit_till_death = how_many_hit_till_death
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed
        self.hits = hits
        self.isDied = False

    def ranPos(self):
        self.x = random.randint(100, 700)
        self.y = 0

    def move(self, min, max):
        self.y += random.uniform(min, max)

    def hit(self):
        self.how_many_hit_till_death -= 1
        if self.hits > self.how_many_hit_till_death:
            self.isDied = True
            # put animation here laterd
            self.ranPos()
            print("score:")
            return True
