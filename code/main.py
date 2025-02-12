import asyncio
import logging
from server.log import *
from server.tokenX import aboba
from dice.rolldice import Roll
from dice.coin import coin_f
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder 
from aiogram import F



logging.basicConfig(level=logging.INFO)
bot = Bot(token=aboba)
dp = Dispatcher()


# Стартовая комманда
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
	builder = ReplyKeyboardBuilder()
	
	builder.row(
		types.KeyboardButton(text="🎲 D20"),
		types.KeyboardButton(text="🎲 D4"),
		types.KeyboardButton(text="🎲 D6")
	)

	builder.row(
        types.KeyboardButton(text="🎲 D8"),
        types.KeyboardButton(text="🎲 D10"),
        types.KeyboardButton(text="🎲 D12")
    )

	builder.row(
		types.KeyboardButton(text="🪙 Подбросить монетку")
	)
	
	await message.answer("Выбери действие, игрок", reply_markup=builder.as_markup(resize_keyboard=True))




# Бросок *D20*
@dp.message(F.text.lower() == "🎲 d20")
async def cmd_d20(message: types.Message):
	await log_time()
	print(f"Имя: |{message.from_user.first_name}|")
	d20 = await Roll(1, 20).roll(5, 15)
	await message.answer(d20)
	print(d20)
	

# Бросок *D6*
@dp.message(F.text.lower() == "🎲 d6")
async def cmd_d6(message: types.Message):
	await log_time()
	print(f"Имя: |{message.from_user.first_name}|")
	d6 = await Roll(1, 6).roll(2, 4)
	await message.answer(d6)
	print(d6)
	

# Бросок *D4*
@dp.message(F.text.lower() == "🎲 d4")
async def cmd_d4(message: types.Message):
	await log_time()
	print(f"Имя: |{message.from_user.first_name}|")
	d4 = await Roll(1, 4).roll(2, 4)
	await message.answer(d4)
	print(d4)
	

# Бросок *D10*
@dp.message(F.text.lower() == "🎲 d10")
async def cmd_d10(message: types.Message):
	await log_time()
	print(f"Имя: |{message.from_user.first_name}|")
	d10 = await Roll(0, 9).roll(3, 7)
	await message.answer(d10)
	print(d10)
	

# Бросок *D8*
@dp.message(F.text.lower() == "🎲 d8")
async def cmd_d8(message: types.Message):
	await log_time()
	print(f"Имя: |{message.from_user.first_name}|")
	d8 = await Roll(1, 8).roll(3, 6)
	await message.answer(d8)
	print(d8)
	

# Бросок *D12*
@dp.message(F.text.lower() == "🎲 d12")
async def cmd_d12(message: types.Message):
	await log_time()
	print(f"Имя: |{message.from_user.first_name}|")
	d12 = await Roll(1, 12).roll(4, 12)
	await message.answer(d12)
	print(d12)


# Подбросить монетку
@dp.message(F.text.lower() == "🪙 подбросить монетку")
async def cmd_coin(message: types.Message):
	await log_time()
	print(f"Имя: |{message.from_user.first_name}|")
	res = await coin_f()
	await message.answer_sticker(res)

	

async def main():
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())