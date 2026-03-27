from __future__ import annotations

from pygame import Surface
from typing import TYPE_CHECKING
from Player import Player
from InputHandler import InputHandler


class Game:
	player = Player(0,0,[])
	inputHandler = InputHandler()
	frameCount = 0

	def __init__(self):
		pass

	def draw(self, screen: Surface):
		screen.fill((0, 0, 0))
		self.player.draw(screen)
		
	def update(self):
		self.player.update(self)