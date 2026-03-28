from __future__ import annotations
from typing import TYPE_CHECKING
from pygame import Vector2
from Cheese import Cheese
from randomPointAroundPlayer import randomPointAroundPlayer
from getScoreBalance import getScoreBalance

if TYPE_CHECKING:
	from Game import Game


class CheeseSpawner:
	couldown = 1
	rythm = 600
	radius = 200

	def calcFrame(self, game: Game):
		sum=0
		L = len(game.monsters)

		if L < 10:
			return 0

		for m in game.monsters:
			s = m.getSpeed() - 2.5
			if s > 0:
				sum += s

		sum /= L
		return .8 * sum * getScoreBalance(game.score)

	def update(self, game: Game):
		help = self.calcFrame(game)
		print(help)
		self.couldown -= 1 + help
		if self.couldown > 0:
			return
		
		self.couldown += self.rythm
		point = randomPointAroundPlayer(game.player.x, game.player.y, self.radius)
		game.cheeses.append(Cheese(point[0], point[1]))


