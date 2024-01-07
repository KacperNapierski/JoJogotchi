import pygame
from settings import *
from random import randrange
from tools import *


class Poop(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.spritesheet = pygame.image.load('graphics/other/poop.png').convert_alpha()
        self.sprite_width = 64
        self.sprite_height = 64

        self.happiness_impact = [5,10,15,20]
        self.max_number = 4
        self.cleanliness_impact = [5, 10, 25, 50]


    def generate(self):
        bounds = {
            'upper': 500,
            'down': 650,
            'left': 300,
            'right': 550,
        }
        self.rect = self.spritesheet.get_rect(center = (randrange(bounds['left'],bounds['right']),(randrange(bounds['down'],bounds['upper']))))
        return self.spritesheet, self.rect


    