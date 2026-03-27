from pygame import Surface
from Game import Game
from Animation import Animation

class Entity:
	x: float
	y: float
	animations : list[Animation]
	animation_index : int 

	def __init__(self, x: float, y: float, _animations : list[Animation]):
		self.x = x
		self.y = y

	def move(self, dx : float, dy : float) :
		self.x += dx
		self.y += dy

	def set_current_animation(self, animation_name : str):
		for i in range()
	
	def update(self, game : Game):
		pass

	def draw(self, screen : Surface):
		pass
