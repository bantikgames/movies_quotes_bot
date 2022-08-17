from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from quiz import *

# Универсальная кнопка назад
back_button = KeyboardButton("⬅ Назад")

# Начальная клавиатура
stat_button = KeyboardButton("📊 Моя статистика")
start_game_button = KeyboardButton("🎮 Начать игру")
help_button = KeyboardButton("❔ Помощь")

begin_kb = ReplyKeyboardMarkup(resize_keyboard=True)

begin_kb.add(stat_button).add(start_game_button).add(help_button)

# Клавиатура для раздела Помощи
help_modes_button = KeyboardButton("🎮 Как играть?")
help_points_button = KeyboardButton("⭐ Игровые очки")
help_stat_button = KeyboardButton("📊 Статистика")

help_kb = ReplyKeyboardMarkup(resize_keyboard=True)

help_kb.insert(help_modes_button).insert(help_points_button).insert(help_stat_button).add(back_button)
