from random import randint
from dino_runner.components.Obstacles.obstacle import Obstacle
from random import randint

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325