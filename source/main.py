import pygame, sys
from settings import *

from jojos import *
from ui import *
from tools import *


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("JoJoGotchi")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_active = True

        self.character_update_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.character_update_timer, 5000)

        self.day_timer = pygame.USEREVENT +2
        #TODO prolong days after tests
        pygame.time.set_timer(self.day_timer, 10000)
        

    def run(self):
        #TODO temp declaration
        jojo = Jotaro()
        button = Button('feed')


        while True:
            #TODO event handler class?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
                #after object get killed new object 
                #gets new age and counter restes
                if event.type == self.day_timer:
                    jojo.aging()

                if self.game_active == True:
                    if event.type == self.character_update_timer:
                        jojo.apply_needs()


                    if event.type == pygame.MOUSEBUTTONDOWN:
                        #jojo.animation_statee rect
                        if frame_rect.collidepoint(event.pos):
                            jojo.pet()
            

            if self.game_active:

                frame = jojo.animation_state('smoking')
                frame_rect = frame.get_rect(center = (WIDTH*2/5,HEIGHT*2/5))
                jojo.update()
                print(f'age: {jojo.age}')
                print(f'hunger: {jojo.hunger}')
                print(f'happiness {jojo.happiness}')
                print(f'clean {jojo.cleanliness}')
                print(f'poop {jojo.physiological_need}')
                print(f'#######')

                self.screen.blit(frame, frame_rect)
                self.screen.blit(button.name_text, button.button_rect)
        
    
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()