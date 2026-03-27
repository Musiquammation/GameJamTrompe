from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from Game import Game

import pygame
from Entity import Entity

class Monster(Entity):
    def update(self, game : Game):
        super()

        direction : pygame.Vector2 = -pygame.Vector2(self.x, self.y) + pygame.Vector2(game.player.x, game.player.y)
        if direction.length_squared() > 0:
            direction.normalize()

        self.vx = direction.x
        self.vy = direction.y