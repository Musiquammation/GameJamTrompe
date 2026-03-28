from __future__ import annotations
from typing import TYPE_CHECKING
from pygame import Vector2
from Cheese import Cheese
from randomPointAroundPlayer import randomPointAroundPlayer

if TYPE_CHECKING:
	from Game import Game


class CheeseSpawner:
	couldown = 1
	rythm = 1000
	radius = 200

	def update(self, game: Game):
		self.couldown -= 1
		if self.couldown > 0:
			return
		
		self.couldown += self.rythm
		point = randomPointAroundPlayer(game.player.x, game.player.y, self.radius)
		game.cheeses.append(Cheese(point[0], point[1]))


