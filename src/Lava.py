from __future__ import annotations
from typing import TYPE_CHECKING
import pygame
from Entity import Entity
from LAVASTATS import *

if TYPE_CHECKING:
	from Game import Game



class Lava(Entity):
	hp = LAVA_HP

	def __init__(self, x: float, y: float):
		super().__init__(x, y)
	
	def getHp(self) -> tuple[float, float] | None:
		return (self.hp, LAVA_HP)

	def update(self, game: Game):
		self.hp -= 1

	def getSize(self) -> tuple[int, int]:
		return (LAVA_SIZE, LAVA_SIZE)
	
	def getTexture(self) -> str | None:
		return "assets/textures/lava.png"

	def draw(self, screen: pygame.Surface, game: Game):
		textureName = self.getTexture()
		if textureName == None:
			return
		
		size = self.getSize()
		texture = game.texture_loader.get_texture(textureName)
		w = size[0]
		h = size[1]

		rect = game.toCamera(self.x, self.y, self.z, w, h)
		if texture.get_width() != w or texture.get_height() != h:
			texture = pygame.transform.scale(texture, (w, h))

		# check if rect is in screen
		rw2 = int((rect.right - rect.left)/2)
		rh2 = int((rect.bottom - rect.top)/2)
		
		# fix rect in border
		if rect.right < rw2:
			rect.left = -rw2
		elif rect.left > game.screen_width - rw2:
			rect.left = game.screen_width - rw2

		if rect.bottom < rh2:
			rect.top = -rh2
		elif rect.top > game.screen_height - rh2:
			rect.top = game.screen_height - rh2

		screen.blit(texture, rect)

