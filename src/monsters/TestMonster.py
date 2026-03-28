from __future__ import annotations
from typing import TYPE_CHECKING

from Monster import Monster
from pygame import Vector2

if TYPE_CHECKING:
	from Game import Game


class TestMonster(Monster):
	def getTexture(self):
		return "assets/textures/jerry_lvl1.png"
	
	def update(self, game : Game):
		direction : Vector2 = -Vector2(self.x, self.y) + Vector2(game.player.x, game.player.y)
		if direction.length_squared() > 0:
			direction = direction.normalize()

		self.vx = direction.x
		self.vy = direction.y

		return True

	def getFullHp(self) -> float:
		return 100