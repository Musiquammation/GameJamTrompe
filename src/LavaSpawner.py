from __future__ import annotations
from typing import TYPE_CHECKING
from pygame import Vector2
from Lava import Lava
from randomPointAroundPlayer import randomPointAroundPlayer

if TYPE_CHECKING:
	from Game import Game


class LavaSpawner:
	couldown = -1000
	rythm = 1700
	radius = 800

	def update(self, game: Game):
		self.couldown -= 1
		if self.couldown > 0:
			return
		
		self.couldown += self.rythm
		point = randomPointAroundPlayer(game.player.x, game.player.y, self.radius)
		game.lavas.append(Lava(point[0], point[1]))


