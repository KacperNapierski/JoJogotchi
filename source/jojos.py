import pygame
from pygame.sprite import Group
from settings import *
from tools import *

#TODO
#[ ] hides all variables of classes inside functions
#[ ] create a group and operate only on functions

class JoJo(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        #basic stats
        self.name = ''
        self.age = 0
        self.cleanliness = 100
        self.hunger = 100
        self.happiness = 100
        self.money_generation_rate = 1
        self.physiological_need = 0.0

        #actions
        self.pets_avaliable = 3

        #animations
        self.spritesheet = ''
        self.sprite_width = 200
        self.sprite_height = 230
        self.animation_frame = 0
        self.animation_speed = 0.03
        self.scale = 1
        self.action_type = {}
        self.animation_dictionary = {}
        


    def aging(self):
        self.age += 1
        # evoluton -> change health and physiololg etc.

    def play(self):
        ...
    
    def pet(self):
            #TODO 
            #[ ]animation
            #[ ] Jotaro anoyence -> happiness lower
            #[ ]limit usage
        if self.happiness < 98 and self.pets_avaliable:
            self.happiness += 2
            self.pets_avaliable -= 1
        else: ...

    def poop():
        ...
    
    def apply_needs(self):
        self.hunger -= 3
        self.happiness -= 5
        #TODO when poop exist change for poop
        self.physiological_need += 0.01
        if self.physiological_need == 1:
            self.cleanliness -= 10
        else: self.cleanliness -=2
        
        self.pets_avaliable = 3

    def animation_state(self):
        ...

    def played(self):
        ...

    def update(self):
        #self.apply_needs()
        self.play()
        #self.animation_state()

    def get_animation_dict(self):
        self.sprite = SpriteSheet(
            self.spritesheet,
            self.sprite_width,
            self.sprite_height,
            self.action_type,
            self.animation_dictionary,
            self.scale
        )


class Jotaro(JoJo):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Jotaro'
        self.spritesheet = pygame.image.load('graphics/Jotaro/jotaro_cute_x10.png').convert_alpha()


        self.action_type = {
            #action_name: level on spritesheet, number of frames
            'walking':       [0,4],
            "petting":       [1,1],
            "smoking":       [2,6],
            'walking_dirty': [3,4],
            "petting_dirty": [4,1],
            "smoking_dirty": [5,6],
            }
        
        self.animation_dictionary = {
            'walking':       [],
            "petting":       [],
            "smoking":       [],
            'walking_dirty': [],
            "petting_dirty": [],
            "smoking_dirty": [],
        }

        self.get_animation_dict()
        
    def animation_state(self,action):
        return self.sprite.animation_state(action,self.animation_speed)
        




class Giorno(JoJo):
    def __init__(self) -> None:
        super().__init__()
        self.money_generation_rate = 1.3


class Kakyoin(JoJo):
    def __init__(self) -> None:
        super().__init__()

