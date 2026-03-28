from __future__ import annotations
from typing import TYPE_CHECKING

from pygame.color import Color as Color

from Entity import Entity
from pygame import Surface, Vector2


if TYPE_CHECKING:
	from Game import Game



CHEESE_HP = 4000
SPEED_REDUCE = .3
MAX_DIST = 400
MAX_DIST_2 = MAX_DIST*MAX_DIST

class Cheese(Entity):
	hp: float = CHEESE_HP
	taken = False

	def getTexture(self) -> str | None:
		return "assets/textures/cheese.png"
	
	def getSize(self) -> tuple[int, int]:
		return (16,16)
	
	def getHp(self) -> tuple[float, float] | None:
		return (self.hp, CHEESE_HP)

	def hit(self, damages: float) -> bool:
		self.hp -= damages
		return self.hp > 0

	def update(self, game: Game):
		v = Vector2(self.vx, self.vy)
		l = v.length()
		l -= SPEED_REDUCE
		if l <= 0:
			self.vx = 0
			self.vy = 0
		else:
			n = v.normalize() * l
			(self.vx, self.vy) = n

		# Collect damages
		for m in game.monsters:
			dx = self.x - m.x
			dy = self.y - m.y
			d2 = dx*dx + dy*dy
			if d2 <= MAX_DIST_2:
				d = d2**0.5
				coef = (MAX_DIST - d) / MAX_DIST
				self.hit(coef)
				

	def draw(self, screen: Surface, game: Game):
		return super().drawWithIcon(screen, game)

	def getHpColor(self) -> Color:
		return Color(0, 255, 0)
