from turtle import delay
from dino_runner.components.game import Game
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame

if __name__ == "__main__":

    pygame.init()
    menu_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Prueba de pruebas")
    space_touched = False
    clock = pygame.time.Clock()
    maxim_quit = False
    nintendo_sequence = (
        pygame.K_UP, pygame.K_UP, pygame.K_DOWN, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT,
        pygame.K_LEFT, pygame.K_RIGHT, pygame.K_b, pygame.K_a, pygame.K_BACKSPACE)
    sequence_index = 0
    super_state = False

    while not space_touched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                space_touched = True
                maxim_quit = True

        menu_screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 170)
        welcome_text_1 = font.render("Welcome, press", True, (0, 0, 0))
        welcome_text_2 = font.render("space to continue", True, (0, 0, 0))
        welcome_text_3 = font.render("or Q to quit", True, (0, 0, 0))
        menu_screen.blit(welcome_text_1, [100, 130])
        menu_screen.blit(welcome_text_2, [30, 230])
        menu_screen.blit(welcome_text_3, [225, 330])
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            space_touched = True
        if user_input[pygame.K_q]:
            space_touched = True
            maxim_quit = True
        #if user_input[pygame.K_BACKSPACE]:
            #print("MMMMMMMMMMMMMMMMM")

        if event.type == pygame.KEYDOWN or user_input[pygame.K_a] or user_input[pygame.K_b]: #or user_input[pygame.K_KP_ENTER]:
            #user_input = pygame.key.get_pressed()
            if user_input[nintendo_sequence[sequence_index]]:
                sequence_index += 1
                #print("AAAAA")
                #print(sequence_index)
                pygame.time.delay(200)
            else: 
                sequence_index = 0
                #print("BUUUU")
        if sequence_index == (len(nintendo_sequence)):
            #print("LOGRADO")
            super_state = True
            menu_screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 170)
            welcome_text_1 = font.render("Welcome, press", True, (255, 255, 255))
            welcome_text_2 = font.render("space to continue", True, (255, 255, 255))
            welcome_text_3 = font.render("or Q to quit", True, (255, 255, 255))
            menu_screen.blit(welcome_text_1, [100, 130])
            menu_screen.blit(welcome_text_2, [30, 230])
            menu_screen.blit(welcome_text_3, [225, 330])
        
        #print(keyA)
        pygame.display.flip()
        #clock.tick(30)

    if not maxim_quit:
        game = Game(super_state)
        game.run()
