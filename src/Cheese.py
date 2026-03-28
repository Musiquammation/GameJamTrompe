from __future__ import annotations
from typing import TYPE_CHECKING

from Entity import Entity
from pygame import Vector2

if TYPE_CHECKING:
	from Game import Game



CHEESE_HP = 300
SPEED_REDUCE = .1

class Cheese(Entity):
	hp: float = CHEESE_HP
	taken = False

	def getTexture(self) -> str | None:
		return "assets/textures/cheese.png"
	
	def getSize(self) -> tuple[int, int]:
		return (16,16)
	
	def getHp(self) -> tuple[float, float] | None:
		return (self.hp, CHEESE_HP)

	def update(self, game: Game):
		v = Vector2(self.vx, self.vy)
		l = v.length()
		l -= SPEED_REDUCE
		if l <= 0:
			self.vx = 0
			self.vy = 0
			return

		n = v.normalize() * l
		(self.vx, self.vy) = n
