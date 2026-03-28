from __future__ import annotations
from typing import TYPE_CHECKING
from pygame import Vector2
from Heart import Heart
from randomPointAroundPlayer import randomPointAroundPlayer
import random

if TYPE_CHECKING:
	from Game import Game


class HeartSpawner:
	radius = 500
	couldown = -1
	rythm = 2400 # 40sec

	def update(self, game: Game):
		self.couldown -= 1
		if self.couldown > 0:
			return

		self.couldown += self.rythm
		point = randomPointAroundPlayer(game.player.x, game.player.y, self.radius)
		game.hearts.append(Heart(point[0], point[1]))


