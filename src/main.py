import pygame
from Game import Game

pygame.init()

screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("GameJam")

game = Game()

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
				# print(f"Souris cliquée : {event.button} en {event.pos}")
				pass

			case pygame.MOUSEBUTTONUP:
				# print(f"Souris relâchée : {event.button} en {event.pos}")
				pass


	game.update()
	game.draw(screen)    
	pygame.display.flip()

pygame.quit()


