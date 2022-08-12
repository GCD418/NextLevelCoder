import pygame
from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING, DUCKING_SHIELD, JUMPING, JUMPING_SHIELD, RUNNING, RUNNING_SHIELD, SHIELD_TYPE, HEART
from pygame.sprite import Sprite

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5
    def __init__(self):
        self.duck_image = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
        self.run_image = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
        self.jump_image = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
        self.type = DEFAULT_TYPE
        self.image = self.run_image[self.type][0]  #RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.time_to_show = 0
        self.setup_state_booleans()
        self.lifes = 3

    def setup_state_booleans(self):
        self.has_powerup = False
        self.shield = False
        self.show_text = False#True#False
        self.shield_time_up = 0

    def update(self, user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if user_input[pygame.K_q]:
            pygame.quit() #Modificar para las vidas

        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        #self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.image = self.run_image[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        #self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.image = self.duck_image[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        #self.image = JUMPING
        self.image = self.jump_image[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, screen, points):
        font = pygame.font.Font('freesansbold.ttf', 30)#pygame.font.Font(None, 180)#pygame.font.Font('freesansbold.ttf', 180)
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2) #Por qué no da?
            if time_to_show >= 0:
                if self.show_text:
                    #print("TEXTTTTTTTTTTTTTTT")
                    #font = pygame.font.Font('freesansbold.ttf', 30)#pygame.font.Font(None, 180)#pygame.font.Font('freesansbold.ttf', 180)
                    text = font.render(f"Shield enabled for {time_to_show} seconds", True, (0, 0, 0))#F string para el format
                    #text_rect = text.get_rect()
                    #text_rect.center = (600, 4)
                    #screen.blit(text, text_rect)
                    screen.blit(text, [400, 10])

        text_points = font.render(f"Points: {points}", True, (0, 0, 0))#F string para el format        
        screen.blit(text_points, [900, 10])
        self.show_lifes(screen)
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        
    def show_lifes(self, screen): #En el futuro con imagenes
        font = pygame.font.Font('freesansbold.ttf', 30)
        lifes = font.render(f"Lifes: {self.lifes}", True, (0, 0, 0))#F string para el format        
        screen.blit(lifes, [10, 10])

    def check_invincibility(self, screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2) #Por qué no da?
            if not time_to_show >= 0:
                self.shield = False
                self.update_to_default(SHIELD_TYPE)
            #    if self.show_text:
            #        #print("TEXTTTTTTTTTTTTTTT")
            #        font = pygame.font.Font(None, 180)#pygame.font.Font('freesansbold.ttf', 180)
            #        text = font.render(f"Shield enable for {time_to_show}", True, (0, 0, 0))#F string para el format
            #        text_rect = text.get_rect()
            #        #text_rect.center = (600, 4)
            #        #screen.blit(text, text_rect)
            #        screen.blit(text, [250, 250])
            #else:
            #    self.shield = False
            #    self.update_to_default(SHIELD_TYPE)
    
    def update_to_default(self, current_type):
        if self.type == current_type:
            self.type = DEFAULT_TYPE