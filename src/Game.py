from __future__ import annotations
from typing import TYPE_CHECKING

import pygame
from pygame import Surface
from Player import Player
from Cheese import Cheese
from Lava import Lava
from monsters.TestMonster import TestMonster
from InputHandler import InputHandler
from TextureLoader import TextureLoader
from random import randint

if TYPE_CHECKING:
	from Monster import Monster

class Game:
	screen_width = 800
	screen_height = 450
	player = Player(0, 0)
	monsters : list[Monster] = []
	cheeses: list[Cheese] = []
	lavas: list[Lava] = []
	inputHandler = InputHandler()
	frameCount = 0
	camX = 0
	camY = 0
	camZ = 1
	texture_loader = TextureLoader()


	def runTest(self):
		for _ in range(50):
			self.monsters.append(TestMonster(randint(-1000,1000), randint(-1000,1000)))

		self.cheeses.append(Cheese(50, 40))
		self.lavas.append(Lava(50, 50))


	def toCamera(self, x, y, z, w, h):
		dz = self.camZ - z
		if dz <= 0:
			dz = 0.01

		scale = 1 / dz

		screen_w = w * scale
		screen_h = h * scale
		screen_x = (x - self.camX) * scale + 400 - screen_w/2
		screen_y = (y - self.camY) * scale + 225 - screen_h/2

		return pygame.Rect(int(screen_x), int(screen_y), int(screen_w), int(screen_h))

	def update(self):
		self.player.update(self)
		self.player.move(self)
		self.player.lasso.follow(self.player.x, self.player.y)

		self.frameCount += 1

		# Update
		for monster in self.monsters:
			monster.update(self)

		for cheese in self.cheeses:
			cheese.update(self)

		for lava in self.lavas:
			lava.update(self)

		# Move
		for monster in self.monsters:
			monster.move(self)

		for cheese in self.cheeses:
			cheese.move(self)

		# Kill
		self.monsters = [e for e in self.monsters if e.isAlive()]
		self.cheeses = [e for e in self.cheeses if e.isAlive()]
		self.lavas = [e for e in self.lavas if e.isAlive()]

	def collectNearestCheese(self, cx: float, cy: float, maxRange2: float):
		best = None

		for cheese in self.cheeses:
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





	def draw(self, screen: Surface):
		screen.fill((0, 0, 0))

		# Place camera
		self.camX = self.player.x
		self.camY = self.player.y


		for monster in self.monsters:
			monster.draw(screen, self)

		for cheese in self.cheeses:
			cheese.draw(screen, self)

		for lava in self.lavas:
			lava.draw(screen, self)


		self.player.draw(screen, self)
		self.player.lasso.draw(screen, self)

