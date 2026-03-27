from __future__ import annotations
from typing import TYPE_CHECKING

import pygame
from pygame import Surface
from Player import Player
from monsters.TestMonster import TestMonster
from InputHandler import InputHandler
from TextureLoader import TextureLoader
from random import randint

if TYPE_CHECKING:
	from Monster import Monster

class Game:
	def __init__(self):
		self.screen_width = 800
		self.screen_height = 450
		self.player = Player(0, 0)
		self.monsters : list[Monster] = []
		self.inputHandler = InputHandler()
		self.frameCount = 0
		self.camX = 0
		self.camY = 0
		self.camZ = 1
		self.texture_loader = TextureLoader()


	def runTest(self):
		for i in range(50):
			self.monsters.append(TestMonster(randint(-1000,1000), randint(-1000,1000)))

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
		self.frameCount += 1

		for monster in self.monsters:
			monster.update(self)

		for monster in self.monsters:
			monster.move(self)

		

	def draw(self, screen: Surface):
		self.camX = self.player.x
		self.camY = self.player.y

		screen.fill((0, 0, 0))
		self.player.draw(screen, self)

		for monster in self.monsters:
			monster.draw(screen, self)

		self.player.lasso.draw(screen, self)

