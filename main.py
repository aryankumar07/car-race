import pygame
import time
import math
from utils import scale_image,scale_image_diiferent_factor,blit_rotate_center

#  IMAGES PATH  AND CONSTANTS

TRACK = scale_image(pygame.image.load('imgs/track.png'), 0.8)
GRASS = scale_image(pygame.image.load('imgs/grass.jpg'), 2.5)
GREEN_CAR = scale_image_diiferent_factor(pygame.image.load('imgs/green-car.png'), 0.32, 1)
RED_CAR= scale_image_diiferent_factor(pygame.image.load('imgs/red-car.png'), 0.32, 1)
TRACK_BORDER = scale_image(pygame.image.load('imgs/track-border.png'),0.8)
FINISH = pygame.image.load('imgs/finish.png')
FPS = 60


class AbstractCar:

    def __init__(self, max_velocity, max_rotation):
        self.max_val = max_velocity
        self.val = 0
        self.rotation_val = max_rotation
        self.angle = 180
        self.img = self.IMG
        self.x,self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self,left=False,right=False):
        if left:
            self.angle += self.rotation_val
        elif right:
            self.angle -=  self.rotation_val

    def draw(self, screen):
        blit_rotate_center(screen, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        val = int(self.max_val)
        if self.val + self.acceleration <= val:
            self.val = self.val + self.acceleration
        else:
            self.val = val
        # self.val  = min(self.val+self.acceleration, self.max_val)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = self.val*math.cos(radians)
        horizontal = self.val*math.sin(radians)
        self.y -= vertical
        self.x -= horizontal

    def retard(self):
        self.val = max(self.val-self.acceleration/2, 0)
        self.move()
class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (135, 200)

WIDTH = TRACK.get_width()
HEIGHT = TRACK.get_height()

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('CAR RACING')

clock = pygame.time.Clock()

images = [
    (GRASS,(0,0)),
    (TRACK,(0,0)),
]

player_car = PlayerCar(4, 4)

def draw(images,screen, player_car):
    for img, pos in images:
        screen.blit(img, pos)

    player_car.draw(screen)
    pygame.display.update()



run = True
while run:
    clock.tick(FPS)
    draw(images, screen, player_car)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    elif keys[pygame.K_d]:
        player_car.rotate(right=True)
    elif keys[pygame.K_w]:
        moved = True
        player_car.move_forward()

    if not moved:
        player_car.retard()

pygame.quit()