import random
from dice.phrase import *

class Roll:
	def __init__(self, min: int, max: int) -> None: 
		self.min = min
		self.max = max
		
	async def roll(self, miss, crit) -> str:
		res = random.randint(self.min, self.max)	
		if res < miss: return f"{random.choice(miss_phrase)}|{res}|"
						
		elif res > crit: return f"{random.choice(crit_phrase)}|{res}|"	

		else: return f"{random.choice(standart_phrase)}|{res}|"
				 
				

		


