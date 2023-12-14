import pygame, sys
from settings import *
from jojos import *


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("JoJoGotchi")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_active = True

        self.character_update_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.character_update_timer, 5000)
        

    def run(self):
        #TODO temp declaration
        jojo = Jotaro()

        while True:
            #TODO event handler class?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if self.game_active == True:
                    if event.type == self.character_update_timer:
                        jojo.apply_needs()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if jojo.jotaro.collidepoint(event.pos):
                            jojo.pet()
            

            if self.game_active:
        
                pygame.draw.rect(self.screen,'#c0e8ec',jojo.jotaro)
                self.screen.blit(jojo.name, jojo.jotaro)
                jojo.update()
                print(f'hunger: {jojo.hunger}')
                print(f'happiness {jojo.happiness}')
                print(f'clean {jojo.cleanliness}')
                print(f'poop {jojo.physiological_need}')
                print(f'#######')
        
    
            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()