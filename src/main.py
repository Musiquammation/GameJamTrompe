import pygame
from Game import Game

pygame.init()

screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("GameJam")

game = Game()

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	game.draw(screen)    
	pygame.display.flip()

pygame.quit()