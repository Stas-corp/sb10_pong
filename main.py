from matplotlib.pyplot import spring
import pygame as pg
pg.init()
DISPLAY = WIN_WIDTH, WIN_HEIGHT = 800, 800
BG_COLOR = (200,200,200)

mw = pg.display.set_mode(DISPLAY)
pg.display.set_caption('PONG')

bg = pg.Surface(DISPLAY)
bg.fill(BG_COLOR)

clock = pg.time.Clock()
#'''''''''''''''''''''ClAsSI'''''''''''''''''''''
class Player(pg.sprite.Sprite):
    def __init__(self, image:str, x:int, y:int, width:int, height:int, speed:int):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self, key1, key2):
        keys = pg.key.get_pressed()
        if keys[key1] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[key2] and self.rect.y < WIN_WIDTH - self.rect.height:
            self.rect.y += self.speed

class Ball(Player):
    def __init__(self, image:str, x:int, y:int, width:int, height:int, speed:int):
        super().__init__(image, x, y, width, height, speed)
        self.xvel = speed
        self.yvel = speed

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel

        if self.rect.left <= 0:
            self.xvel *= -1
        if self.rect.right >= WIN_WIDTH:
            self.xvel *= -1

        if self.rect.top <= 0:
            self.yvel *= -1
        if self.rect.bottom >= WIN_HEIGHT:
            self.yvel *= -1

        if pg.sprite.collide_rect(RC1, ball):
            self.xvel *= -1
        if pg.sprite.collide_rect(ball, RC2):
            self.xvel *= -1

#'''''''''''''''''''''Главний цикл'''''''''''''''''''''''''
RC1 = Player('rc.png', 15 ,WIN_HEIGHT/2 - 53, 16, 106, 7)
RC2 = Player('rc.png', WIN_WIDTH - 31, WIN_HEIGHT/2 - 53, 16, 106, 7)
ball = Ball('ball.png', 300, 400, 32, 32, 3)

FPS = 60
game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
    mw.blit(bg, (0,0))
    mw.blit(RC1.image, (RC1.rect.x, RC1.rect.y))
    mw.blit(RC2.image, (RC2.rect.x, RC2.rect.y))
    mw.blit(ball.image, (ball.rect.x, ball.rect.y))
    RC1.update(pg.K_w, pg.K_s)
    RC2.update(pg.K_UP, pg.K_DOWN)
    ball.update()

    pg.display.update()
    clock.tick(FPS)