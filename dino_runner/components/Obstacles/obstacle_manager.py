from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.components.Obstacles.cactus import Cactus
import pygame

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game, lifes):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(300)
                    if lifes >= 0:
                        self.obstacles.pop() #Gracias Karen
                    return True
                    #game.playing = False
                    #break
        return False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)