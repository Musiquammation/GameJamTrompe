import pygame
from typing import Optional
from Game import Game
from GamePanel import GamePanel
from TextureLoader import TextureLoader
from InputHandler import InputHandler
from SCREEN import SCREEN

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((SCREEN.w, SCREEN.h))
pygame.display.set_caption("Trompe them up")


textureLoader = TextureLoader()
inputHandler = InputHandler()
game: Optional[Game] = None
panel = GamePanel(-1, textureLoader, inputHandler)

clock = pygame.time.Clock()

running = True

while running:
	clock.tick(60)

	if game:
		inputHandler.frame(game.camX, game.camY, game.camZ)
	else:
		inputHandler.frame(0, 0, 1)

	for event in pygame.event.get():
		match event.type:
			case pygame.QUIT:
				running = False

			case pygame.KEYDOWN:
				inputHandler.addKey(event.key)

			case pygame.KEYUP:
				inputHandler.removeKey(event.key)

			case pygame.MOUSEBUTTONDOWN:
				if event.button == 1: # left
					inputHandler.addKey(-1)
				elif event.button == 3: # right
					inputHandler.addKey(-3)
				elif event.button == 2: # middle
					inputHandler.addKey(-2)
				
			case pygame.MOUSEBUTTONUP:
				if event.button == 1: # left
					inputHandler.removeKey(-1)
				elif event.button == 3: # right
					inputHandler.removeKey(-3)
				elif event.button == 2: # middle
					inputHandler.removeKey(-2)

			case pygame.MOUSEMOTION:
				inputHandler.appendMouse(event.pos[0], event.pos[1])


	
	if game:
		u = game.update()
		game.draw(screen)

		if u:
			panel = GamePanel(int(game.score), textureLoader, inputHandler)
			game = None
	else:
		u = panel.update()
		panel.draw(screen)

		if u:
			game = Game(textureLoader, inputHandler)


	pygame.display.flip()


pygame.quit()