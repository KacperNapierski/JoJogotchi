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
        
        self.poop_group = pygame.sprite.Group()



    def run(self):
        jojo = Jotaro(WIDTH*1.5/5, HEIGHT*2.8/5)

        #BUTTONS
        play_button = Button('play', WIDTH*4/5, HEIGHT/5)
        feed_button = Button('feed', WIDTH*4/5, HEIGHT*1.5/5)
        clean_button = Button('clean', WIDTH*4/5, HEIGHT*2/5)
        cure_button = Button('cure', WIDTH*4/5, HEIGHT*2.5/5)

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
                        is_poop = jojo.check_needs()
                        if is_poop != None:
                            self.poop_group.add(is_poop)
                            print('POOP')
                        jojo.apply_needs()

                    # leeft mouse button click
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        #jojo.animation_statee rect
                        if jojo_rect.collidepoint(event.pos):
                            jojo.pet()

                        #FIXME how to compress that
                        #BUTTONS
                        if play_rect.collidepoint(event.pos) and play_button.countdown == 0:
                            play_button.countdown = 20
                            jojo.play()
                        elif feed_rect.collidepoint(event.pos) and feed_button.countdown == 0:
                            feed_button.countdown  = 20
                            #jojo_surface = jojo.animation_state('walking')
                        elif clean_rect.collidepoint(event.pos) and clean_button.countdown == 0:
                            clean_button.countdown = 20
                            #jojo_surface = jojo.animation_state('walking')
                        elif cure_rect.collidepoint(event.pos) and cure_button.countdown == 0:
                            cure_button.countdown = 20



            if self.game_active:

                #BUTTONS
                play_surface, play_rect = play_button.animation_handler()
                feed_surface, feed_rect = feed_button.animation_handler()
                clean_surface,clean_rect = clean_button.animation_handler()
                cure_surface,cure_rect = cure_button.animation_handler()

                #JOJO
                jojo_surface, jojo_rect = jojo.animation_handler()
                
                #jojo.update()

                print(f'age: {jojo.age}')
                print(f'hunger: {jojo.hunger}')
                print(f'happiness {jojo.happiness}')
                print(f'clean {jojo.cleanliness}')
                print(f'poop {jojo.physiological_need}')
                print(f'#######')
                

                #BLIT
                self.screen.blit(self.background, (0,0))
                self.screen.blit(jojo_surface, jojo_rect)
                self.screen.blit(play_surface,play_rect)
                self.screen.blit(feed_surface,feed_rect)
                self.screen.blit(clean_surface,clean_rect)
                self.screen.blit(cure_surface,cure_rect)
                self.poop_group.draw(self.screen)
    
    
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()