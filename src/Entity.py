from pygame import Surface

class Entity:
	x: float
	y: float

	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	def move(self, dx : float, dy : float) :
		self.x += dx
		self.y += dy
	
	def update(self):
		pass

	def draw(self, screen : Surface):
		pass
