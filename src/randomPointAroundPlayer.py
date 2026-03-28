from GAMESIZE import GAMESIZE
import random
import math

def randomPointAroundPlayer(player_x, player_y, radius, margin=100):
	gx = -GAMESIZE.x
	gy = -GAMESIZE.y
	gw = +GAMESIZE.x
	gh = +GAMESIZE.y
	
	# Génère un point aléatoire dans le cercle
	angle = random.uniform(0, 2 * math.pi)
	x = player_x + math.cos(angle) * radius
	y = player_y + math.sin(angle) * radius

	# Clamp pour rester dans la zone avec marge
	x = max(gx + margin, min(x, gw - margin))
	y = max(gy + margin, min(y, gh - margin))
	
	return x, y