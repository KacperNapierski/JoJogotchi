import pygame

class SpriteSheet():
    def __init__(self, image) -> None:
        self.sheet = image
        self.sprite_width = 200
        self.sprite_height = 230
        self.index = 0

        self.action_type = {
            #action_name: level on spritesheet, number of frames
            'walking': [0,4],
            "petting": [1,1],
            "smoking": [2,6],
            'walking_dirty': [3,4],
            "petting_dirty": [4,1],
            "smoking_dirty": [5,6],
            }
        
        self.animation_dictionary = {
            'walking': [],
            "petting": [],
            "smoking": [],
            'walking_dirty': [],
            "petting_dirty": [],
            "smoking_dirty": [],
        }

        self.get_animation_dict()

    def get_image(self,animation_frame:int, sprite_width:int, sprite_height:int, action:str): #, scale=1, color):
        sprite = pygame.Surface((sprite_width, sprite_height)).convert_alpha()
        sprite.blit(self.sheet, (0,0),((animation_frame * sprite_width), (self.action_type[action][0] * sprite_height), sprite_width, sprite_height))
        #sprite = pygame.transform.scale(sprite, (sprite_width * scale, sprite_height * scale))
        #sprite.set_colorkey(color)
        return sprite
    
    def get_animation_dict(self):
        for key in self.action_type:
            for frame in range(self.action_type[key][1]):
                self.animation_dictionary[key].append(self.get_image(frame,self.sprite_width, self.sprite_height, key))

    def animation_state(self, action):
        self.index += 0.03
        if self.index >= len(self.animation_dictionary[action]):
            self.index = 0
        
        return self.animation_dictionary[action][int(self.index)]