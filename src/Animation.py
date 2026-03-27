from pygame import Rect


class Animation:
    frames : list[Rect]
    fps : float
    lastFrameStartTime : float
    frame_index : int = 0

    def __init__(self, _frames : list[Rect] = [], _fps : float = 5):
        frames = _frames
        fps = _fps

