class ScreenDim:
    def __init__(self, w: int, h: int) -> None:
        self.w = w
        self.h = h

SCREEN_WIDTH = 1600
SCREEN = ScreenDim(SCREEN_WIDTH, int(SCREEN_WIDTH * 9/16))
