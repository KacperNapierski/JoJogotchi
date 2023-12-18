import pygame
from settings import *

class Button(pygame.sprite.Sprite):
    def __init__(self, text:str):

        #load spritesheet

        name_font = pygame.font.Font(None,50)
        self.name_text = name_font.render(text, False, (64,64,64))
        self.button_rect = self.name_text.get_rect(center = (WIDTH//4, HEIGHT*4//5))
