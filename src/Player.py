from __future__ import annotations

from pygame import Surface, Color
from typing import TYPE_CHECKING
from Entity import Entity

if TYPE_CHECKING:
	from Game import Game


ACCELERATION = 1
ACC_REVERSE = 2
SLOW_DOWN = .1
DECELERATION = 3

SIZE=32

class Player(Entity):
	maxSpeed = 10

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
	def update(self, game : Game):
		self.updateSpeed(game)
		self.move(game)

		
				


	def draw(self, screen: Surface, game: Game):
		rect=game.toCamera(self.x, self.y, 0, SIZE, SIZE)
		screen.fill(Color(255,255,0), rect)