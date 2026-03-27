from pygame import Rect
from Game import Game

class Animation:
    name : str 
    frames : list[Rect]
    fps : float
    lastFrameStartTime : float
    frame_index : int = 0

    def __init__(self, name : str = "Animation", frames : list[Rect] = [], fps : float = 5):
        self.frames = frames
        self.fps = fps
        self.name = name

    def update(self, game : Game):
        pass
