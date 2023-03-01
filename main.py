import pygame
import random

pygame.init()



def draw_bullet(x,y, dir):
    img = bullet

    match dir:
        case "siaure":
            img = pygame.transform.rotate(img, 0)
        case "pietus":
            img = pygame.transform.rotate(img, 180)
        case "rytai":
            img = pygame.transform.rotate(img, 270)
        case "vakarai":
            img = pygame.transform.rotate(img, 90)
    dis.blit(img, (x, y))




tank_speed = 10
bullet_speed = 40

clock = pygame.time.Clock()




width = 600
height = 400
size = 20


black = 0, 0, 0
green = 0, 255, 0
blue=(0,0,225)
red=(255,0,0)
yellow=(255,255,102)

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tanko zaidimas")

tankas = pygame.image.load("images.jpg")
tankas = pygame.transform.scale(tankas, (20,20))

enemy = pygame.image.load("enemy.jpg")
enemy = pygame.transform.scale(enemy, (20,20))

bg_img = pygame.image.load('download (2).jpg')
bg_img = pygame.transform.scale(bg_img, (600, 400))

bullet = pygame.image.load("bullet.jpg")
bullet = pygame.transform.scale(bullet, (20,20))

font_style = pygame.font.SysFont(None, 40)
score_font = pygame.font.SysFont("comicsansms", 16)
font = pygame.font.SysFont('Consolas', 30)

def tankas_dis(x, y):
    dis.blit(tankas, (x,y))

def enemy_dis(x, y):
    dis.blit(enemy, (x,y))

def your_score(score, shots, shots_kairen, shots_desinen, shots_pirmyn, shots_atgal):
    value = score_font.render("Taskai: " + str(score), True, yellow)
    value1 = score_font.render("Is viso suviu: " + str(shots), True, yellow)
    value2 = score_font.render("Suviai i vakarus: " + str(shots_kairen), True, yellow)
    value3 = score_font.render("Suviai i rytus: " + str(shots_desinen), True, yellow)
    value4 = score_font.render("Suviai i pietus: " + str(shots_atgal), True, yellow)
    value5 = score_font.render("Suviai i siaure: " + str(shots_pirmyn), True, yellow)

    dis.blit(value, [0,0])
    dis.blit(value1, [0,20])
    dis.blit(value2, [0,40])
    dis.blit(value3, [0,60])
    dis.blit(value4, [0,80])
    dis.blit(value5, [0,100])



def gameloop():
    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    bullet_x = x1
    bullet_y = y1

    taskai = 0
    suvis_siaure = 0
    suvis_rytus = 0
    suvis_vakarus = 0
    suvis_pietus = 0
    viso = 0
    direction = "siaure"
    bullet_dir = ""

    enemy_x = round(random.randrange(0, width - size) / 10.0) * 10.0
    enemy_y = round(random.randrange(0, height - size) / 10.0) * 10.0

    start_ticks = pygame.time.get_ticks()

    game_close = False
    run = True

    while run:
        dis.blit(bg_img, (0, 0))

        while game_close == True:
            loose = font_style.render("Time Over! Press Q - quit or C - play again", True, red)
            dis.fill(blue)
            dis.blit(loose, [width/16, height/2])
            your_score(taskai, viso, suvis_vakarus, suvis_rytus, suvis_siaure, suvis_pietus)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        run = False
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()

        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
        seconds_for_disp = font.render(str(seconds), True, yellow)
        # print(str(seconds))

        if seconds > 30:
            game_close=True
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close=True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                    direction = "vakarai"
                if event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                    direction = "rytai"
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                    direction = "siaure"
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10
                    direction = "pietus"
                if event.key == pygame.K_SPACE:

                    bullet_x = x1
                    bullet_y = y1
                    match direction:
                        case "siaure":
                            bullet_dir = "siaure"
                            viso += 1
                            suvis_siaure +=1
                        case "pietus":
                            bullet_dir = "pietus"
                            viso += 1
                            suvis_pietus += 1
                        case "rytai":
                            bullet_dir = "rytai"
                            viso += 1
                            suvis_rytus += 1
                        case "vakarai":
                            bullet_dir = "vakarai"
                            viso +=1
                            suvis_vakarus += 1
        if (x1<0 or x1>width or y1<0 or y1>height):
            game_close = True

        x1 += x1_change
        y1 += y1_change

        pygame.display.update()

        if bullet_x < 600 or bullet_y < 400 or bullet_x > 0 or bullet_y > 0:
            match bullet_dir:
                case "siaure":
                    bullet_y -= bullet_speed
                    draw_bullet(bullet_x, bullet_y, "siaure")

                case "pietus":
                    bullet_y += bullet_speed
                    draw_bullet(bullet_x, bullet_y, "pietus")
                case "rytai":
                    bullet_x += bullet_speed
                    draw_bullet(bullet_x, bullet_y, "rytai")
                case "vakarai":
                    bullet_x -= bullet_speed
                    draw_bullet(bullet_x, bullet_y, "vakarai")

        # if bullet_x == enemy_x and bullet_y == enemy_y: #or (x1 == enemy_x and y1 == enemy_y):
        #     enemy_x = round(random.randrange(0,width-size)/10)*10
        #     enemy_y = round(random.randrange(0,height-size)/10)*10
        #     taskai += 50

        if bullet_dir == "rytai" and bullet_x == enemy_x and (bullet_y - enemy_y < 5 or bullet_y-enemy_y > -5): #or (x1 == enemy_x and y1 == enemy_y):
            enemy_x = round(random.randrange(0, width-size)/10)*10
            enemy_y = round(random.randrange(0, height-size)/10)*10
            taskai += 50
        elif bullet_x == enemy_x and bullet_y == enemy_y or (x1 == enemy_x and y1 == enemy_y):
            enemy_x = round(random.randrange(0, width - size) / 10) * 10
            enemy_y = round(random.randrange(0, height - size) / 10) * 10
            taskai += 50
        elif bullet_dir == "vakarai" and bullet_x == enemy_x and (bullet_y - enemy_y < 5 or bullet_y - enemy_y > -5):
            enemy_x = round(random.randrange(0, width - size) / 10) * 10
            enemy_y = round(random.randrange(0, height - size) / 10) * 10
            taskai += 50
        elif bullet_dir == "siaure" and bullet_y == enemy_y and (bullet_x - enemy_x < 5 or bullet_x - enemy_x > -5):
            enemy_x = round(random.randrange(0, width - size) / 10) * 10
            enemy_y = round(random.randrange(0, height - size) / 10) * 10
            taskai += 50
        elif bullet_dir == "pietus" and bullet_y == enemy_y and (bullet_x - enemy_x < 5 or bullet_x - enemy_x > -5):
            enemy_x = round(random.randrange(0, width - size) / 10) * 10
            enemy_y = round(random.randrange(0, height - size) / 10) * 10
            taskai += 50

        tankas_dis(x1, y1)
        enemy_dis(enemy_x, enemy_y)

        dis.blit(seconds_for_disp, [width/2, 0])
        pygame.display.update()

        pygame.display.flip()
        clock.tick(tank_speed)

    pygame.quit()
    quit()




gameloop()

