from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < h - 85:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < h - 85:
            self.rect.y += self.speed


finish = False


class Ball(GameSprite):
    speed_x = randint(3, 6)
    speed_y = randint(3, 6)

    def update(self):
        global finish
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > h - 50 or self.rect.y < 0:
            self.speed_y *= -1 * randint(8,12)/10

        if sprite.collide_rect(sprite1, self) or sprite.collide_rect(sprite2, self):
            self.speed_x *= -1 * randint(8,12)/10

        if self.rect.x < 0:
            finish = True
            window.blit(win2, (700, 400))

        if self.rect.x > w:
            finish = True
            window.blit(win1, (700, 400))


w = 1530
h = 800
back = "#64A8D1"
window = display.set_mode((w, h))
display.set_caption("Пинг-Понг")
window.fill(back)

sprite1 = Player('kirp.jpg', 100, 0, 40, 5, 150)
sprite2 = Player('kirp.jpg', 1300, 0, 40, 5, 150)
ball = Ball('ball.png', 600, 500, 40, 50, 50)
ball2 = Ball('ball.png', 500, 400, 40, 50, 50)
ball2.speed_x *= -1

font.init()
font1 = font.Font(None, 35)
win1 = font1.render('PLAYER 1 WIN', True, (100, 0, 0))
win2 = font1.render('PLAYER 2 WIN', True, (100, 0, 0))
clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_r:
                ball.rect.x = 600
                ball.speed_x = randint(3, 6)
                ball2.rect.x = 500
                ball2.speed_x = -1 * ball.speed_x
                finish = False

    if not finish:
        window.fill(back)
        sprite1.update_l()
        sprite2.update_r()
        ball2.update()
        ball.update()
        sprite1.reset()
        sprite2.reset()
        ball.reset()
        ball2.reset()

    display.update()
    clock.tick(FPS)
