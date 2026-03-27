import pygame
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

	def move(self, game: Game) :
		self.x += self.vx
		self.y += self.vy

	def set_current_animation(self, animation_name : 'str'):
		for i in range(len(self.animations)):
			if self.animations[i].name == animation_name :
				self.animation_index = i
				self.animations[self.animation_index].frame_index = 0
				return
	
	def update(self, game : Game):
		if self.animation_index < len(self.animations):
			self.animations[self.animation_index].update(game)

		self.move(game)

	def draw(self, screen : pygame.Surface):
		current_animation : Animation = self.animations[self.animation_index]
		src_rect : pygame.Rect = current_animation.frames[current_animation.frame_index]

		screen.blit(current_animation.texture, (self.x, self), src_rect)
