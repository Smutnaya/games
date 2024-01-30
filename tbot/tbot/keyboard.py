from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Основа для кнопок

product_all = types.KeyboardButton("Товары")
product_edit = types.KeyboardButton("Управление запасами")
order = types.KeyboardButton("Заказы")
# review = types.KeyboardButton("Отзывы")
start.add(product_all, product_edit, order)  # добавляем кнопки в основу бота key

# product_ = InlineKeyboardMarkup()
# btn1 = InlineKeyboardButton('Имеющиеся продукты', callback_data='Info-btn')
# btn2 = InlineKeyboardButton('Изменение запасов', callback_data='Ost-btn')
# btn3 = InlineKeyboardButton('Назад', callback_data='cancle')
# product_.add(btn1, btn2, btn3)
#
# order_ = InlineKeyboardMarkup(row_width=3)
# order_.add(InlineKeyboardButton(f'Просмотр заказов', callback_data='orders'))
# order_.add(InlineKeyboardButton(f'Обработка заказа', callback_data='process'))
# order_.add(InlineKeyboardButton(f'Назад', callback_data='cancle'))
