from pygame import Surface
from TextureLoader import TextureLoader
from InputHandler import InputHandler
from SCREEN import SCREEN

class GamePanel:
	def __init__(self, score: int, textureLoader: TextureLoader, inputHandler: InputHandler) -> None:
		self.score = score
		self.inputHandler = inputHandler
		self.textureLoader = textureLoader

	def draw(self, screen: Surface):
		screen.fill((0, 0, 0))

		font = self.textureLoader.sysFont
		
		if self.score < 0:
			firstLine = "Trompe them'up"
		else:
			firstLine = f"Score: {self.score}"

		lines = [
			firstLine,
			"",
			"ZQSD/Arrows: Move",
			"Left mouse: move trunk",
			"Good luck!",
			"",
			"Press LEFT-CLICK to start"
		]

		y = SCREEN.h // 4
		line_height = font.get_height() + 5

		for line in lines:
			text_surface = font.render(line, True, (255, 255, 255))

			x = (SCREEN.w - text_surface.get_width()) // 2

			screen.blit(text_surface, (x, y))
			y += line_height

	def update(self):
		return self.inputHandler.isFirstPressed('mouse-left')
