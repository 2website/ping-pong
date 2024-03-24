from pygame import *


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


w = 1530
h = 800
back = "#64A8D1"
window = display.set_mode((w, h))
display.set_caption("Пинг-Понг")
window.fill(back)


sprite1 = Player('kirp.jpg', 10, 0, 40, 50, 100)
sprite2 = Player('kirp.jpg', 1300, 0, 40, 50, 100)
ball = GameSprite('ball.png', 600, 500, 40, 50, 50)


clock = time.Clock()
FPS = 60
game = True
speed_x = 3
speed_y = 3
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)
        sprite1.update_l()
        sprite2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 100:
            ball.rect.y -= speed_y


    sprite1.reset()
    sprite2.reset()
    ball.reset()
    ball.update()

    display.update()
    clock.tick(FPS)
