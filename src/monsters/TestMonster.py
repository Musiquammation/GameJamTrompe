from __future__ import annotations
from typing import TYPE_CHECKING

from Monster import Monster
from pygame import Vector2

if TYPE_CHECKING:
	from Game import Game

CHEESE_RADIUS = 300
MONSTER_FOLLOW_ACC = .02
MONSTER_CHEESE_SPEED = 2

class TestMonster(Monster):
	followingCheese = False
	speed = MONSTER_CHEESE_SPEED

	def getTexture(self):
		if self.followingCheese:
			return "assets/textures/mouse.png"
		else:
			return "assets/textures/flying-mouse.png"
	
	def update(self, game : Game):
		target = game.collectNearestCheese(self.x, self.y, CHEESE_RADIUS*CHEESE_RADIUS)
		if target == None:
			self.followingCheese = False
			target = Vector2(game.player.x, game.player.y)
			self.speed += MONSTER_FOLLOW_ACC
		else:
			self.followingCheese = True
			target = Vector2(target[0].x, target[0].y)
			self.speed = MONSTER_CHEESE_SPEED

		direction : Vector2 = -Vector2(self.x, self.y) + target
		
		if direction.length_squared() > 0:
			direction = direction.normalize() * self.speed

		self.vx = direction.x
		self.vy = direction.y
		

	def getFullHp(self) -> float:
		return 1
	
	def careAboutLava(self) -> bool:
		return self.followingCheese