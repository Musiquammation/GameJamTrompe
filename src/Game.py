from __future__ import annotations
from typing import TYPE_CHECKING

import pygame
from pygame import Surface
from Player import Player
from Cheese import Cheese
from Lava import Lava
from GAMESIZE import GAMESIZE
from MonsterSpawner import MonsterSpawner
from LavaSpawner import LavaSpawner
from CheeseSpawner import CheeseSpawner
from monsters.TestMonster import TestMonster
from InputHandler import InputHandler
from TextureLoader import TextureLoader
from SCREEN import SCREEN
from random import randint

if TYPE_CHECKING:
	from Monster import Monster

MONSTER_SCORE = 30


class Game:
	def __init__(self, textureLoader: TextureLoader, inputHandler: InputHandler) -> None:
		self.textureLoader = textureLoader
		self.inputHandler = inputHandler

		self.player = Player(0, 0)
		
		self.monsters: list[Monster] = []
		self.cheeses: list[Cheese] = []
		self.lavas: list[Lava] = []
		
		self.frameCount = 0
		
		self.camX = 0
		self.camY = 0
		self.camZ = 1
		
		self.monsterSpawner = MonsterSpawner()
		self.lavaSpawner = LavaSpawner()
		self.cheeseSpawner = CheeseSpawner()
		
		self.score: float = 0
		


	def toCamera(self, x, y, z, w, h):
		dz = self.camZ - z
		if dz <= 0:
			dz = 0.01

		scale = 1 / dz

		screen_w = w * scale
		screen_h = h * scale
		screen_x = (x - self.camX) * scale + SCREEN.w/2 - screen_w/2
		screen_y = (y - self.camY) * scale + SCREEN.h/2 - screen_h/2

		return pygame.Rect(int(screen_x), int(screen_y), int(screen_w), int(screen_h))

	def update(self):
		self.frameCount += 1
		self.score += .1 # survive reward

		# Update
		self.player.update(self)
		self.player.lasso.follow(self.player.x, self.player.y)

		self.monsterSpawner.update(self)
		self.cheeseSpawner.update(self)
		self.lavaSpawner.update(self)

		for monster in self.monsters:
			monster.update(self)

		for cheese in self.cheeses:
			cheese.update(self)

		for lava in self.lavas:
			lava.update(self)

		# Move
		self.player.move(self)
		for monster in self.monsters:
			monster.move(self)

		for cheese in self.cheeses:
			cheese.move(self)

		# Resolve collisions
		L = len(self.monsters)
		for i in range(L):
			for j in range(i):
				self.monsters[i].resolveCollision(self.monsters[j])

		for m in self.monsters:
			if not m.isAlive():
				self.score += MONSTER_SCORE

		# Kill
		self.monsters = [e for e in self.monsters if e.isAlive()]
		self.cheeses = [e for e in self.cheeses if e.isAlive()]
		self.lavas = [e for e in self.lavas if e.isAlive()]

		return self.player.hp <= 0

	def collectNearestCheese(self, cx: float, cy: float, maxRange2: float):
		best = None

		for cheese in self.cheeses:
			if cheese.taken:
				continue

			dx = cheese.x - cx
			dy = cheese.y - cy
			d2 = dx * dx + dy * dy
			if d2 <= maxRange2:
				best = cheese
				maxRange2 = d2

		if best == None:
			return None
		return (best, maxRange2)
	
	def collectCheesesInRange(self, cx: float, cy: float, range2: float):
		list: list[tuple[Cheese,float,float,float]] = []
		for cheese in self.cheeses:
			dx = cheese.x - cx
			dy = cheese.y - cy
			d2 = dx * dx + dy * dy
			if d2 <= range2:
				list.append((cheese, dx, dy, d2))
		
		return list




	def drawBackground(self, screen: Surface):
		rect = self.toCamera(0,0, 0, GAMESIZE.x*2, GAMESIZE.y*2)
		color = (127, 127, 127)
		pygame.draw.rect(screen, color, rect)

	def printScore(self, screen: Surface):
		score_text = f"{int(self.score):06d}"
		text_surface = self.textureLoader.sysFont.render(score_text, True, pygame.Color('white'))
		screen.blit(text_surface, (10, 10))


	def placeCamera(self):
		self.camX = self.player.x
		self.camY = self.player.y

		if self.camX < -GAMESIZE.x + SCREEN.w/2:
			self.camX = -GAMESIZE.x + SCREEN.w/2
		elif self.camX > GAMESIZE.x - SCREEN.w/2:
			self.camX = GAMESIZE.x - SCREEN.w/2

		if self.camY < -GAMESIZE.y + SCREEN.h/2:
			self.camY = -GAMESIZE.y + SCREEN.h/2
		elif self.camY > GAMESIZE.y - SCREEN.h/2:
			self.camY = GAMESIZE.y - SCREEN.h/2


	def draw(self, screen: Surface):
		screen.fill((0, 0, 0))

		# Place camera
		self.placeCamera()
		
		self.drawBackground(screen)




		for lava in self.lavas:
			lava.draw(screen, self)

		for monster in self.monsters:
			monster.draw(screen, self)

		for cheese in self.cheeses:
			cheese.draw(screen, self)


		self.player.draw(screen, self)
		self.player.lasso.draw(screen, self)

		self.printScore(screen)

