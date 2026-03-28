from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import pygame

if TYPE_CHECKING:
	from Game import Game
	from Animation import Animation

class Entity:
	x: float
	y: float
	z: float = 0
	vx = 0
	vy = 0 

	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	def move(self, game: Game):
		self.x += self.vx
		self.y += self.vy

		# Check for lava
	


	def update(self, game : Game):
		pass

	def draw(self, screen : pygame.Surface, game: Game):
		textureName = self.getTexture()
		if textureName != None:
			size = self.getSize()
			texture = game.texture_loader.get_texture(textureName)
			w = size[0]
			h = size[1]

			rect = game.toCamera(self.x, self.y, self.z, w, h)
			if texture.get_width() != w or texture.get_height() != h:
				texture = pygame.transform.scale(texture, (w, h))

			screen.blit(texture, rect)

	def hit(self, damages: float) -> bool:
		return True # still alive

	def getSize(self) -> tuple[int, int]:
		return (32,32)

	def getTexture(self) -> Optional[str]:
		return None
	
	def getHp(self) -> Optional[tuple[float,float]]:
		return None
	
	def isAlive(self) -> bool:
		hp = self.getHp()
		if hp:
			return hp[0] > 0
		
		return True

