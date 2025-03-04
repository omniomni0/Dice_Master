import random

async def coin_f() -> str:
	coin_res = random.randint(1, 2)
	if coin_res == 1:
		print("Орёл / Дракон")
		return "CAACAgIAAxkBAAEI2-Vm-rfm9Qtgxa1WyM_0psS4sIvtfgACVAADUqjXBMz71bIdmgEhNgQ"
	else:
		print("Решка / Штурвал")
		return "CAACAgIAAxkBAAEI2-dm-rfohfhUhdZxWYTQRRvqxfY7XgACVQADUqjXBGVDO3J4yuC9NgQ"