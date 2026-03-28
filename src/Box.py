from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
from Entity import Entity
from pygame import Surface, Vector2


if TYPE_CHECKING:
	from Game import Game


BOX_HP = 2400 # 40sec
BOX_SIZE = 48
SPEED_REDUCE = .3

class Box(Entity):
	hp = BOX_HP

	def __init__(self, x: float, y: float):
		super().__init__(x, y)
	
	def getHp(self) -> tuple[float, float] | None:
		return (self.hp, BOX_HP)

	def getSizeInc(self) -> float:
		return .8

	def update(self, game: Game):
		self.hp -= 1
		v = Vector2(self.vx, self.vy)
		l = v.length()
		l -= SPEED_REDUCE
		if l <= 0:
			self.vx = 0
			self.vy = 0
		else:
			n = v.normalize() * l
			(self.vx, self.vy) = n

	def getSize(self) -> tuple[int, int]:
		return (BOX_SIZE, BOX_SIZE)
	
	def getTexture(self) -> str | None:
		return "assets/textures/box.png"

	def draw(self, screen: pygame.Surface, game: Game):
		super().drawWithIcon(screen, game)

	def getHpColor(self) -> pygame.Color:
		return pygame.Color(127, 127, 0)
