from Entity import Entity

CHEESE_HP = 300

class Cheese(Entity):
	hp: float = CHEESE_HP

	def getTexture(self) -> str | None:
		return "assets/textures/cheese.png"
	
	def getSize(self) -> tuple[int, int]:
		return (16,16)
	
	def getHp(self) -> tuple[float, float] | None:
		return (self.hp, CHEESE_HP)
