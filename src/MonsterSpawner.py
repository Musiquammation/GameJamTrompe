from __future__ import annotations
from typing import TYPE_CHECKING
from pygame import Vector2
from monsters.TestMonster import TestMonster
from randomPointAroundPlayer import randomPointAroundPlayer
from math import log

if TYPE_CHECKING:
	from Game import Game



def getRythm(x: float):
	return -6.211 * log(x) + 88.61

class MonsterSpawner:
	couldown: float = -200
	radius = 300

	def update(self, game: Game):
		self.couldown -= 1
		if self.couldown > 0:
			return
		
		rythm = getRythm(game.score)
		self.couldown += rythm
		print(rythm)
		point = randomPointAroundPlayer(game.player.x, game.player.y, self.radius)
		game.monsters.append(TestMonster(point[0], point[1]))


