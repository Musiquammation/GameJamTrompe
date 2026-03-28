from __future__ import annotations
from typing import TYPE_CHECKING
from pygame import Vector2
from monsters.TestMonster import TestMonster
from randomPointAroundPlayer import randomPointAroundPlayer

if TYPE_CHECKING:
	from Game import Game




class MonsterSpawner:
	couldown = 1
	rythm = 40
	radius = 300

	def update(self, game: Game):
		self.couldown -= 1
		if self.couldown > 0:
			return
		
		self.couldown += self.rythm
		point = randomPointAroundPlayer(game.player.x, game.player.y, self.radius)
		game.monsters.append(TestMonster(point[0], point[1]))


