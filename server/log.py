import datetime as dt
call = 0

async def log_time():
	global call
	call += 1
	print(f"→ Вызов: [{call}] | {dt.datetime.now()}")