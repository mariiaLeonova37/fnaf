
import random
import sys
from random import randint

from pygame import *

window = display.set_mode((1000, 500))
display.set_caption("Fnaf")

class GameSprite(sprite.Sprite):
    def __init__(self, file_name, size_x, size_y, pos_x, pos_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(file_name), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def __init__(self, filename, size_x, size_y, pos_x, pos_y, speed):
        super().__init__(filename, size_x, size_y, pos_x, pos_y, speed)
        self.active = True
    def update(self):
        if self.active:
            coord = [[120,120],[120,290],[800,290],[800,120],[460,120],[465,390]]
            coord_choice = random.choice(coord)
            time.wait(1000)
            self.rect.x = coord_choice[0]
            self.rect.y = coord_choice[1]


class Wall(sprite.Sprite):
    def __init__(self, size_y, size_x, pos_x, pos_y, color1, color2, color3):
        super().__init__()
        self.image = Surface ((size_y, size_x))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.visible = True

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

background = transform.scale(image.load ('roar.jpeg'), (1000, 500))
wall1 = Wall(200, 50, 410, 215, 190,0, 255)
wall3 = Wall(50, 200, 635, 260, 190,0, 255)
wall2 = Wall(50, 200, 310, 260, 190,0, 255)
player = GameSprite('play.png', 70, 70, 465, 390, 0)
enemy = Enemy('animatronik.png', 70, 80, 460, 120, 1)

coords = [[120,120],[120,290],[800,290],[800,120],[460,120],[465,390]]
walls = sprite.Group()
walls.add(wall1)
#doors.add(wall3)
#doors.add(wall2)

font.init()
timer = 100
gameOver = False
font = font.Font(None, 100)
win = font.render("YOU WON!!", True, (255, 255, 255))
loose = font.render("LOOSE!!", True, (255, 255, 255))
clock = time.Clock()
while True:

    posit = random.choice(coords)

    window.blit(background,(0,0))
    player.update()
    player.draw()
    enemy.update()
    enemy.draw()
    timer -= 1
    if wall1.visible:
        wall1.reset()
    wall2.reset()
    wall3.reset()
    if timer <= 0 and not gameOver:
        window.blit(win, (250, 250))
        enemy.active = False

    for e in event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if wall1.visible:
                    wall1.visible = False
                else:
                    wall1.visible = True
    if not wall1.visible:
        if enemy.rect.x == 465 and enemy.rect.y == 390:
            gameOver = True
    if gameOver:
        window.blit(loose, (250, 250))
        enemy.active = False


    clock.tick(60)
    display.update()
