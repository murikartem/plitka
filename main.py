import pygame
import sys
import os

current_path = os.path.dirname(__file__)
os.chdir(current_path)
pygame.init()
W = 1000
H = 800
screen = pygame.display.set_mode((W, H))
FPS = 60
clock = pygame.time.Clock()

image1 = pygame.image.load('data/image/on.png').convert_alpha()
image2 = pygame.image.load('data/image/da.png').convert_alpha()
image3 =pygame.image.load('data/image/p_2.png').convert_alpha()

plitka_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

list_player = []
NUM_HOD = 0
font = pygame.font.SysFont('Aria', 40)

maps_list = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

player_1 = Player(image2, 10, 10, 'AAAA')
player_group.add(player_1)
list_player.append(player_1)
player_2 = Player(image3, 610, 610, 'bbb')
player_group.add(player_2)
list_player.append(player_2)
list_player[0].hod = True







def game():
    screen.fill('grey')
    plitka_group.update()
    plitka_group.draw(screen)
    player_group.update()
    player_group.draw(screen)
    pygame.display.update()
class Player(pygame.sprite.Sprite):
    def __init__(self, image, x,y ,name):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hod = False
        self.step = False
        self.name = name

class Plitka(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image1
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.on = True
        self.adr = (self.rect.y // 100, self.rect.x // 100)


def drawmaps():
    for i in range(0, 7):
        for j in range(0, 7):
            x = 100 * i
            y = 100 * j
            pos = (x, y)
            plitka = Plitka(pos)
            plitka_group.add(plitka)

drawmaps()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game()

    clock.tick(FPS)
