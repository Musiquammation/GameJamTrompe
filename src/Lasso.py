from __future__ import annotations
from typing import TYPE_CHECKING
import pygame

if TYPE_CHECKING:
	from Game import Game

class Lasso:
	increasing = True
	points: list[tuple[float, float]] = []

	def apply(self):
		# print(self.points)
		pass

	def draw(self, screen: pygame.Surface, game: Game):
		if len(self.points) < 2:
			return  # Il faut au moins deux points pour dessiner une ligne

		color = (128, 0, 128)  # violet RGB
		width = 2  # épaisseur des lignes

		for i in range(len(self.points) - 1):
			start = self.points[i]
			end = self.points[i + 1]

			pStart = game.toCamera(start[0], start[1], 0, 0,0)
			pEnd = game.toCamera(end[0], end[1], 0, 0,0)

			print(pStart)
			pygame.draw.line(
				screen, color,
				(pStart[0], pStart[1]),
				(pEnd[0], pEnd[1]),
				width)