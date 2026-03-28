from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import pygame
import LAVASTATS
from GAMESIZE import GAMESIZE
from SCREEN import SCREEN

from math import sqrt


if TYPE_CHECKING:
	from Game import Game
	from Animation import Animation

class Entity:
	x: float
	y: float
	z: float
	vx: float
	vy: float
	
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y
		self.z = 0
		self.vx = 0
		self.vy = 0

	def careAboutLava(self) -> bool:
		return True

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

		if self.careAboutLava():
			self.checkLava(game)

	def getLavaDamage(self) -> float:
		return 0

	def checkLava(self, game: Game):
		damage = self.getLavaDamage()
		hot = False

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
				self.hit(damage)
				hot = True

		self.markLava(hot)
				

	def update(self, game: Game):
		pass

	def draw(self, screen : pygame.Surface, game: Game):
		textureName = self.getTexture()
		if textureName == None:
			return
		
		size = self.getSize()

		if self.vx < 0:
			texture = game.textureLoader.getFlippedTexture(textureName)
		else:
			texture = game.textureLoader.getTexture(textureName)

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
		texture = game.textureLoader.getTexture(textureName)
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
		elif rect.left > SCREEN.w - rw2:
			rect.left = SCREEN.w - rw2
			notEdited = False

		if rect.bottom < rh2:
			rect.top = -rh2
			notEdited = False
		elif rect.top > SCREEN.h - rh2:
			rect.top = SCREEN.h - rh2
			notEdited = False

		screen.blit(texture, rect)

		if notEdited:
			self.drawHp(screen, rect)

	def getSizeInc(self) -> float:
		return 2
	
	def markLava(self, hot: bool):
		pass

	def drawHp(self, screen: pygame.Surface, rect: pygame.Rect):
		HP_BAR_DISTANCE = 10
		HP_BAR_HEIGHT = 7
		HP_BAR_PADDING = 1
		sizeInc = self.getSizeInc()

		hp = self.getHp()
		color = self.getHpColor()
		if hp is None or color is None:
			return

		current, maximum = hp

		# Calcul du rectangle blanc (fond)
		white_rect_width = rect.width * sizeInc
		white_rect_height = HP_BAR_HEIGHT
		white_rect_x = rect.centerx - white_rect_width // 2
		white_rect_y = rect.top - HP_BAR_DISTANCE - white_rect_height

		white_rect = pygame.Rect(white_rect_x, white_rect_y, white_rect_width, white_rect_height)
		pygame.draw.rect(screen, (255, 255, 255), white_rect)

		# Calcul du rectangle rouge (HP)
		hp_ratio = max(0, min(1, current / maximum))
		red_rect_width = int((white_rect_width - 2 * HP_BAR_PADDING) * hp_ratio)
		red_rect_height = HP_BAR_HEIGHT - 2 * HP_BAR_PADDING
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


	def resolveCollision(self, m: Entity):
		selfSize = self.getSize()  # (width, height)
		mSize = m.getSize()        # (width, height)

		rSelf = (selfSize[0] + selfSize[1]) / 4
		rM    = (mSize[0]   + mSize[1])    / 4
		minDist = rSelf + rM

		dx = self.x - m.x
		dy = self.y - m.y
		dist = sqrt(dx * dx + dy * dy)

		if dist == 0:
			dx, dy, dist = 1.0, 0.0, 1.0

		if dist < minDist:
			# Normaliser
			nx = dx / dist
			ny = dy / dist

			# Séparer les deux entités
			overlap = minDist - dist
			self.x += nx * overlap / 2
			self.y += ny * overlap / 2
			m.x    -= nx * overlap / 2
			m.y    -= ny * overlap / 2

			# Réfléchir les vitesses sur l'axe de collision
			dvx = self.vx - m.vx
			dvy = self.vy - m.vy
			dot = dvx * nx + dvy * ny

			if dot < 0:  # seulement si ils se rapprochent
				self.vx -= dot * nx
				self.vy -= dot * ny
				m.vx    += dot * nx
				m.vy    += dot * ny

			# Clamp dans les limites du monde
			rSelfW, rSelfH = selfSize[0] / 2, selfSize[1] / 2
			rMW,    rMH    = mSize[0]    / 2, mSize[1]    / 2

			self.x = max(-GAMESIZE.x + rSelfW, min(self.x, GAMESIZE.x  - rSelfW))
			self.y = max(-GAMESIZE.y  + rSelfH, min(self.y, GAMESIZE.y - rSelfH))
			m.x    = max(-GAMESIZE.x + rMW,    min(m.x,    GAMESIZE.x  - rMW))
			m.y    = max(-GAMESIZE.y  + rMH,    min(m.y,    GAMESIZE.y - rMH))