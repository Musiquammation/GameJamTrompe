import pygame

KEYS_DICT = {
	'left': [pygame.K_LEFT, pygame.K_q],
	'right': [pygame.K_RIGHT, pygame.K_d],
	'up': [pygame.K_UP, pygame.K_z],
	'down': [pygame.K_DOWN, pygame.K_s],
	'take': [pygame.K_a],
	'mouse-left': [-1],
	'mouse-right': [-2],
	'mouse-middle': [-3],
}

class InputHandler:
	_mouseX = 0
	_mouseY = 0
	_gameMouseX: float = 0
	_gameMouseY: float = 0
	_pressed_keys = set()
	_first_pressed_keys = set()

	def addKey(self, key: int):
		if key not in self._pressed_keys:
			self._first_pressed_keys.add(key)
		self._pressed_keys.add(key)

	def removeKey(self, key: int):
		self._pressed_keys.discard(key)
		self._first_pressed_keys.discard(key)

	def isPressed(self, key: str):
		return any(k in self._pressed_keys for k in KEYS_DICT.get(key, []))

	def isFirstPressed(self, key: str):
		return any(k in self._first_pressed_keys for k in KEYS_DICT.get(key, []))

	def appendMouse(self, x: int, y: int):
		self._mouseX = x
		self._mouseY = y

	def getGameMouse(self):
		return (self._gameMouseX, self._gameMouseY)

	def frame(self, camX: float, camY: float, camZ: float):
		self._first_pressed_keys.clear()

		self._gameMouseX = (self._mouseX - 400) * camZ + camX
		self._gameMouseY = (self._mouseY - 225) * camZ + camY		
		
