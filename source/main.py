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
        self.background = pygame.image.load('graphics/test_jotaro/background_egypt.png').convert_alpha()

        self.character_update_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.character_update_timer, 5000)

        self.day_timer = pygame.USEREVENT +2
        #TODO prolong days after tests
        pygame.time.set_timer(self.day_timer, 10000)
        

        self.play_countdown = 0
        self.feed_countdown = 0
        self.clean_countdown = 0
        self.cure_countdown = 0



    def run(self):
        #TODO temp declaration / 
        #FIXME HOW UTTONS BETTER????
        jojo = Jotaro()

        #BUTTONS
        play_button = Button('play')
        feed_button = Button('feed')
        clean_button = Button('clean')
        cure_button = Button('cure')

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

                    # leeft mouse button click
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        #jojo.animation_statee rect
                        if jojo_rect.collidepoint(event.pos):
                            jojo.pet()

                        #FIXME how to compress that
                        #BUTTONS
                        if play_rect.collidepoint(event.pos) and self.play_countdown == 0:
                            self.play_countdown = 20

                        if feed_rect.collidepoint(event.pos) and self.feed_countdown == 0:
                            self.feed_countdown = 20

                        if clean_rect.collidepoint(event.pos) and self.clean_countdown == 0:
                            self.clean_countdown = 20

                        if cure_rect.collidepoint(event.pos) and self.cure_countdown == 0:
                            self.cure_countdown = 20



            if self.game_active:


                jojo_surface = jojo.animation_state('walking')
                jojo_rect = jojo_surface.get_rect(center = (WIDTH*1.5/5,HEIGHT*2.8/5))
                jojo.update()
                
                #BUTTONS
                if self.play_countdown > 0:
                    play_surface = play_button.animation_state(offset=1)
                    self.play_countdown -= 1
                else: play_surface = play_button.default_animation_state()
                play_rect = play_surface.get_rect(center = (WIDTH*4/5, HEIGHT/5))

                if self.feed_countdown > 0:
                    feed_surface = feed_button.animation_state(offset=1)
                    self.feed_countdown -= 1
                else: feed_surface = feed_button.default_animation_state()
                feed_rect = feed_surface.get_rect(center = (WIDTH*4/5, HEIGHT*1.5/5))

                if self.clean_countdown > 0:
                    clean_surface = clean_button.animation_state(offset=1)
                    self.clean_countdown -= 1
                else: clean_surface = clean_button.default_animation_state()
                clean_rect = clean_surface.get_rect(center = (WIDTH*4/5, HEIGHT*2/5))

                if self.cure_countdown > 0:
                    cure_surface = cure_button.animation_state(offset=1)
                    self.cure_countdown -= 1
                else: cure_surface = cure_button.default_animation_state()
                cure_rect = cure_surface.get_rect(center = (WIDTH*4/5, HEIGHT*2.5/5))



                print(f'age: {jojo.age}')
                print(f'hunger: {jojo.hunger}')
                print(f'happiness {jojo.happiness}')
                print(f'clean {jojo.cleanliness}')
                print(f'poop {jojo.physiological_need}')
                print(f'#######')
                
                self.screen.blit(self.background, (0,0))
                self.screen.blit(jojo_surface, jojo_rect)
                self.screen.blit(play_surface,play_rect)
                self.screen.blit(feed_surface,feed_rect)
                self.screen.blit(clean_surface,clean_rect)
                self.screen.blit(cure_surface,cure_rect)
                #self.screen.blit(button.name_text, button.button_rect)
        
    
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()