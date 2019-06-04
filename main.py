'''''''''''''''''''''
#####################
'''''''''''''''''''''

gameName = ""

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

gametime = 30
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
isGameOver = False
stop = False
is_cow1_sick = False
is_cow2_sick = False
is_cow3_sick = False
is_cow4_sick = False
is_cow5_sick = False
cow1_dead = False
cow2_dead = False
cow3_dead = False
cow4_dead = False
cow5_dead = False
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
winBackgound = sprite("win screen.png", 0, 0)
winBackgound.resize(800, 600)
cow1 = sprite("cow.png", 400, 300)
cow1.resize(92, 52)
sickCow1 = sprite("sickcow.png", 400, 300)
sickCow1.resize(92, 52)
cow2 = sprite("cow.png", 400, 300)
cow2.resize(92, 52)
sickCow2 = sprite("sickcow.png", 400, 300)
sickCow2.resize(92, 52)
cow3 = sprite("cow.png", 400, 300)
cow3.resize(92, 52)
sickCow3 = sprite("sickcow.png", 400, 300)
sickCow3.resize(92, 52)
cow4 = sprite("cow.png", 400, 300)
cow4.resize(92, 52)
sickCow4 = sprite("sickcow.png", 400, 300)
sickCow4.resize(92, 52)
cow5 = sprite("cow.png", 400, 300)
cow5.resize(92, 52)
sickCow5 = sprite("sickcow.png", 400, 300)
sickCow5.resize(92, 52)

cow1.x = random.randint(100, 700)
cow1.y = random.randint(300, 500)

cow2.x = random.randint(100, 700)
cow2.y = random.randint(300, 500)

cow3.x = random.randint(100, 700)
cow3.y = random.randint(300, 500)

cow4.x = random.randint(100, 700)
cow4.y = random.randint(300, 500)

cow5.x = random.randint(100, 700)
cow5.y = random.randint(300, 500)

######################## game over and  text display ###########################

font = pygame.font.Font('freesansbold.ttf', 20)
bigFont = pygame.font.Font('freesansbold.ttf', 70)
midFont = pygame.font.Font("freesansbold.ttf", 50)


def gameOver(toxic, died):
    isToxic = False

    if died:
        deadBackgound.blit()
        gameOverText = bigFont.render('Game Over', True, (0, 0, 0))
        screen.blit(gameOverText, (200, 300))

    elif not died:

        winBackgound.blit()

        if toxic > -1 and toxic < 1:
            finalScoreText = font.render('Your farm is Extremely Healthy with no GMO', True, (0, 0, 0))
            screen.blit(finalScoreText, (190, 350))
            isToxic = False

        elif toxic > 0 and toxic < 3:
            finalScoreText = font.render('Your farm is OK with little GMO', True, (0, 0, 0))
            screen.blit(finalScoreText, (235, 350))
            isToxic = False

        elif toxic > 2 and toxic < 7:
            finalScoreText = font.render('Your farm is kind of toxic', True, (0, 30, 0))
            screen.blit(finalScoreText, (270, 350))
            isToxic = True

        elif toxic > 6 and toxic < 10:
            finalScoreText = font.render('Your farm is toxic', True, (0, 100, 0))
            screen.blit(finalScoreText, (310, 350))
            isToxic = True

        elif toxic > 10:
            finalScoreText = font.render('Your farm is SUPER toxic', True, (0, 200, 0))
            screen.blit(finalScoreText, (280, 350))
            isToxic = True

        if isToxic == True:
            gameOverText = bigFont.render('You Win-ish', True, (0, 0, 0))
        elif isToxic == False:
            gameOverText = bigFont.render('You Win', True, (0, 0, 0))
        screen.blit(gameOverText, (270, 250))

        cowDeaths = []

        if cow1_dead:
            cowDeaths.append(1)
        if cow2_dead:
            cowDeaths.append(1)
        if cow3_dead:
            cowDeaths.append(1)
        if cow4_dead:
            cowDeaths.append(1)
        if cow5_dead:
            cowDeaths.append(1)
        cowDeathSum = sum(cowDeaths)
        cowDeathText = font.render("Cows Dead: " + str(cowDeathSum), True, (0, 0, 0))

        sickCows = []

        if is_cow1_sick:
            sickCows.append(1)
        if is_cow2_sick:
            sickCows.append(1)
        if is_cow3_sick:
            sickCows.append(1)
        if is_cow4_sick:
            sickCows.append(1)
        if is_cow4_sick:
            sickCows.append(1)

        sickCowSum = sum(sickCows)
        sickCowsText = font.render("Cows Sick: " + str(sickCowSum), True, (0, 0, 0))

        screen.blit(sickCowsText, (350, 390))
        screen.blit(cowDeathText, (350, 420))

#########################   game loop   ################################

while 1:

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
        time_left = gametime + 1 - the_time

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

        ###################    cow colider   ########################

        if enemy1.rect.colliderect(cow1.rect) and not is_cow1_sick:
            enemy1.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow1_sick = True
        elif enemy1.rect.colliderect(cow1.rect) and is_cow1_sick:
            enemy1.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow1_dead = True

        if enemy2.rect.colliderect(cow1.rect) and not is_cow1_sick:
            enemy2.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow1_sick = True
        elif enemy2.rect.colliderect(cow1.rect) and is_cow1_sick:
            enemy2.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow1_dead = True

        if enemy3.rect.colliderect(cow1.rect) and not is_cow1_sick:
            enemy3.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow1_sick = True
        elif enemy3.rect.colliderect(cow1.rect) and is_cow1_sick:
            enemy3.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow1_dead = True

        if enemy4.rect.colliderect(cow1.rect) and not is_cow1_sick:
            enemy4.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow1_sick = True
        elif enemy4.rect.colliderect(cow1.rect) and is_cow1_sick:
            enemy4.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow1_dead = True

        if enemy5.rect.colliderect(cow1.rect) and not is_cow1_sick:
            enemy5.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow1_sick = True
        elif enemy5.rect.colliderect(cow1.rect) and is_cow1_sick:
            enemy5.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow1_dead = True
        '''
        '''
        if enemy1.rect.colliderect(cow2.rect) and not is_cow2_sick:
            enemy1.hit()
            score += 1
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow2_sick = True
        elif enemy1.rect.colliderect(cow2.rect) and is_cow2_sick:
            enemy1.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow2_dead = True

        if enemy2.rect.colliderect(cow2.rect) and not is_cow2_sick:
            enemy2.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow2_sick = True
        elif enemy2.rect.colliderect(cow2.rect) and is_cow2_sick:
            enemy2.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow2_dead = True

        if enemy3.rect.colliderect(cow2.rect) and not is_cow2_sick:
            enemy3.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow2_sick = True
        elif enemy3.rect.colliderect(cow2.rect) and is_cow2_sick:
            enemy3.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow2_dead = True

        if enemy4.rect.colliderect(cow2.rect) and not is_cow2_sick:
            enemy4.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow2_sick = True
        elif enemy4.rect.colliderect(cow2.rect) and is_cow2_sick:
            enemy4.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow2_dead = True

        if enemy5.rect.colliderect(cow2.rect) and not is_cow2_sick:
            enemy5.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow2_sick = True
        elif enemy5.rect.colliderect(cow2.rect) and is_cow2_sick:
            enemy5.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow2_dead = True
        '''
        '''
        if enemy1.rect.colliderect(cow3.rect) and not is_cow3_sick:
            enemy1.hit()
            score += 1
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow3_sick = True
        elif enemy1.rect.colliderect(cow3.rect) and is_cow3_sick:
            enemy1.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow3_dead = True

        if enemy2.rect.colliderect(cow3.rect) and not is_cow3_sick:
            enemy2.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow3_sick = True
        elif enemy2.rect.colliderect(cow3.rect) and is_cow3_sick:
            enemy2.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow3_dead = True

        if enemy3.rect.colliderect(cow3.rect) and not is_cow3_sick:
            enemy3.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow3_sick = True
        elif enemy3.rect.colliderect(cow3.rect) and is_cow3_sick:
            enemy3.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow3_dead = True

        if enemy4.rect.colliderect(cow3.rect) and not is_cow3_sick:
            enemy4.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow3_sick = True
        elif enemy4.rect.colliderect(cow3.rect) and is_cow3_sick:
            enemy4.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow3_dead = True

        if enemy5.rect.colliderect(cow3.rect) and not is_cow3_sick:
            enemy5.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow3_sick = True
        elif enemy5.rect.colliderect(cow3.rect) and is_cow3_sick:
            enemy5.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow3_dead = True
        '''
        '''
        if enemy1.rect.colliderect(cow4.rect) and not is_cow4_sick:
            enemy1.hit()
            score += 1
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow4_sick = True
        elif enemy1.rect.colliderect(cow4.rect) and is_cow4_sick:
            enemy1.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow4_dead = True

        if enemy2.rect.colliderect(cow4.rect) and not is_cow4_sick:
            enemy2.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow4_sick = True
        elif enemy2.rect.colliderect(cow4.rect) and is_cow4_sick:
            enemy2.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow4_dead = True

        if enemy3.rect.colliderect(cow4.rect) and not is_cow4_sick:
            enemy3.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow4_sick = True
        elif enemy3.rect.colliderect(cow4.rect) and is_cow4_sick:
            enemy3.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow4_dead = True

        if enemy4.rect.colliderect(cow4.rect) and not is_cow4_sick:
            enemy4.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow4_sick = True
        elif enemy4.rect.colliderect(cow4.rect) and is_cow4_sick:
            enemy4.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow4_dead = True

        if enemy5.rect.colliderect(cow4.rect) and not is_cow4_sick:
            enemy5.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow4_sick = True
        elif enemy5.rect.colliderect(cow4.rect) and is_cow4_sick:
            enemy5.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow4_dead = True
        '''
        '''
        if enemy1.rect.colliderect(cow5.rect) and not is_cow5_sick:
            enemy1.hit()
            score += 1
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow5_sick = True
        elif enemy1.rect.colliderect(cow5.rect) and is_cow5_sick:
            enemy1.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow5_dead = True

        if enemy2.rect.colliderect(cow5.rect) and not is_cow5_sick:
            enemy2.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow5_sick = True
        elif enemy2.rect.colliderect(cow5.rect) and is_cow5_sick:
            enemy2.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow5_dead = True

        if enemy3.rect.colliderect(cow5.rect) and not is_cow5_sick:
            enemy3.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow5_sick = True
        elif enemy5.rect.colliderect(cow5.rect) and is_cow5_sick:
            enemy3.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow5_dead = True

        if enemy4.rect.colliderect(cow5.rect) and not is_cow5_sick:
            enemy4.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow5_sick = True
        elif enemy5.rect.colliderect(cow5.rect) and is_cow5_sick:
            enemy4.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow5_dead = True

        if enemy5.rect.colliderect(cow5.rect) and not is_cow5_sick:
            enemy5.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            is_cow5_sick = True
        elif enemy5.rect.colliderect(cow5.rect) and is_cow5_sick:
            enemy5.hit()
            enemyMinSpeed += change
            enemyMaxSpeed += change
            change -= 0.02
            cow5_dead = True
        ################   player colider  #####################

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
        ###################  cows ###############################

        sickCow1.x = cow1.x
        sickCow1.y = cow1.y

        sickCow2.x = cow2.x
        sickCow2.y = cow2.y

        sickCow3.x = cow3.x
        sickCow3.y = cow3.y

        sickCow4.x = cow4.x
        sickCow4.y = cow4.y

        sickCow5.x = cow5.x
        sickCow5.y = cow5.y

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

        if change < 0.1:
            change = 0.1

        clock.tick(fps)

        if not cow1_dead:
            if not is_cow1_sick:
                cow1.blit()
                cow1.drawHitBox()
            else:
                sickCow1.blit()
                cow1.drawHitBox()
        else:
            cow1.x = 10000
            sickCow1.x = 10000
            cow1.drawHitBox()
            is_cow1_sick = False

        if not cow2_dead:
            if not is_cow2_sick:
                cow2.blit()
                cow2.drawHitBox()
            else:
                sickCow2.blit()
                cow2.drawHitBox()
        else:
            cow2.x = 10000
            sickCow2.x = 10000
            cow2.drawHitBox()
            is_cow2_sick = False

        if not cow3_dead:
            if not is_cow3_sick:
                cow3.blit()
                cow3.drawHitBox()
            else:
                sickCow3.blit()
                cow3.drawHitBox()
        else:
            cow3.x = 10000
            sickCow3.x = 10000
            cow3.drawHitBox()
            is_cow3_sick = False

        if not cow4_dead:
            if not is_cow4_sick:
                cow4.blit()
                cow4.drawHitBox()
            else:
                sickCow4.blit()
                cow4.drawHitBox()
        else:
            cow4.x = 10000
            sickCow4.x = 10000
            cow4.drawHitBox()
            is_cow4_sick = False

        if not cow5_dead:
            if not is_cow5_sick:
                cow5.blit()
                cow5.drawHitBox()
            else:
                sickCow5.blit()
                cow5.drawHitBox()
        else:
            cow5.x = 10000
            sickCow5.x = 10000
            cow5.drawHitBox()
            is_cow5_sick = False

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

    if lives == 0 and stop == False:
        onScreen5 = False
        onScreen4 = False
        onScreen3 = False
        onScreen2 = False
        onScreen1 = False
        screen.fill((255, 255, 255))
        gameOver(toxic, True)
        time_left = 1

    if time_left < 0:
        stop = True
        onScreen5 = False
        onScreen4 = False
        onScreen3 = False
        onScreen2 = False
        onScreen1 = False
        screen.fill((255, 255, 255))
        gameOver(toxic, False)

    pygame.display.flip()

# # # # # # #
#           #
#           #
#           #
#           #
# # # # # # #
