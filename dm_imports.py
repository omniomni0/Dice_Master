import asyncio
import logging
from server.log import *
from server.tokenX import TOKEN_X
from dice.rolldice import Roll
from dice.coin import coin_f
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder 
from aiogram import F
from dice.builder_rows import row_d20_d4_d6, row_d8_d10_d12