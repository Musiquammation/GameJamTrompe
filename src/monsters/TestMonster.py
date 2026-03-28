from __future__ import annotations
from typing import TYPE_CHECKING

from Monster import Monster
from pygame import Vector2

if TYPE_CHECKING:
	from Game import Game

CHEESE_RADIUS = 300

class TestMonster(Monster):
	def getTexture(self):
		return "assets/textures/jerry_lvl1.png"
	
	def update(self, game : Game):
		target = game.collectNearestCheese(self.x, self.y, CHEESE_RADIUS*CHEESE_RADIUS)
		if target == None:
			target = Vector2(game.player.x, game.player.y)
		else:
			target = Vector2(target[0].x, target[0].y)

		direction : Vector2 = -Vector2(self.x, self.y) + target
		if direction.length_squared() > 0:
			direction = direction.normalize()

		self.vx = direction.x
		self.vy = direction.y
		

	def getFullHp(self) -> float:
		return 2