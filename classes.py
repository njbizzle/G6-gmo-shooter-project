import pygame
import random

screen = pygame.display.set_mode((800, 600))


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


#####################   player class   ############################

class player:
    def __init__(self, sprite, x, y):
        self.sprite = sprite
        self.x = x
        self.y = y
        # TODO(3) make sprite class, coment power ups for later, but put all the movement and stuff in the class [Push to GitHub!]


#################   enemy class   ##########################

class enemy:
    def __init__(self, x, y, sprite, how_many_hit_till_death, minSpeed, maxSpeed, hits=0, isDied=False, ):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.how_many_hit_till_death = how_many_hit_till_death
        self.minSpeed = minSpeed
        self.maxSpeed = maxSpeed
        self.hits = hits
        self.isDied = isDied
        self.hitbox = (self.x, self.y, 60, 55)

    def ranPos(self):
        self.x = random.randint(100, 700)
        self.y = 0

    def move(self, min, max):
        self.y += random.uniform(min, max)

    def hit(self):
        self.how_many_hit_till_death -= 1
        if self.hits > self.how_many_hit_till_death:
            self.isDied = True
            # put animation here later
            self.ranPos()
            print("score:")
            print(score)

    def colider(self, x, y, bulletRadius):
        if y - bulletRadius < self.hitbox[1] + self.hitbox[3] and y + bulletRadius > self.hitbox[1]:
            if x - bulletRadius > self.hitbox[0] and x - bulletRadius < self.hitbox[0] + self.hitbox[2]:
                return True
