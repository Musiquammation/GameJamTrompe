import pygame
from Game import Game

class Animation:
    name : str 
    texture : pygame.Surface
    frames : list[pygame.Rect]
    fps : float
    lastFrameStart : float
    frame_index : int = 0

    def __init__(self, texture_path : str ,name : str = "Animation" ,frames : list[pygame.Rect] = [], fps : float = 5):
        self.frames = frames
        self.fps = fps
        self.name = name
        self.texture = pygame.image.load(texture_path)

    def update(self, game : Game):
        if game.frameCount - self.lastFrameStart > 1/self.fps:
            self.frame_index += 1

            if self.frame_index >= len(self.frames):
                self.frame_index = 0

            self.lastFrameStart = game.frameCount
