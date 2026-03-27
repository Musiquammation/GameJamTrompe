from __future__ import annotations

from pygame import Surface
from typing import TYPE_CHECKING
from Entity import Entity

if TYPE_CHECKING:
	from Game import Game


ACCELERATION = 120
DECELERATION = 60
STOP = 180

class Player(Entity):
	maxSpeed = 100

	def update(self, game : Game):
		# Handle speed logic

		pressLeft = game.inputHandler.isPressed('left')
		pressRight = game.inputHandler.isPressed('right')

		print(pressLeft, pressRight)		
		# if self.vx < 0:


	 