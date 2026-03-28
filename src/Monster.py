from __future__ import annotations
from typing import TYPE_CHECKING

from GAMESIZE import GAMESIZE

if TYPE_CHECKING:
	from Game import Game

from math import sqrt
from Entity import Entity

class Monster(Entity):
	def __init__(self, x: float, y: float):
		super().__init__(x,y)
		self.hp = self.getFullHp()

	def getFullHp(self) -> float:
		return 100
	
	def getHp(self) -> tuple[float, float] | None:
		return (self.hp, self.getFullHp())
	
	def hit(self, damages: float) -> bool:
		self.hp -= damages
		return self.hp > 0
	

	def getLavaDamage(self) -> float:
		return 1
	
	def getSpeed(self) -> float:
		return 1