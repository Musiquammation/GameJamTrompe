from __future__ import annotations

from pygame import Surface, Color
from typing import TYPE_CHECKING
from Entity import Entity

if TYPE_CHECKING:
	from Game import Game


ACCELERATION = 2
ACC_REVERSE = 1
SLOW_DOWN = 1
DECELERATION = 3

SIZE=32

class Player(Entity):
	maxSpeed = 100

	def update(self, game : Game):
		# Handle speed logic

		pressLeft = game.inputHandler.isPressed('left')
		pressRight = game.inputHandler.isPressed('right')

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
				
				


	def draw(self, screen: Surface):
		rect=(self.x - SIZE/2, self.y - SIZE/2 , SIZE, SIZE)
		screen.fill(Color(255,255,0), rect)
		pass
	 