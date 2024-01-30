import time

import psycopg2
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from tbot.tbot import config, keyboard
import logging  # модуль для вывода информации

storage = MemoryStorage()  # FSM
bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)  # Хранилище состояний в оперативной памяти
answers = 0
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.INFO,
                    )


class product(StatesGroup):
    pr_all = State()
    pr_ed = State()
    pr_ed2 = State()
    ord = State()


product_art = ''


@dp.message_handler(Command("start"), state=None)  # задаем название команды start
async def welcome(message):
    await bot.send_message(message.chat.id, f"Привет, *{message.from_user.first_name},* бот работает",
                           reply_markup=keyboard.start, parse_mode='Markdown')


@dp.message_handler(content_types=['text'])
async def get_message(message):
    if message.text == "Товары":
        await product.pr_all.set()
    if message.text == "Заказы":
        await product.ord.set()
        # await message.answer("Посмотреть статистику?")
    if message.text == "Управление запасами":
        await message.answer("Введите артикул товара")
        await product.pr_ed.set()


@dp.message_handler(content_types=['text'], state=product.pr_ed)
async def upp(message, state: FSMContext):
    global product_art
    product_art = message.text
    product_art = product_art.strip()

    await message.answer("Введите количество товара")
    await product.pr_ed2.set()


@dp.message_handler(content_types=['text'], state=product.pr_ed2)
async def upp(message, state: FSMContext):
    global product_art
    conn = psycopg2.connect(dbname="sale", host="localhost", user="admin", password="6410656", port="5432")
    cursor = conn.cursor()
    try:
        count = int(message.text)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE product_product SET quantity = {count} WHERE article = '{product_art}'")
        conn.commit()
        await message.answer("Данные обновлены")
    except:
        await message.answer("Данные введенны не корректно")

    cursor.close()  # закрываем курсор
    conn.close()  # закрываем подключение
    await state.finish()


@dp.message_handler(content_types=['text'], state=product.pr_all)
async def upp(message, state: FSMContext):
    global cursor
    conn = psycopg2.connect(dbname="sale", host="localhost", user="admin", password="6410656", port="5432")
    cursor = conn.cursor()
    await message.answer("Имеющиеся товары:")
    await state.finish()
    cursor.execute("SELECT * FROM Product_product")
    for prod in cursor:
        await message.answer(f'#{prod[2]} - {prod[1]} ({prod[5]} шт) - {prod[4]}руб')

    cursor.close()  # закрываем курсор
    conn.close()  # закрываем подключение


@dp.message_handler(content_types=['text'], state=product.ord)
async def upp(message, state: FSMContext):
    global cursor
    await state.finish()
    conn = psycopg2.connect(dbname="sale", host="localhost", user="admin", password="6410656", port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Product_order")

    for order in cursor:
        date = f'{order[5].day}.{order[5].month}.{order[5].year}'

        if order[0] == 2:
            await message.answer(f'#{order[0]} - от {date} : ')
        if order[0] == 1:
            await message.answer(f'#{order[0]} - от {date} : +')
        if order[0] == 0:
            await message.answer(f'#{order[0]} - от {date} : -')

    cursor.close()  # закрываем курсор
    conn.close()  # закрываем подключение


@dp.callback_query_handler(text_contains='cancle')
async def cancle(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text='Возврат в главное меню', parse_mode='Markdown')


if __name__ == '__main__':
    print('Бот запущен!')  # Чтобы бот работал всегда с выводом в начале вашего любого текста
    executor.start_polling(dp, skip_updates=True)
