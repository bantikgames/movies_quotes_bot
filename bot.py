from keyboards.client_kb import begin_kb, modes_kb, help_kb
from config import API_TOKEN
from aiogram.dispatcher.filters import Text
import logging
from aiogram import Bot, Dispatcher, executor, types

# Конфигурация логгирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Стартовое сообщение и сообщение с помощью
start_msg = "🙋‍ ПРИВЕТСТВУЕМ!" + "\n" + "\n" + "Отгадывайте цитаты из фильмов, получайте баллы, соревнуйтесь с другими игроками. Вы можете получить " \
            "доступ к своей статистике или начать новую игру."

help_modes_text = "В игре существует два режима:" + "\n" + "\n" + "1️⃣ Классический: раунд состоит из 10 вопросов, " \
                                                                  "сложность которых постепенно растет." + "\n" + "\n" + \
                  "2️⃣ На время: ответьте на большее количество вопросов различной сложности за 1 минуту."

help_points_text = "За каждый правильный ответ вы получаете ⭐ (очки). Их можно тратить на подсказки. Также количество " \
                   "заработанных очков позволяет вам соревноваться с другими игроками."

help_stat_text = "Статистика ведется по каждому из режимов. В конце недели и месяца подводятся итоги."


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(start_msg, reply_markup=begin_kb)


@dp.message_handler(Text(equals="📊 Моя статистика"))
async def my_stat(message: types.Message):
    await message.answer("Здесь в скором времени появится статистика")


@dp.message_handler(Text(equals="🎮 Начать игру"))
async def start_quiz(message: types.Message):
    await message.answer("Выберите режим игры", reply_markup=modes_kb)


@dp.message_handler(Text(equals="❔ Помощь"))
async def help_func(message: types.Message):
    await message.answer("Какую информацию вы бы хотели получить?", reply_markup=help_kb)


@dp.message_handler(Text(equals="🎮 Режимы игры"))
async def help_game_modes(message: types.Message):
    await message.answer(help_modes_text)


@dp.message_handler(Text(equals="⭐ Игровые очки"))
async def help_points(message: types.Message):
    await message.answer(help_points_text)


@dp.message_handler(Text(equals="📊 Статистика"))
async def help_stat(message: types.Message):
    await message.answer(help_stat_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
