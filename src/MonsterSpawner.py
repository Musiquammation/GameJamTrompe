from __future__ import annotations
from typing import TYPE_CHECKING
from pygame import Vector2
from GAMESIZE import GAMESIZE
import random
import math
from monsters.TestMonster import TestMonster


if TYPE_CHECKING:
	from Game import Game



def randomPointAroundPlayer(player_x, player_y, radius, margin=100):
	gx = -GAMESIZE.x
	gy = -GAMESIZE.y
	gw = +GAMESIZE.x
	gh = +GAMESIZE.y
	
	# Génère un point aléatoire dans le cercle
	angle = random.uniform(0, 2 * math.pi)
	x = player_x + math.cos(angle) * radius
	y = player_y + math.sin(angle) * radius

	# Clamp pour rester dans la zone avec marge
	x = max(gx + margin, min(x, gw - margin))
	y = max(gy + margin, min(y, gh - margin))
	
	return x, y


class MonsterSpawner:
	couldown = 1
	rythm = 60
	radius = 300

	def update(self, game: Game):
		self.couldown -= 1
		if self.couldown > 0:
			return
		
		self.couldown += self.rythm
		point = randomPointAroundPlayer(game.player.x, game.player.y, self.radius)
		game.monsters.append(TestMonster(point[0], point[1]))


