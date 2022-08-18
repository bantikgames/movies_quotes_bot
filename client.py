import logging
import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import API_TOKEN
from keyboards.client_kb import begin_kb, help_kb
from msg import start_msg, help_modes_msg, help_points_msg, help_stat_msg, back_button_msg
from quiz import *

# Конфигурация логгирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

INDEX = 0
POINTS = 0


# Создание клавиатуры с вариантами ответа
def create_quiz_keyboard(question_number):
    with open("question.json", "r") as jsonfile:
        data = json.load(jsonfile)
        variants_kb = InlineKeyboardMarkup()
        films = data["Questions"][question_number]["Question"][0]["Film"]
        random.shuffle(films)
        for variant in films:
            variants_kb.add(InlineKeyboardButton(text=variant, callback_data=variant))
            print(len(variant))
        return variants_kb


# Действие на команду /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    check_user_id = User.select().where(User.nickname == user_id)
    if check_user_id.exists():
        print("User is exists")
    else:
        User.create(nickname=user_id)
    await message.answer(start_msg, reply_markup=begin_kb)


# Вывод статистики игрока (кол-во полученных баллов)
@dp.message_handler(Text(equals="📊 Моя статистика"))
async def my_stat(message: types.Message):
    current_user = message.from_user.id
    current_points = User.get(User.nickname == current_user).points
    await message.answer("На данный момент у вас: {} ⭐".format(current_points))


# Начало игры (вывод первого вопроса и клавиатуры с вариантами ответа)
@dp.message_handler(Text(equals="🎮 Начать игру"))
async def start_quiz(message: types.Message):
    await clear_question_json()
    await generate_question_json()
    await message.answer(get_question(INDEX)[0], reply_markup=create_quiz_keyboard(INDEX))


# Обработка нажатия на кнопки с ответами
@dp.callback_query_handler()
async def get_answer(call_back: CallbackQuery):
    global INDEX, POINTS
    await bot.answer_callback_query(call_back.id)
    if call_back.data == get_question(INDEX)[1]:
        await call_back.message.answer("Правильно: +1 ⭐")
        POINTS += 1
    else:
        await call_back.message.answer("Неверно 🙁")
    if INDEX < 10:
        INDEX += 1
        await call_back.message.answer(get_question(INDEX)[0],
                                       reply_markup=create_quiz_keyboard(INDEX))
    else:
        INDEX = 0
        await call_back.message.answer("Раунд закончился. Вы заработали {} ⭐".format(POINTS))
        await call_back.message.answer("Можете сыграть еще раз или проверить свою статистику",
                                       reply_markup=begin_kb)


# Вывод меню со справочной информации
@dp.message_handler(Text(equals="❔ Помощь"))
async def help_func(message: types.Message):
    await message.answer("Какую информацию вы бы хотели получить?", reply_markup=help_kb)


# Справка по режиму игры
@dp.message_handler(Text(equals="🎮 Как играть?"))
async def help_game_modes(message: types.Message):
    await message.answer(help_modes_msg)


# Справка по игровым очкам
@dp.message_handler(Text(equals="⭐ Игровые очки"))
async def help_points(message: types.Message):
    await message.answer(help_points_msg)


# Справка по статистике и том, как она формируется
@dp.message_handler(Text(equals="📊 Статистика"))
async def help_stat(message: types.Message):
    await message.answer(help_stat_msg)


# Кнопка Назад, которая выводит начальное меню
@dp.message_handler(Text(equals="⬅ Назад"))
async def back_button(message: types.Message):
    await message.answer(back_button_msg, reply_markup=begin_kb)


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
