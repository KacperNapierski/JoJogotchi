import pygame
from settings import *
from tools import *

class Button(pygame.sprite.Sprite):
    def __init__(self, action,  pos_x, pos_y):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.action = action
        self.spritesheet = pygame.image.load('graphics/UI/buttons.png').convert_alpha()
        self.sprite_width = 60
        self.sprite_height = 60
        self.index = 0
        self.animation_speed = 0.1
        self.countdown = 0
        self.scale = 1

        self.action_type = {
            'play':  [0,3],
            'feed':  [1,3],
            'clean': [2,3],
            'cure':  [3,3],
        }

        self.animation_dictionary = {
            'play':  [],
            'feed':  [],
            'clean': [],
            'cure':  [],
        }

        self.get_animation_dict()

    def get_animation_dict(self):
        self.sprite = SpriteSheet(
            self.spritesheet,
            self.sprite_width,
            self.sprite_height,
            self.action_type,
            self.animation_dictionary,
            self.scale
        )

    def animation_state(self, offset = 0):
        return self.sprite.animation_state(self.action, self.animation_speed, offset)
    #import sprite and animation just like jotaro

    def default_animation_state(self):
        self.index = 0
        return self.animation_dictionary[self.action][0]
    
    def animation_handler(self):
        if self.countdown > 0:
            surface = self.animation_state(offset=1)
            self.countdown -= 1
        else: surface = self.default_animation_state()
        rect = surface.get_rect(center = (self.pos_x,self.pos_y))
        return surface, rect

    ##TODO update funtion
    #def update(self):
    #    self.animation_handler()
