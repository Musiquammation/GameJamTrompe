from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
from Entity import Entity
from LAVASTATS import *

if TYPE_CHECKING:
	from Game import Game



class Lava(Entity):
	hp = LAVA_HP

	def __init__(self, x: float, y: float):
		super().__init__(x, y)
	
	def getHp(self) -> tuple[float, float] | None:
		return (self.hp, LAVA_HP)

	def update(self, game: Game):
		self.hp -= 1

	def getSizeInc(self) -> float:
		return 1.6

	def getSize(self) -> tuple[int, int]:
		return (LAVA_SIZE, LAVA_SIZE)
	
	def getTexture(self) -> str | None:
		return "assets/textures/lava.png"

	def draw(self, screen: pygame.Surface, game: Game):
		super().drawWithIcon(screen, game)

	def getHpColor(self) -> pygame.Color:
		return pygame.Color(255, 255, 0)
