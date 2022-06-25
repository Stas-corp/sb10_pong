import pygame as pg
pg.init()
DISPLAY = WIN_WIDTH, WIN_HEIGHT = 800, 800
BG_COLOR = (200,200,200)
mw = pg.display.set_mode(DISPLAY)
pg.display.set_caption('PONG')

bg = pg.Surface(DISPLAY)
bg.fill(BG_COLOR)

clock = pg.time.Clock()
#'''''''''''''''''''''ClAsSI''''''''''''''''''''''''''''''''
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

RC1 = Player('rc.png', 15 ,WIN_HEIGHT/2 - 53, 16, 106, 7)

#'''''''''''''''''''''Главний цикл'''''''''''''''''''''''''
FPS = 60
game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
    mw.blit(bg, (0,0))
    mw.blit(RC1.image, (RC1.rect.x, RC1.rect.y))
    RC1.update(pg.K_w, pg.K_s)

    pg.display.update()
    clock.tick(FPS)