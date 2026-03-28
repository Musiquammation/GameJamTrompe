from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
import math

if TYPE_CHECKING:
	from Game import Game

LASSO_SPEED_INC = 10
LASSO_SPEED_REMTIMES = 3

class Lasso:
	increasing = True
	points: list[tuple[float, float]] = []
	spawnX: float = 0
	spawnY: float = 0
	finalX: float = 0
	finalY: float = 0
	startX: float = 0
	startY: float = 0

	def follow(self, x: float, y: float):
		if x == self.startX and y == self.startY:
			return
			
		sx = self.startX
		sy = self.startY
		self.startX = x
		self.startY = y

		if len(self.points) < 2:
			self.points.insert(0, (sx, sy))
			return
		
		f = self.points[1]
		v = pygame.Vector2(f[0] - x, f[1] - y)
		if v.length() < LASSO_SPEED_INC:
			self.points[0] = (x,y)
		else:
			self.points.insert(0, (x, y))


	def setSpawn(self, x: float, y: float):
		self.spawnX = x
		self.spawnY = y
		self.startX = x
		self.startY = y
		self.points.append((x,y))

	def getLassoPoint(self):
		L = len(self.points)

		if L < 1:
			return None
		
		sx = self.points[L-1][0]
		sy = self.points[L-1][1]
		dx = self.finalX - sx
		dy = self.finalY - sy
		dist = math.hypot(dx, dy)

		if dist <= LASSO_SPEED_INC:
			end = (self.finalX, self.finalY)
		else:
			ratio = LASSO_SPEED_INC / dist
			end = (
				sx + dx * ratio,
				sy + dy * ratio
			)

		return end


	def append(self, x: float, y: float):
		self.finalX = x
		self.finalY = y

		(lx, ly) = self.points[len(self.points)-1]
		v = pygame.Vector2(x-lx, y-ly)
		if v.length() < LASSO_SPEED_INC:
			return
		
		delta = v.normalize() * LASSO_SPEED_INC
		self.points.append((delta.x + lx, delta.y + ly))
		
	def removePoint(self):
		for _ in range(LASSO_SPEED_REMTIMES):
			if len(self.points) == 0:
				break
			
			self.points.pop()
		
	def hasLasso(self):
		return len(self.points) > 0

	def apply(self):
		# print(self.points)
		pass

	def draw(self, screen: pygame.Surface, game: Game):
		if len(self.points) < 2:
			return

		color = (128, 0, 128)
		width = 3

		L = len(self.points)
		for i in range(L):
			start = self.points[i]

			if i < L - 1:
				end = self.points[i + 1]

			elif self.increasing:
				end = self.getLassoPoint()
				if end == None:
					end = start
			else:
				break

			pStart = game.toCamera(start[0], start[1], 0, 0,0)
			pEnd = game.toCamera(end[0], end[1], 0, 0,0)

			pygame.draw.line(
				screen, color,
				(pStart[0], pStart[1]),
				(pEnd[0], pEnd[1]),
				width)