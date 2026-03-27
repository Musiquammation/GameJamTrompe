from pygame import Surface
from Player import Player
from InputHandler import InputHandler

class Game:
	player = Player(0,0)
	inputHandler = InputHandler()
	frameCount = 0

	def __init__(self):
		pass

	def draw(self, screen: Surface):
		screen.fill((0, 0, 0))
		