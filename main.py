'''''''''''''''''''''
#####################
'''''''''''''''''''''

gameName = "Name of the Game"

'''''''''''''''''''''
#####################
'''''''''''''''''''''

import pygame
import random
from classes import sprite
from classes import player
from classes import enemy
import time


pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Top Down Shooter")


############ todos ##################


############  variabeles  ##############

start_time = time.time()
fps = 30
speed = 15
thing1 = 0
shooting1 = False
shootSpeed = 60
enemyDirition = "none"
enemyMinSpeed = 2
enemyMaxSpeed = 5
score = 0
bulletRadius = 15
lives = 5
resetLazer = False
onScreen1 = True
onScreen2 = False
onScreen3 = False
onScreen4 = False
onScreen5 = False
startButtonPressed = False
startButtonHovered = False
clock = pygame.time.Clock()
the_time = round(time.time() - start_time)
time_left = 101 - the_time
change = 0.1
toxic = 0

#################   create sprites   ######################

spritey_da_sprite = player("sprite.png", 400, 300)
spritey_da_sprite.resize(90, 85)
lazer1 = sprite("bullet.png", 0, 0)
lazer1.resize(bulletRadius * 2, bulletRadius * 2)
background = sprite("background.png", 0, 0)
background.resize(800, 600)
enemy1 = enemy("gmo.png", 0, 0, 1, enemyMinSpeed, enemyMaxSpeed)
enemy1.resize(70, 70)
enemy1.ranPos()
enemy2 = enemy("gmo.png", 0, 0, 1, enemyMinSpeed, enemyMaxSpeed)
enemy2.resize(70, 70)
enemy3 = enemy("gmo.png", 0, 0, 1, enemyMinSpeed, enemyMaxSpeed)
enemy3.resize(70, 70)
enemy4 = enemy("gmo.png", 0, 0, 1, enemyMinSpeed, enemyMaxSpeed)
enemy4.resize(70, 70)
enemy5 = enemy("gmo.png", 0, 0, 1, enemyMinSpeed, enemyMaxSpeed)
enemy5.resize(70, 70)
startButton = sprite("startButton.png", 275, 300)
startButton.resize(272, 120)
startButtonlight = sprite("startButtonLight.png", 275, 300)
startButtonlight.resize(272, 120)
startBackgound = sprite("startBackground.png", 0, 0)
startBackgound.resize(800, 600)
deadBackgound = sprite("game over.png", 0, 0)
deadBackgound.resize(800, 600)
########################  text display ###########################

font = pygame.font.Font('freesansbold.ttf', 20)
bigFont = pygame.font.Font('freesansbold.ttf', 70)
midFont = pygame.font.Font("freesansbold.ttf", 50)


def gameOver(toxic, died):
    gameOverText = bigFont.render('Game Over', True, (0, 0, 0))
    if toxic > -1 and toxic < 1:
        finalScoreText = font.render('Your farm is Extremely Healthy With no GMO', True, (0, 0, 0))
    elif toxic > 1 and toxic < 6:
        finalScoreText = font.render('Your farm is good with little GMO', True, (0, 0, 0))
    elif toxic > 6 and toxic < 10:
        finalScoreText = font.render('Your farm is kind of toxic', True, (0, 0, 0))
    elif toxic > 10 and toxic < 15:
        finalScoreText = font.render('Your farm is toxic', True, (0, 0, 0))
    elif toxic > 15:
        finalScoreText = font.render('Your farm is SUPER toxic', True, (0, 0, 0))
    else:
        finalScoreText = font.render("weeeeeeeeeeeeeee", True, (0, 0, 0))
    deadBackgound.blit()
    screen.blit(gameOverText, (200, 250))
    screen.blit(finalScoreText, (300, 350))

#########################   game loop   ################################

while 1:

    time_left = 20 - the_time
    the_time = round(time.time() - start_time)
    timeText = font.render("Time: " + str(time_left), True, (0, 0, 0))
    pygame.event.get()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_q]:
        break

    #######################  start   #########################

    if not startButtonPressed:
        if keys[pygame.K_SPACE]:
            startButtonPressed = True

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 275 + 272 > mouse[1] > 275 and 300 + 120 > mouse[1] > 300:
            startButtonHovered = True
            if click[0] == 1:
                time.sleep(0.1)
                startButtonPressed = True
        else:
            startButtonHovered = False

        screen.fill((255, 255, 255))
        startText = bigFont.render(gameName, True, (0, 0, 0))
        startBackgound.blit()
        screen.blit(startText, (100, 150))

        if startButtonHovered == True:
            startButtonlight.blit()
        elif startButtonHovered == False:
            startButton.blit()

        pygame.draw.rect(screen, (255, 255, 255), (275, 300, 272, 120), 3)

        pygame.display.flip()

    else:

        spritey_da_sprite.move(speed)

        ##################   shooting   #####################

        if keys[pygame.K_SPACE]:
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

        if resetLazer == True:
            shooting1 = False

        ###################   colider   ###################

        if enemy1.rect.colliderect(lazer1.rect):
            if enemy1.hit():
                score += 1
                enemyMinSpeed += change
                enemyMaxSpeed += change
                change -= 0.02

        if enemy2.rect.colliderect(lazer1.rect):
            if enemy2.hit():
                score += 1
                enemyMinSpeed += change
                enemyMaxSpeed += change
                change -= 0.02

        if enemy3.rect.colliderect(lazer1.rect):
            if enemy3.hit():
                score += 1
                enemyMinSpeed += change
                enemyMaxSpeed += change
                change -= 0.02

        if enemy4.rect.colliderect(lazer1.rect):
            if enemy4.hit():
                score += 1
                enemyMinSpeed += change
                enemyMaxSpeed += change
                change -= 0.02

        if enemy5.rect.colliderect(lazer1.rect):
            if enemy5.hit():
                score += 1
                enemyMinSpeed += change
                enemyMaxSpeed += change
                change -= 0.02

        if spritey_da_sprite.rect.colliderect(enemy1.rect):
            lives = 0
            isGameOver = True
        if spritey_da_sprite.rect.colliderect(enemy2.rect):
            lives = 0
            isGameOver = True
        if spritey_da_sprite.rect.colliderect(enemy3.rect):
            lives = 0
            isGameOver = True
        if spritey_da_sprite.rect.colliderect(enemy4.rect):
            lives = 0
            isGameOver = True
        if spritey_da_sprite.rect.colliderect(enemy5.rect):
            lives = 0
            isGameOver = True

        ###################    enemy stuff    #####################

        if onScreen1:
            enemy1.move(enemyMinSpeed, enemyMaxSpeed)
        if enemy1.y > 700 and onScreen1 == True:
            enemy1.y = 0
            enemy1.x = random.randint(100, 700)
            toxic += 1
        if not onScreen1:
            enemy1.ranPos()

        if onScreen2:
            enemy2.move(enemyMinSpeed, enemyMaxSpeed)
        if enemy2.y > 700 and onScreen2 == True:
            enemy2.y = 0
            enemy2.x = random.randint(100, 700)
            toxic += 1
        if not onScreen2:
            enemy2.ranPos()

        if onScreen3:
            enemy3.move(enemyMinSpeed, enemyMaxSpeed)
        if enemy3.y > 700 and onScreen3 == True:
            enemy3.y = 0
            enemy3.x = random.randint(100, 700)
            toxic += 1
        if not onScreen3:
            enemy3.ranPos()

        if onScreen4:
            enemy4.move(enemyMinSpeed, enemyMaxSpeed)
        if enemy4.y > 700 and onScreen4 == True:
            enemy4.y = 0
            enemy4.x = random.randint(100, 700)
            toxic += 1
        if not onScreen4:
            enemy4.ranPos()

        if onScreen5:
            enemy5.move(enemyMinSpeed, enemyMaxSpeed)
        if enemy5.y > 700 and onScreen5 == True:
            enemy5.y = 0
            enemy5.x = random.randint(100, 700)
            toxic += 1
        if not onScreen5:
            enemy5.ranPos()
        ###################   bliting and stuff   ######################

        if change < 0.1:
            change = 0.1

        clock.tick(fps)

        if spritey_da_sprite.x > 750:
            spritey_da_sprite.x = 750
        elif spritey_da_sprite.x < -50:
            spritey_da_sprite.x = -50
        elif spritey_da_sprite.y > 550:
            spritey_da_sprite.y = 550
        elif spritey_da_sprite.y < -50:
            spritey_da_sprite.y = -50

        screen.fill((255, 255, 255))
        background.blit()
        spritey_da_sprite.blit()
        lazer1.blit()

        enemy1.blit()
        enemy1.drawHitBox()
        onScreen1 = True

        if score > 5:
            onScreen2 = True
            enemy2.blit()
            enemy2.drawHitBox()

        if score > 10:
            onScreen3 = True
            enemy3.blit()
            enemy3.drawHitBox()

        if score > 15:
            onScreen4 = True
            enemy4.blit()
            enemy4.drawHitBox()

        if score > 20:
            onScreen5 = True
            enemy5.blit()
            enemy5.drawHitBox()

        lazer1.drawHitBox()
        spritey_da_sprite.drawPlayerHitBox()

        scoreText = font.render('Score: ' + str(score), True, (0, 0, 0))

        screen.blit(scoreText, (670, 10))
        screen.blit(timeText, (670, 30))

    if lives == 0:
        onScreen5 = False
        onScreen4 = False
        onScreen3 = False
        onScreen2 = False
        onScreen1 = False
        screen.fill((255, 255, 255))
        gameOver(toxic, True)

    if time_left == 0:
        onScreen5 = False
        onScreen4 = False
        onScreen3 = False
        onScreen2 = False
        onScreen1 = False
        screen.fill((255, 255, 255))
        gameOver(toxic, False)

    print(lives)
    pygame.display.flip()

# # # # # # #
#           #
#           #
#           #
#           #
# # # # # # #
