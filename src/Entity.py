from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import pygame
import LAVASTATS
from GAMESIZE import GAMESIZE


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
		if self.x < -GAMESIZE.x:
			self.x = -GAMESIZE.x
		elif self.x > GAMESIZE.x:
			self.x = GAMESIZE.x

		if self.y < -GAMESIZE.y:
			self.y = -GAMESIZE.y
		elif self.y > GAMESIZE.y:
			self.y = GAMESIZE.y

		self.checkLava(game)


	def checkLava(self, game: Game):
		# Check for lava
			for lava in game.lavas:
				if lava == self:
					continue

				# Check collision with lava
				size = self.getSize()
				hW = size[0]/2
				hH = size[1]/2
				half_lava = LAVASTATS.LAVA_SIZE / 2

				dx = abs(self.x - lava.x)
				dy = abs(self.y - lava.y)

				if dx <= hW + half_lava and dy <= hH + half_lava:
					# collision
					self.hit(LAVASTATS.LAVA_DAMAGES_TO_MOUSE)

	def update(self, game: Game):
		pass

	def draw(self, screen : pygame.Surface, game: Game):
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

		screen.blit(texture, rect)
		self.drawHp(screen, rect)


	def drawWithIcon(self, screen: pygame.Surface, game: Game):
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

		notEdited = True
		
		# fix rect in border
		if rect.right < rw2:
			rect.left = -rw2
			notEdited = False
		elif rect.left > game.screen_width - rw2:
			rect.left = game.screen_width - rw2
			notEdited = False

		if rect.bottom < rh2:
			rect.top = -rh2
			notEdited = False
		elif rect.top > game.screen_height - rh2:
			rect.top = game.screen_height - rh2
			notEdited = False

		screen.blit(texture, rect)

		if notEdited:
			self.drawHp(screen, rect)

	def drawHp(self, screen: pygame.Surface, rect: pygame.Rect):
		HP_BAR_DISTANCE = 10
		HP_BAR_HEIGHT = 7
		HP_BAR_PADDING = 1
		SIZE_INC = 1.2

		hp = self.getHp()
		color = self.getHpColor()
		if hp is None or color is None:
			return

		current, maximum = hp

		# Calcul du rectangle blanc (fond)
		white_rect_width = rect.width * 2
		white_rect_height = HP_BAR_HEIGHT
		white_rect_x = rect.centerx - white_rect_width // 2
		white_rect_y = rect.top - HP_BAR_DISTANCE - white_rect_height

		white_rect = pygame.Rect(white_rect_x, white_rect_y, white_rect_width, white_rect_height)
		pygame.draw.rect(screen, (255, 255, 255), white_rect)

		# Calcul du rectangle rouge (HP)
		hp_ratio = max(0, min(1, current / maximum))
		red_rect_width = int((white_rect_width - SIZE_INC * HP_BAR_PADDING) * hp_ratio)
		red_rect_height = HP_BAR_HEIGHT - SIZE_INC * HP_BAR_PADDING
		red_rect_x = white_rect_x + HP_BAR_PADDING
		red_rect_y = white_rect_y + HP_BAR_PADDING

		red_rect = pygame.Rect(red_rect_x, red_rect_y, red_rect_width, red_rect_height)
		pygame.draw.rect(screen, color, red_rect)



	def hit(self, damages: float) -> bool:
		return True # still alive

	def getSize(self) -> tuple[int, int]:
		return (32,32)

	def getTexture(self) -> Optional[str]:
		return None
	
	def getHp(self) -> Optional[tuple[float,float]]:
		return None
	
	def getHpColor(self) -> Optional[pygame.Color]:
		return None

	def isAlive(self) -> bool:
		hp = self.getHp()
		if hp:
			return hp[0] > 0
		
		return True

