import pygame
from Game import Game

pygame.init()

screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("Trompe them up")

game = Game()
game.runTest()

clock = pygame.time.Clock()

running = True
while running:
	for event in pygame.event.get():
		match event.type:
			case pygame.QUIT:
				running = False

			case pygame.KEYDOWN:
				game.inputHandler.addKey(event.key)

			case pygame.KEYUP:
				game.inputHandler.removeKey(event.key)

			case pygame.MOUSEBUTTONDOWN:
				pass

			case pygame.MOUSEBUTTONUP:
				pass

	game.update()
	game.draw(screen)
	pygame.display.flip()

	clock.tick(60)

pygame.quit()