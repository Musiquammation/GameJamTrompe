from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from pygame import Surface, Color
from Entity import Entity
from Lasso import Lasso
from math import sqrt

if TYPE_CHECKING:
	from Game import Game
	from Cheese import Cheese


ACCELERATION = 1
ACC_REVERSE = 2
SLOW_DOWN = .1
DECELERATION = 3
CHEESE_RANGE = 140
CHEESE_FIX_RANGE = 15
ASPIRATION_SPEED = .4
MOUSE_DAMAGE = 8

SIZE=32
PLAYER_HP = 100

class Player(Entity):
	maxSpeed = 6
	lasso = Lasso()
	takenCheese: Optional[Cheese] = None
	hp = PLAYER_HP

	def getHp(self) -> tuple[float, float] | None:
		return (self.hp, PLAYER_HP)

	def updateSpeed(self, game: Game):
		pressLeft = game.inputHandler.isPressed('left')
		pressRight = game.inputHandler.isPressed('right')
		pressUp = game.inputHandler.isPressed('up')
		pressDown = game.inputHandler.isPressed('down')

		if pressRight:
			max_speed = self.maxSpeed
			vx = self.vx

			if vx > max_speed:
				vx -= SLOW_DOWN
				if vx < max_speed:
					vx = max_speed
			else:
				if vx < 0:
					vx += ACC_REVERSE
				else:
					vx += ACCELERATION

				if vx > max_speed:
					vx = max_speed

			self.vx = vx

		elif pressLeft:
			max_speed = -self.maxSpeed
			vx = self.vx

			if vx < max_speed:
				vx += SLOW_DOWN
				if vx > max_speed:
					vx = max_speed
			else:
				if vx > 0:
					vx -= ACC_REVERSE
				else:
					vx -= ACCELERATION

				if vx < max_speed:
					vx = max_speed

			self.vx = vx

		else:
			if self.vx > 0:
				self.vx -= DECELERATION
				if self.vx < 0:
					self.vx = 0

			elif self.vx < 0:
				self.vx += DECELERATION
				if self.vx > 0:
					self.vx = 0
				

		if pressDown:
			max_speed = self.maxSpeed
			vy = self.vy

			if vy > max_speed:
				vy -= SLOW_DOWN
				if vy < max_speed:
					vy = max_speed
			else:
				if vy < 0:
					vy += ACC_REVERSE
				else:
					vy += ACCELERATION

				if vy > max_speed:
					vy = max_speed

			self.vy = vy

		elif pressUp:
			max_speed = -self.maxSpeed
			vy = self.vy

			if vy < max_speed:
				vy += SLOW_DOWN
				if vy > max_speed:
					vy = max_speed
			else:
				if vy > 0:
					vy -= ACC_REVERSE
				else:
					vy -= ACCELERATION

				if vy < max_speed:
					vy = max_speed

			self.vy = vy

		else:
			if self.vy > 0:
				self.vy -= DECELERATION
				if self.vy < 0:
					self.vy = 0

			elif self.vy < 0:
				self.vy += DECELERATION
				if self.vy > 0:
					self.vy = 0

	def careAboutLava(self) -> bool:
		return True

	def handleLasso(self, game: Game):
		# Increase / Decrease lasso
		mouseLeft = game.inputHandler.isPressed('mouse-left')
		if mouseLeft:
			if len(self.lasso.points) == 0:
				self.lasso.setSpawn(self.x, self.y)
				
			(mx, my) = game.inputHandler.getGameMouse()
			self.lasso.append(mx, my)
		elif len(self.lasso.points) > 0:
			self.lasso.increasing = False
			self.lasso.removePoint()

		lasso = self.lasso.getLassoPoint()
		if lasso:
			if self.takenCheese:
				if mouseLeft:
					self.takenCheese.x = lasso[0]
					self.takenCheese.y = lasso[1]
				else:
					self.takenCheese.taken = False
					self.takenCheese = None

			else:
				list = game.collectCheesesInRange(lasso[0], lasso[1], CHEESE_RANGE*CHEESE_RANGE)
				for (cheese, dx, dy, dist2) in list:
					if dist2 < CHEESE_FIX_RANGE*CHEESE_FIX_RANGE:
						cheese.x = lasso[0]
						cheese.y = lasso[1]
						cheese.vx = 0
						cheese.vy = 0
						cheese.taken = True
						self.takenCheese = cheese
						break

					scale = ASPIRATION_SPEED / sqrt(dist2)
					cheese.vx -= dx * scale
					cheese.vy -= dy * scale

		elif self.takenCheese:
			self.takenCheese.taken = False
			self.takenCheese = None

		
	def checkMouses(self, game: Game):
		for mouse in game.monsters:
			dx = mouse.x - self.x
			dy = mouse.y - self.y
			# check collision
			size = self.getSize()
			hW = size[0]/2
			hH = size[1]/2
			if abs(dx) <= hW and abs(dy) <= hH:
				self.hit(MOUSE_DAMAGE)
				mouse.hit(10000000) # kill mouse

	def update(self, game : Game):
		self.updateSpeed(game)
		self.handleLasso(game)
		self.checkMouses(game)

	def getSize(self) -> tuple[int, int]:
		return (32,32)

	def getTexture(self) -> str | None:
		return "assets/textures/elephant.png"
	
	def hit(self, damages: float) -> bool:
		self.hp -= damages
		return self.hp > 0

	def getHpColor(self) -> Color | None:
		return Color(255, 0, 63)

	def getLavaDamage(self) -> float:
		return 0.2