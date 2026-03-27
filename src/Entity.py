from pygame import Surface
from Game import Game
from Animation import Animation

class Entity:
	x: float
	y: float
	vx = 0
	vy = 0 
	animations : list[Animation]
	animation_index : int 

	def __init__(self, x: float, y: float, animations : list[Animation]):
		self.x = x
		self.y = y
		self.animations = animations
		self.animation_index = 0

	def move(self) :
		self.x += self.vx
		self.y += self.vy

	def set_current_animation(self, animation_name : str):
		for i in range(len(self.animations)):
			if self.animations[i].name == animation_name :
				self.animation_index = i

				
				return
	
	def update(self, game : Game):
		pass

	def draw(self, screen : Surface):
		pass
