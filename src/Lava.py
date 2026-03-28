from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
from Entity import Entity

if TYPE_CHECKING:
	from Game import Game

LAVA_HP = 1000

class Lava(Entity):
	hp = LAVA_HP
	
	def getHp(self) -> tuple[float, float] | None:
		return (self.hp, LAVA_HP)

	def update(self, game: Game):
		self.hp -= 1