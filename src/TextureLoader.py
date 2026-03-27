import pygame

class TextureLoader:
    def __init__(self):
        self.textures: dict[str, pygame.Surface] = {}

    def get_texture(self, texture_path: str) -> pygame.Surface:
        if texture_path not in self.textures:
            try:
                # Chargement et optimisation immédiate du format
                surface = pygame.image.load(texture_path).convert_alpha()
                self.textures[texture_path] = surface
            except pygame.error as e:
                print(f"Erreur de chargement : {texture_path} - {e}")
                # Retourne une surface rose flashy par défaut en cas d'erreur
                error_surf = pygame.Surface((32, 32))
                error_surf.fill((255, 0, 255))
                return error_surf
                
        return self.textures[texture_path]