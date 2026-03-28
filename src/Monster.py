from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from Game import Game

import pygame
from Entity import Entity

class Monster(Entity):
	def __init__(self, x: float, y: float):
		self.hp = self.getFullHp()

	def getFullHp(self) -> float:
		return 100
	
	def getHp(self) -> tuple[float, float] | None:
		return (self.hp, self.getFullHp())
	
	def hit(self, damages: float) -> bool:
		self.hp -= damages
		return self.hp > 0