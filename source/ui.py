import pygame
from settings import *

class Button(pygame.sprite.Sprite):
    def __init__(self, text:str):

        #load spritesheet

        name_font = pygame.font.Font(None,50)
        #self.name_text = name_font.render(text, False, (64,64,64))
        #self.button_rect = self.name_text.get_rect(center = (WIDTH//4, HEIGHT*4//5))

        self.spritesheet = pygame.image.load('').convert_alpha()
        self.sprite_width = 200
        self.sprite_height = 230
        self.index = 0
        self.scale = 1

        self.action_type = {
            'click': [0,3]
        }

        self.animation_dictionary = {
            'click': []
        }

        self.animation_speed = 0.1

    #import sprite and animation just like jotaro