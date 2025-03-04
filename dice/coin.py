import random

async def coin_f():
	coin_res = random.randint(1, 2)
	if coin_res == 1:
		mes = "CAACAgIAAxkBAAEI2-Vm-rfm9Qtgxa1WyM_0psS4sIvtfgACVAADUqjXBMz71bIdmgEhNgQ"
		print("Орёл / Дракон")
		return mes
	else:
		mes = "CAACAgIAAxkBAAEI2-dm-rfohfhUhdZxWYTQRRvqxfY7XgACVQADUqjXBGVDO3J4yuC9NgQ"
		print("Решка / Штурвал")
		return mes