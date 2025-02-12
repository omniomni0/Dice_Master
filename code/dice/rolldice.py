import random
from dice.phrase import *

class Roll:
	def __init__(self, min, max):
		self.min = min
		self.max = max
		
	async def roll(self, miss, crit):
		res = random.randint(self.min, self.max)	
		if res < miss:
			chose_miss = random.choice(miss_phrase)
			mes = f"{chose_miss}|{res}|"
			return mes
		
		elif res > crit:
			chose_crit = random.choice(crit_phrase)
			mes = f"{chose_crit}|{res}|"
			return mes

		else:
			chose_standart = random.choice(standart_phrase)
			mes = f"{chose_standart}|{res}|"
			return mes	

		


