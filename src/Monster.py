import pygame
from Game import Game

class Monster(Entity):
    
    def update(self, game : Game):
        super()

        direction : pygame.Vector2 = -(self.x, self.y) + (game.player.x, game.player.y)
        direction.normalize()

        self.vx = direction.x
        self.vy = direction.y