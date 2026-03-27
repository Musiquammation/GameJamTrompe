from __future__ import annotations
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
	from Game import Game
	from Animation import Animation

class Entity:
	x: float
	y: float
	vx = 0
	vy = 0 
	texture : pygame.Surface

	def __init__(self, x: float, y: float, texture_path : str):
		self.x = x
		self.y = y
		self.texture = pygame.image.load(texture_path)

	def move(self, game: Game) :
		self.x += self.vx
		self.y += self.vy

	def update(self, game : Game):
		self.move(game)

	def draw(self, screen : pygame.Surface, game: Game):
		screen.blit(self.texture, (self.x, self.y))
