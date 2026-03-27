import pygame

KEYS_DICT = {
	'left': [pygame.K_LEFT, pygame.K_a],
	'right': [pygame.K_RIGHT, pygame.K_d],
	'up': [pygame.K_UP, pygame.K_w],
	'down': [pygame.K_DOWN, pygame.K_s]
}

class InputHandler:
	def __init__(self):
		self._pressed_keys = set()
		self._first_pressed_keys = set()

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

	def frame(self):
		self._first_pressed_keys.clear()