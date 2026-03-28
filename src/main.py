import pygame
from Game import Game

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Trompe them up")

game = Game()
game.runTest()

clock = pygame.time.Clock()

running = True
while running:
	game.inputHandler.frame(game.camX, game.camY, game.camZ)

	for event in pygame.event.get():
		match event.type:
			case pygame.QUIT:
				running = False

			case pygame.KEYDOWN:
				game.inputHandler.addKey(event.key)

			case pygame.KEYUP:
				game.inputHandler.removeKey(event.key)

			case pygame.MOUSEBUTTONDOWN:
				if event.button == 1: # left
					game.inputHandler.addKey(-1)
				elif event.button == 3: # right
					game.inputHandler.addKey(-3)
				elif event.button == 2: # middle
					game.inputHandler.addKey(-2)
				
			case pygame.MOUSEBUTTONUP:
				if event.button == 1: # left
					game.inputHandler.removeKey(-1)
				elif event.button == 3: # right
					game.inputHandler.removeKey(-3)
				elif event.button == 2: # middle
					game.inputHandler.removeKey(-2)

			case pygame.MOUSEMOTION:
				game.inputHandler.appendMouse(event.pos[0], event.pos[1])


	game.update()
	game.draw(screen)
	pygame.display.flip()

	clock.tick(60)

pygame.quit()