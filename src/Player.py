from __future__ import annotations
from typing import TYPE_CHECKING

from pygame import Surface, Color
from Entity import Entity
from Lasso import Lasso
from math import sqrt

if TYPE_CHECKING:
	from Game import Game


ACCELERATION = 1
ACC_REVERSE = 2
SLOW_DOWN = .1
DECELERATION = 3
CHEESE_RANGE = 500
ASPIRATION_SPEED = .3

SIZE=32

class Player(Entity):
	maxSpeed = 10
	lasso = Lasso()

	def updateSpeed(self, game: Game):
		pressLeft = game.inputHandler.isPressed('left')
		pressRight = game.inputHandler.isPressed('right')
		pressUp = game.inputHandler.isPressed('up')
		pressDown = game.inputHandler.isPressed('down')

		if pressRight:
			max_speed = self.maxSpeed
			vx = self.vx

			if vx > max_speed:
				vx -= SLOW_DOWN
				if vx < max_speed:
					vx = max_speed
			else:
				if vx < 0:
					vx += ACC_REVERSE
				else:
					vx += ACCELERATION

				if vx > max_speed:
					vx = max_speed

			self.vx = vx

		elif pressLeft:
			max_speed = -self.maxSpeed
			vx = self.vx

			if vx < max_speed:
				vx += SLOW_DOWN
				if vx > max_speed:
					vx = max_speed
			else:
				if vx > 0:
					vx -= ACC_REVERSE
				else:
					vx -= ACCELERATION

				if vx < max_speed:
					vx = max_speed

			self.vx = vx

		else:
			if self.vx > 0:
				self.vx -= DECELERATION
				if self.vx < 0:
					self.vx = 0

			elif self.vx < 0:
				self.vx += DECELERATION
				if self.vx > 0:
					self.vx = 0
				

		if pressDown:
			max_speed = self.maxSpeed
			vy = self.vy

			if vy > max_speed:
				vy -= SLOW_DOWN
				if vy < max_speed:
					vy = max_speed
			else:
				if vy < 0:
					vy += ACC_REVERSE
				else:
					vy += ACCELERATION

				if vy > max_speed:
					vy = max_speed

			self.vy = vy

		elif pressUp:
			max_speed = -self.maxSpeed
			vy = self.vy

			if vy < max_speed:
				vy += SLOW_DOWN
				if vy > max_speed:
					vy = max_speed
			else:
				if vy > 0:
					vy -= ACC_REVERSE
				else:
					vy -= ACCELERATION

				if vy < max_speed:
					vy = max_speed

			self.vy = vy

		else:
			if self.vy > 0:
				self.vy -= DECELERATION
				if self.vy < 0:
					self.vy = 0

			elif self.vy < 0:
				self.vy += DECELERATION
				if self.vy > 0:
					self.vy = 0


	def handleLasso(self, game: Game):
		# Increase / Decrease lasso
		if game.inputHandler.isPressed('mouse-left'):
			if len(self.lasso.points) == 0:
				self.lasso.setSpawn(self.x, self.y)
				
			(mx, my) = game.inputHandler.getGameMouse()
			self.lasso.append(mx, my)
		elif len(self.lasso.points) > 0:
			self.lasso.increasing = False
			self.lasso.removePoint()

		# if game.inputHandler.isPressed('take'):
		if True:
			lasso = self.lasso.getLassoPoint()
			if lasso:
				list = game.collectCheesesInRange(lasso[0], lasso[1], CHEESE_RANGE*CHEESE_RANGE)
				for (cheese, dx, dy, dist2) in list:
					scale = ASPIRATION_SPEED / sqrt(dist2)
					cheese.vx -= dx * scale
					cheese.vy -= dy * scale
				


	def update(self, game : Game):
		self.updateSpeed(game)
		self.handleLasso(game)

	def getSize(self) -> tuple[int, int]:
		return (32,32)

	def getTexture(self) -> str | None:
		return "assets/textures/elephant.png"
