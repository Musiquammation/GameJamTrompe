import pygame

class TextureLoader:

	def __init__(self):
		self.sysFont = pygame.font.SysFont("Courier New", 36)
		self.textures: dict[str, pygame.Surface] = {}
		self.flip_textures: dict[str, pygame.Surface] = {}

	def getTexture(self, path: str) -> pygame.Surface:
		if path not in self.textures:
			try:
				surface = pygame.image.load(path).convert_alpha()
				self.textures[path] = surface
			except pygame.error as e:
				print(f"Erreur de chargement : {path} - {e}")
				# Retourne une surface rose flashy par défaut en cas d'erreur
				error_surf = pygame.Surface((32, 32), pygame.SRCALPHA)
				error_surf.fill((255, 0, 255))
				self.textures[path] = error_surf
				
		return self.textures[path]

	def getFlippedTexture(self, path: str) -> pygame.Surface:
		if path not in self.flip_textures:
			original = self.getTexture(path)
			flipped = pygame.transform.flip(original, True, False)
			self.flip_textures[path] = flipped
		return self.flip_textures[path]