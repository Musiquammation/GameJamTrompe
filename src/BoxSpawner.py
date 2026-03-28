from __future__ import annotations
from typing import TYPE_CHECKING
from pygame import Vector2
from Box import Box
from randomPointAroundPlayer import randomPointAroundPlayer
import random

if TYPE_CHECKING:
	from Game import Game


class BoxSpawner:
	radius = 400
	rythm = 600
	couldown = -(rythm*2+100)

	def update(self, game: Game):
		self.couldown -= 1
		if self.couldown > 0:
			return

		self.couldown += self.rythm
		point = randomPointAroundPlayer(game.player.x, game.player.y, self.radius)
		game.boxes.append(Box(point[0], point[1]))


