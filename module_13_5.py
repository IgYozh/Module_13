from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
from base import my_token_id


api = my_token_id
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
knopka1 = KeyboardButton(text='Рассчитать', resize_keyboard=True)
knopka2 = KeyboardButton(text='Информация', resize_keyboard=True)
kb.add(knopka1)
kb.add(knopka2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(message):
    print('Пользователь использует команду /Start')
    await message.answer('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Давай расчитаем калории для тебя?', reply_markup=kb)


@dp.message_handler(text="Рассчитать")
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f"Для возраста - {data['age']}\nРоста - {data['growth']}\nВеса - {data['weight']}\nНорма "
                         f"калорий составляет: {10*int(data['weight'])+6.25*int(data['growth'])-5*int(data['age'])+5}")





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)