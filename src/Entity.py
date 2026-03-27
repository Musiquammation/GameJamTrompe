from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import pygame

if TYPE_CHECKING:
	from Game import Game
	from Animation import Animation

class Entity:
	x: float
	y: float
	vx = 0
	vy = 0 

	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	def move(self, game: Game) :
		self.x += self.vx
		self.y += self.vy

	def update(self, game : Game):
		self.move(game)

	def draw(self, screen : pygame.Surface, game: Game):
		textureName = self.getTexture()
		if textureName != None:
			texture = game.texture_loader.get_texture(textureName)
			screen.blit(texture, (self.x, self.y))

	def getTexture(self) -> Optional[str]:
		return None
