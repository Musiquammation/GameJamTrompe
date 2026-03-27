class InputHandler:
	def __init__(self):
		self._pressed_keys = set()
		self._first_pressed_keys = set()

	def addKey(self, key: int):
		if key not in self._pressed_keys:
			self._first_pressed_keys.add(key)
		self._pressed_keys.add(key)

	def removeKey(self, key):
		self._pressed_keys.discard(key)
		self._first_pressed_keys.discard(key)

	def isPressed(self, key):
		return key in self._pressed_keys

	def isFirstPressed(self, key):
		return key in self._first_pressed_keys

	def frame(self):
		self._first_pressed_keys.clear()


