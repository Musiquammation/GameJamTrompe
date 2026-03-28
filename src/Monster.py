from __future__ import annotations
from typing import TYPE_CHECKING

from GAMESIZE import GAMESIZE

if TYPE_CHECKING:
	from Game import Game

from math import sqrt
import pygame
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
	

	def resolveCollision(self, m: Monster):
		selfSize = self.getSize()  # (width, height)
		mSize = m.getSize()        # (width, height)

		rSelf = (selfSize[0] + selfSize[1]) / 4
		rM    = (mSize[0]   + mSize[1])    / 4
		minDist = rSelf + rM

		dx = self.x - m.x
		dy = self.y - m.y
		dist = sqrt(dx * dx + dy * dy)

		if dist == 0:
			dx, dy, dist = 1.0, 0.0, 1.0

		if dist < minDist:
			# Normaliser
			nx = dx / dist
			ny = dy / dist

			# Séparer les deux entités
			overlap = minDist - dist
			self.x += nx * overlap / 2
			self.y += ny * overlap / 2
			m.x    -= nx * overlap / 2
			m.y    -= ny * overlap / 2

			# Réfléchir les vitesses sur l'axe de collision
			dvx = self.vx - m.vx
			dvy = self.vy - m.vy
			dot = dvx * nx + dvy * ny

			if dot < 0:  # seulement si ils se rapprochent
				self.vx -= dot * nx
				self.vy -= dot * ny
				m.vx    += dot * nx
				m.vy    += dot * ny

			# Clamp dans les limites du monde
			rSelfW, rSelfH = selfSize[0] / 2, selfSize[1] / 2
			rMW,    rMH    = mSize[0]    / 2, mSize[1]    / 2

			self.x = max(-GAMESIZE.x + rSelfW, min(self.x, GAMESIZE.x  - rSelfW))
			self.y = max(-GAMESIZE.y  + rSelfH, min(self.y, GAMESIZE.y - rSelfH))
			m.x    = max(-GAMESIZE.x + rMW,    min(m.x,    GAMESIZE.x  - rMW))
			m.y    = max(-GAMESIZE.y  + rMH,    min(m.y,    GAMESIZE.y - rMH))
