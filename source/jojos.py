import pygame
from pygame.sprite import Group
from settings import *

#TODO
#[ ] hides all variables of classes inside functions
#[ ] create a group and operate only on functions

class JoJo(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.cleanliness = 100
        self.hunger = 100
        self.happiness = 100
        self.money_generation_rate = 1
        self.physiological_need = 0.0
        self.pets_avaliable = 3

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


    def animation_state():
        ...

    def update(self):
        #self.apply_needs()
        self.play()
        #self.animation_state()



class Jotaro(JoJo):
    def __init__(self) -> None:
        super().__init__()
        name_font = pygame.font.Font(None,50)
        self.name = name_font.render('Jotaro', False, "green")
        self.jotaro = self.name.get_rect(center = (WIDTH//2, HEIGHT//4))



class Giorno(JoJo):
    def __init__(self) -> None:
        super().__init__()
        self.money_generation_rate = 1.3



class Kakyoin(JoJo):
    def __init__(self) -> None:
        super().__init__()

