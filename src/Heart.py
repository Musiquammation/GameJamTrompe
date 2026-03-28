from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
from Entity import Entity
from pygame import Surface, Vector2


if TYPE_CHECKING:
	from Game import Game


HEART_HP = 1800 # 30sec
HEART_SIZE = 48

class Heart(Entity):
	hp = HEART_HP

	def __init__(self, x: float, y: float):
		super().__init__(x, y)
	
	def getHp(self) -> tuple[float, float] | None:
		return (self.hp, HEART_HP)

	def getSizeInc(self) -> float:
		return .8

	def update(self, game: Game):
		self.hp -= 1

	def hit(self, damages: float) -> bool:
		self.hp -= damages
		return self.hp <= 0

	def getSize(self) -> tuple[int, int]:
		return (HEART_SIZE, HEART_SIZE)
	
	def getTexture(self) -> str | None:
		return "assets/textures/heart.png"

	def draw(self, screen: pygame.Surface, game: Game):
		super().drawWithIcon(screen, game)

	def getHpColor(self) -> pygame.Color:
		return pygame.Color(255, 127, 127)
