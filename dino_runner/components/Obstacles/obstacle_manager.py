from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.components.Obstacles.cactus import Cactus
import pygame

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)