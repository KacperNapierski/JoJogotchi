import pygame
from sys import exit
from random import randint, choice
from pygame.sprite import Group, GroupSingle


WIDTH = 800
HEIGHT = 400


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1,player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.3)

    def player_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity +=1
        self.rect.y += self.gravity
        if self.rect.bottom >=300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump

        else: 
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type) -> None:
        super().__init__()

        if type == 'fly':
            fly_frame_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 200

        else:
            snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [ snail_frame_1, snail_frame_2]
            y_pos = 300
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1200), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100: self.kill()

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()


def display_score():
    current_time = (pygame.time.get_ticks() - start_time)//1000
    score_surface = test_font.render(f'score: {current_time}', False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    pygame.draw.rect(screen,'#c0e8ec',score_rect.inflate(10,10), border_radius= 10)
    screen.blit(score_surface,score_rect)
    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group, False):
        obstacle_group.empty()
        return False
    else: return True


pygame.init()
#pygame.display.set_icon('')
pygame.display.set_caption('Runner')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_Music = pygame.mixer.Sound('audio/music.wav')
bg_Music.set_volume(0.5)
bg_Music.play(loops=-1)

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center =(400,200))
game_title = test_font.render('Runner', False, (64,64,64))
game_title_rect = game_title.get_rect(center = (400,75))
restart_text = test_font.render('Press SPACE to run', False, (64,64,64))
restart_text_rect = restart_text.get_rect(center = (400,325))

obstacle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer, 1500)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active == True:
            if event.type == obstacle_timer:
                    obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface,(0,300))
        score = display_score()
        player.update()
        player.draw(screen)

        obstacle_group.draw(screen)
        obstacle_group.update()
        game_active = collision_sprite()
    
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        player_gravity = 0
        score_message = test_font.render(f'Your score: {score}', False,(64,64,64))
        score_message_rect = score_message.get_rect(center=(400,325))
        screen.blit(game_title, game_title_rect)
        if score == 0:
            screen.blit(restart_text, restart_text_rect)
        else:
            screen.blit(score_message, score_message_rect)
    
    pygame.display.update()
    clock.tick(60)