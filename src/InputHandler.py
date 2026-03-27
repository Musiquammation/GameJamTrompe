class InputHandler:
	def __init__(self):
		self.keys_pressed = set()

	def addKey(self, key):
		self.keys_pressed.add(key)
		print(f"Touche '{key}' ajoutée. Touches actives : {self.keys_pressed}")

	def removeKey(self, key):
		self.keys_pressed.discard(key)  # discard ne lève pas d'erreur si la touche n'existe pas
		print(f"Touche '{key}' supprimée. Touches actives : {self.keys_pressed}")

