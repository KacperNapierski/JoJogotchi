import pygame

class SpriteSheet():
    def __init__(self, image, width:int, height:int, description_dict:dict, animation_dict:dict, scale:float) -> None:
        self.sheet = image
        self.sprite_width = width
        self.sprite_height = height
        self.animation_index = 0
        self.action_type = description_dict
        self.animation_dictionary = animation_dict
        self.scale = scale
        self.get_animation_dict()

    def get_image(self,animation_frame:int, sprite_width:int, sprite_height:int, action:str, scale=1): #, color):
        sprite = pygame.Surface((sprite_width, sprite_height)).convert_alpha()
        sprite.blit(self.sheet, (0,0),((animation_frame * sprite_width), (self.action_type[action][0] * sprite_height), sprite_width, sprite_height))
        sprite = pygame.transform.scale(sprite, (sprite_width * scale, sprite_height * scale))
        #sprite.set_colorkey(color)
        return sprite
    
    def get_animation_dict(self):
        for key in self.action_type:
            for frame in range(self.action_type[key][1]):
                self.animation_dictionary[key].append(self.get_image(frame,self.sprite_width, self.sprite_height, key, self.scale))

    def animation_state(self, action, speed:float):
        self.animation_index += speed
        if self.animation_index >= len(self.animation_dictionary[action]):
            self.animation_index = 0
        
        return self.animation_dictionary[action][int(self.animation_index)]