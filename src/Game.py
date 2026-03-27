from pygame import Surface
from Player import Player

class Game:
	player = Player(0,0)

	def __init__(self):
		pass

	def draw(self, screen: Surface):
		screen.fill((0, 0, 0))
		